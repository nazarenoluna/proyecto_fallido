from django.urls import path

from viajeros.views import (
    inicio    
)


urlpatterns = [
    path('inicio/',inicio)
]
