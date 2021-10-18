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
    )
]