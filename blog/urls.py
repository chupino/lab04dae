from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('autores/',views.lista_autores, name='lista_autores'),
    path('filtrar/',views.lista_resultado, name='lista_resultado')
]
