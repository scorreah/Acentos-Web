"""Libros views."""

# Django
from django.shortcuts import render

# Models
from libros.models import Libro

# Create your views here.
def detalles(request, titulo):
    """Muestra los detalles de un libro."""
    libro = Libro.objects.filter(url_libro__exact=titulo)
    libro = list(libro.values())
    libro = libro[0]
    return render(
        request=request, 
        template_name='libros/detalles.html',
        context={'libro': libro, 'titulo': titulo}
    )