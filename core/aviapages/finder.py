import requests
import os
from pathlib import Path

MAX_IMAGES = 3
BASE_DIR = Path(__file__).resolve().parent.parent

AVIAPAGES_TOKEN = os.environ.get("AVIAPAGES_TOKEN")
HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': AVIAPAGES_TOKEN
}


def generate_aircraft_info(request_json: dict) -> dict:

    images = []
    # Aircraft may have no images
    aircraft_images = request_json.get('images')
    if aircraft_images:
        for image in aircraft_images:
            images.append(image.get('url'))
            if len(images) == MAX_IMAGES:
                break

    return {
        'aircraft_id': request_json.get('aircraft_id'),
        'tail_number': request_json.get('tail_number'),
        'serial_number': request_json.get('serial_number'),
        'type_name': request_json.get('aircraft_type_name'),
        'year_of_production': request_json.get('year_of_production'),
        'images': images,
        'class_name': request_json.get('aircraft_class_name'),
        'company_name': request_json.get('company_name'),
        'home_base': request_json.get('home_base')
    }


def find_aircrafts(find_string: str, find_type: str) -> list:

    aircrafts_found = []

    page_number = 1

    # Main loop
    while True:
        found_info = get_aircraft_info(find_string, find_type, page_number)
        aircrafts_found += found_info.get('aircrafts')
        if found_info.get('next_page'):
            page_number += 1
        else:
            break

    return aircrafts_found


def get_aircraft_info(find_string: str, find_type: str, page_number: int) -> dict:

    aircrafts_found = []
    next_page = ''

    # Query Type
    if find_type.upper() == 'SERIAL':
        request_query = f'search_serial_number={find_string}'
    elif find_type.upper() == 'TAIL':
        request_query = f'search_tail_number={find_string}'

    request_url = f'https://dir.aviapages.com:443/api/aircraft/?page={page_number}&images=True&{request_query}'
    request = requests.get(url=request_url, headers=HEADERS)
    if request.status_code == 200:
        request_json = request.json()
        next_page = request_json.get('next')
        for aircraft in request_json.get('results'):
            aircrafts_found.append(generate_aircraft_info(aircraft))

    return {
        'aircrafts': aircrafts_found,
        'next_page': next_page
    }


def get_aircraft_info_by_id(aircraft_id: str) -> dict | None:

    request_url = f'https://dir.aviapages.com:443/api/aircraft/{aircraft_id}/?images=True'
    request = requests.get(url=request_url, headers=HEADERS)
    if request.status_code == 200:
        request_json = request.json()
        return generate_aircraft_info(request_json)

    return None


def get_company_info(find_string: str) -> dict | None:

    request_url = f'https://dir.aviapages.com:443/api/companies/?search_name={find_string}'
    request = requests.get(url=request_url, headers=HEADERS)
    if request.status_code == 200:
        request_json = request.json()
        for company in request_json.get('results'):
            name = company.get('name')
            if find_string.upper() == name.upper():
                return {
                    'company_name': name,
                    'company_phone': company.get('phone'),
                    'company_website': company.get('website')
                }

    return None


def get_base_info(find_string: str) -> dict | None:

    request_url = f'https://dir.aviapages.com:443/api/airports/?search_icao={find_string}'
    request = requests.get(url=request_url, headers=HEADERS)
    if request.status_code == 200:
        request_json = request.json()
        for base in request_json.get('results'):
            icao = base.get('icao')
            if find_string.upper() == icao.upper():
                return {
                    'airport_name': base.get('name'),
                    'airport_icao': icao,
                    'airport_iata': base.get('iata')
                }

    return None
