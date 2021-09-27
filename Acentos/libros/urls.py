"""Libros URLs."""

# Django
from django.urls import path

# Views
from libros import views

urlpatterns = [
    path(
        route='detalles/',
        view=views.detalles,
        name='detalles'
    ),
]