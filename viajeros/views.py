from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def inicio(request):
    return HttpResponse(f'bienvenidos. hora:{datetime.now().hour}')


def listar_lugares(request):
    return render(
        request=request,
        template_name='viajeros/lista_lugares.html')