"""Compras urls."""
# Django
from django.urls import path

# Views
from compras import views

urlpatterns = [
    path(
        route='carrito/',
        view=views.carrito,
        name='carrito'
    ),
    path(
        route= 'compra/',
        view= views.compra,
        name= 'compra',
    ),
    path(
        route= 'anadirCarrito/<str:titulo>/',
        view = views.anadirCarrito,
        name='anadirCarrito',
    ),
    path(
        route= 'eliminarCarrito/<str:titulo>/',
        view = views.eliminarCarrito,
        name='eliminarCarrito',
    )
]