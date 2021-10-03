"""Libros URLs."""

# Django
from django.urls import path

# Views
from libros import views

urlpatterns = [
    path(
        route='detalles/<str:titulo>/',
        view=views.detalles,
        name='detalles'
    ),
]