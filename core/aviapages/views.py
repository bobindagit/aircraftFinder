from django.shortcuts import render, HttpResponse
from django_tables2 import RequestConfig

from .forms import AircraftFinder, AircraftInfo
from .finder import find_aircrafts, get_aircraft_info_by_id, get_company_info, get_base_info
from .tables import MainTable


# Create your views here.
def index(request):

    error = ''

    form = AircraftFinder(request.POST)

    if request.method == 'POST':
        find_string = form['find_string'].value()
        find_type = form['find_type'].value()
        request.session['api_data'] = find_aircrafts(find_string, find_type)

    if 'api_data' not in request.session:
        request.session['api_data'] = []

    # Generating final table
    main_table = MainTable(request.session['api_data'], order_by=("type_name", "year_of_production"))
    RequestConfig(request, paginate={"per_page": 300}).configure(main_table)

    return render(request, 'aviapages/index.html', {'error': error, 'form': form, 'main_table': main_table})


def details(request, aircraft_id: str):

    aircraft_data = get_aircraft_info_by_id(aircraft_id)
    company_data = get_company_info(aircraft_data.get('company_name'))
    base_data = get_base_info(aircraft_data.get('home_base'))

    form = AircraftInfo(request.POST)

    return render(
        request,
        'aviapages/details.html',
        {'form': form, 'aircraft_data': aircraft_data, 'company_data': company_data, 'base_data': base_data}
    )
