"""Libros views."""

# Django
from django.shortcuts import render

# Models
from libros.models import Libro
from libros.models import Resena

# Create your views here.
def detalles(request, titulo):
    """Muestra los detalles de un libro."""
    libro = Libro.objects.filter(url_libro__exact=titulo)
    libro = list(libro.values())
    libro = libro[0]
    comentarios = Resena.objects.create(comentario='Hola que tal',puntuacion='2.0',libro=libro)
    comentarios.save()
    recomendados = Libro.objects.filter(editorial__icontains=libro['editorial']).exclude(url_libro__exact=titulo)
    

    return render(
        request=request, 
        template_name='libros/detalles.html',
        context={'libro': libro, 'titulo': titulo, 'recomendados': recomendados, 'comentarios': comentarios}
    )


