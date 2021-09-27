"""Clientes views."""
#Django
from django.shortcuts import render

# Create your views here.

def login(request):
    """Muestra la vista para que se logee el cliente"""
    return render(request=request,template_name='clientes/login.html')