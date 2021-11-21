"""Busquedas views."""

# Django
from django.shortcuts import render

# Models
from libros.models import Libro, Autor

libros = ""

# Create your views here.
def resultados(request):
    """vista resultados"""
    global libros
    if request.method == "POST":
        searched = request.POST['searched']
        searchType = request.POST.get('searchType', "Libros")
        if searchType == "Libros":
            libros = Libro.objects.filter(titulo__icontains=searched)
        elif searchType == "Autor":
            libros = Libro.objects.filter(autor__nombre__icontains=searched)
        elif searchType == "Editorial":
            libros = Libro.objects.filter(editorial__icontains=searched)

        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros })
    else:
        libros = Libro.objects.all()
        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': ' ', 'searchType': 'Libro', 'resultados': libros })

def ordenar(request):
    global libros
    if request.method == "POST":
        orderType = request.POST.get('orderType')
        if orderType == "Alf":
            libros = libros.order_by('titulo')
        if orderType == "Ran":
            libros = libros.order_by('puntuacion').reverse()
        if orderType == "Fec":
            libros = libros.order_by('fecha_publicacion')
    return render(
        request=request, 
        template_name="busquedas/resultados.html",
        context={'orderType': orderType, 'resultados': libros}
    )

