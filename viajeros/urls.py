from django.urls import path

from viajeros.views import (
    inicio, listar_lugares, crear_lugar, listar_about_me, editar_lugar, buscar_lugar,
    eliminar_lugar, listar_busquedas, ver_lugar, registro, login_view, CustomLogoutView,
)


urlpatterns = [
    path('inicio/',inicio, name="inicio"),
    path('pages/',listar_lugares, name="listar_lugares"),
    path('recomendar/',crear_lugar, name="crear_lugar"),
    path('about/',listar_about_me, name="listar_about_me"),
    path('lugar/<int:id>/',editar_lugar, name="editar_lugar"),
    path('buscar_lugar/',buscar_lugar, name="buscar_lugar"),
    path('lugar/<int:id>/',eliminar_lugar, name="eliminar_lugar"),
    path('listar_recomendaciones/',listar_busquedas, name="listar_busquedas"),
    path('lugar/<int:id>/',ver_lugar, name="ver_lugar"),
    #URLS Usuario y sesion
    path('registro/',registro, name="registro"),
    path('login/',login_view, name="login"),
    path('logout/',CustomLogoutView.as_view(), name="logout"),
]
