"""Busquedas views."""
# Django
from django.shortcuts import render

# Create your views here.

def resultados(request):
    """vista resultados"""
    return render(request=request, template_name="busquedas/resultados.html")