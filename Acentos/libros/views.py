"""Libros views."""

# Django
from django.shortcuts import render

# Models
from libros.models import Libro
from libros.models import Resena

# Create your views here.
def detalles(request, titulo):
    """Muestra los detalles de un libro."""
    if request.method == 'POST':
        libroInstance = Libro.objects.get(url_libro__exact=titulo)
        newComent = Resena.objects.create(comentario=request.POST.get('newcoment'),puntuacion='3.0',libro=libroInstance)
        newComent.save()
    libro = Libro.objects.filter(url_libro__exact=titulo)
    libro = list(libro.values())
    libro = libro[0]
    recomendados = Libro.objects.filter(editorial__icontains=libro['editorial']).exclude(url_libro__exact=titulo)
    comentarios = Resena.objects.filter(libro_id__exact= libro['ISBN'])
    divisor = comentarios.count()
    sumaTotal = 0
    puntu = 0.0
    for i in comentarios:
        sumaTotal += i.puntuacion
    puntu = sumaTotal // divisor
    puntu = float(puntu)
    libro = Libro.objects.filter(url_libro__exact=titulo).update(puntuacion=puntu)
    libro = Libro.objects.filter(url_libro__exact=titulo)
    libro = list(libro.values())
    libro = libro[0]

    return render(
        request=request, 
        template_name='libros/detalles.html',
        context={'libro': libro, 'titulo': titulo, 'recomendados': recomendados, 'comentarios': comentarios}
    )


