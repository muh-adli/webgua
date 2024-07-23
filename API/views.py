from django.shortcuts import render
from django.http import HttpResponse

from .models import Aff

from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    return render(request, "test1.html")

def halamanfarda(request):
    return render(request, "cobahalaman.html")

def cekjam(request):
    now = datetime.now()

    qs=Aff.objects.values('hewan')
    print(qs)

    context = {
        'jam': now,
        'data': qs
    }
    return render (request, "cekjam.html", context)