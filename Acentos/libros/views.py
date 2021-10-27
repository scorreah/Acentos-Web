"""Libros views."""

# Django
from django.shortcuts import render
from django.contrib import messages

# Models
from libros.models import Libro
from compras.models import Resena

# Create your views here.
def detalles(request, titulo):
    """Muestra los detalles de un libro."""
    if request.method == 'POST' and request.user.is_authenticated:
        libroInstance = Libro.objects.get(url_libro__exact=titulo)
        aux = 0.0
        try:
            if request.POST['estrellas5']:
                aux = 5.0
        except:
            try:
                if request.POST['estrellas4']:
                    aux = 4.0
            except:
                try:
                    if request.POST['estrellas3']:
                        aux = 3.0
                except:
                    try:
                        if request.POST['estrellas2']:
                            aux = 2.0
                    except:
                        try:
                            if request.POST['estrellas1']:
                                aux = 1.0
                        except:
                            pass
        newComent = Resena.objects.create(comentario=request.POST.get('newcoment'),puntuacion=aux,libro=libroInstance)
        newComent.save()
    else:
        messages.error(request,'Logueateee putooo')

    libro = Libro.objects.filter(url_libro__exact=titulo)
    libro = list(libro.values())
    libro = libro[0]

    recomendados = Libro.objects.filter(editorial__icontains=libro['editorial']).exclude(url_libro__exact=titulo).order_by('?')[:1]
    recomendados |= Libro.objects.filter(categoria__icontains=libro['categoria']).exclude(url_libro__exact=titulo).order_by('?')[:3]


    comentarios = Resena.objects.filter(libro_id__exact= libro['ISBN'])
    divisor = comentarios.count()
    sumaTotal = 0
    puntu = 0.0
    for i in comentarios:
        sumaTotal += i.puntuacion
    try:
        puntu = sumaTotal // divisor
    except:
        puntu = 0
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


