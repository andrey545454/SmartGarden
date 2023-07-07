import os

from django.shortcuts import render
from requests import get
from json import loads


def index(request):
    return render(request, 'index.html')


def nature_home(request):
    return render(request, 'nature_home.html')


def nature_outside(request):
    return render(request, 'nature_outside.html')


def last_nature_home(request):
    return render(request, 'last_nature_home.html')


def add_nature(request):
    return render(request, 'add_nature.html')


def timetable(request):
    return render(request, 'timetable.html')


def sensors(request):
    res = get(
        'https://api-uae-test.ujin.tech/api/devices/get-device-info/',
        data={
            'token': os.getenv('API_TOKEN'),
            'serialnumber': os.getenv('SERIAL_NUMBER')
        }
    )
    obj = loads(res.content)
    print(obj)
    return render(request, 'sensors.html')
