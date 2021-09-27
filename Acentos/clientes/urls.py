"""Cliente Urls."""

#django
from django.urls import path

#Views
from clientes import views

urlpatterns = [
    path(
        route='login/',
        view = views.login,
        name='login'
    )
]