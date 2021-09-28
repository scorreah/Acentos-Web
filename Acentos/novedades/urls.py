"""Novedades URLs."""

# Django
from django.urls import path

# Views
from novedades import views

urlpatterns = [
    path(
        route='home/',
        view=views.home,
        name='home'
    ),
]