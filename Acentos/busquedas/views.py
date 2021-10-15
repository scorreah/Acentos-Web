"""Busquedas views."""

# Django
from django.shortcuts import render

# Models
from libros.models import Libro

# Create your views here.
def resultados(request):
    """vista resultados"""
    if request.method == "POST":
        searched = request.POST['searched']
        searchType = request.POST.get('searchType', "Libros")
        if searchType == "Libros":
            libros = Libro.objects.filter(titulo__icontains=searched)
        elif searchType == "Autor":
            pass
        elif searchType == "Editorial":
            libros = Libro.objects.filter(editorial__icontains=searched)
        
        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros })
    else:
        libros = Libro.objects.filter(titulo__icontains=' ')
        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': ' ', 'searchType': 'Libro', 'resultados': libros })

