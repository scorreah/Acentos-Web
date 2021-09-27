"""Libros views."""

# Django
from django.shortcuts import render

# Create your views here.
def detalles(request):
    """Muestra los detalles de un libro."""
    return render(request, 'libros/detalles.html')