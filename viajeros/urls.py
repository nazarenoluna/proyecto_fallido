from django.urls import path

from viajeros.views import (
    inicio, listar_lugares,    
)


urlpatterns = [
    path('inicio/',inicio),
    path('lugares/',listar_lugares),
]
