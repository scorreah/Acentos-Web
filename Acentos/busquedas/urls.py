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
    ),
    path(
        route= "resultados/filtrar",
        view = views.filtrar,
        name = "filtrar",
    ),
    path(
        route= "resultados/limpiar",
        view = views.limpiarFiltros,
        name= "limpiarFiltros",
    ),
    path(
        route= "resultados/librosAll",
        view = views.librosAll,
        name= "librosAll",
    )
]
