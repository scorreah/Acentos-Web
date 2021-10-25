"""Cliente Urls."""

#django
from django.urls import path

#Views
from clientes import views

urlpatterns = [
    # Management
    path(
        route='login/', 
        view=views.login_view, 
        name='login'
    ),
    path(
        route='logout/', 
        view=views.logout_view, 
        name='logout'
    ),
    path(
        route='signup/', 
        view=views.signup, 
        name='signup'
    ),
    path(
        route='perfil/', 
        view=views.perfil, 
        name='perfil'
    ),
]