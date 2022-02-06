FROM python:3.10.0
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /working/aviapages

COPY requirements.txt /working/aviapages/
RUN pip install --no-cache-dir -r /working/aviapages/requirements.txt

COPY /core /working/aviapages

RUN python manage.py collectstatic --noinput