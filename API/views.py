from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import DataGoa, DataGoaView

import json


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    # Query all objects from DataGoaView
    qs = DataGoaView.objects.values(
        'kode_desa',
        'geom_4326'
    )

    geojson = serialize('geojson', qs, fields=('kode_desa', 'geom_4326'))

    # Render the template with the JSON data
    return (request, "test1.html", {'geojson': geojson})

def goa(request):
    # Query all objects from DataGoaView
    qs = DataGoa.objects.all()

    for i in qs:
        print(i)

    # Render the template with the JSON data
    return (request, "test1.html", {'geojson': geojson})