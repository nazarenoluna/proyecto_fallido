from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def inicio(request):
    return HttpResponse(f'bienvenidos. hora:{datetime.now().hour}')