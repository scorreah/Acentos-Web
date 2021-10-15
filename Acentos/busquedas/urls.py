"""Busquedas urls"""
# Django
from django.urls import path

# View
from busquedas import views

urlpatterns = [
    path(
        route= "resultados/",
        view= views.resultados,
        name= "resultados",
    ),
    path(
        route= "resultados/a",
        view= views.ordenar,
        name= "ordenar",
    )
]
