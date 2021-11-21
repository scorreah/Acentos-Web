"""Busquedas views."""

# Django
from django.shortcuts import render, redirect

# Models
from libros.models import Libro, Autor

libros = ""
librosBU = ""
searched = ""
searchType = ""
orderType = ""
filterType = ""

# Create your views here.

def librosAll(request):
    global libros, librosBU,searched,searchType,orderType,filterType
    isLibrosAll = True
    libros = Libro.objects.all()
    return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType, 'librosAll': isLibrosAll })

def resultados(request):
    """vista resultados"""
    global libros, librosBU,searched,searchType
    if request.method == "POST":
        searched = request.POST['searched']
        searchType = request.POST.get('searchType', "Libros")
        if searchType == "Libros":
            libros = Libro.objects.filter(titulo__icontains=searched)
        elif searchType == "Autor":
            libros = Libro.objects.filter(autor__nombre__icontains=searched)
        elif searchType == "Editorial":
            libros = Libro.objects.filter(editorial__icontains=searched)
        librosBU = libros
        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType })
    else:
        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType })

def ordenar(request):
    global libros, librosBU,searched,searchType,orderType,filterType
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
        context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType }
    )

def filtrar(request):
    global libros, librosBU,searched,searchType,orderType,filterType 
    if request.method == "POST":
        filterType = request.POST.get('filterType')
        if filterType == "Inf":
            libros = libros.filter(categoria__exact="Informatica")
        if filterType == "Lun":
            libros = libros.filter(categoria__exact="Literatura universal")
        if filterType == "Fan":
            libros = libros.filter(categoria__exact="Fantasia")
        if filterType == "Bio":
            libros = libros.filter(categoria__exact="Biografia")
        if filterType == "Non":
            pass
        rango = request.POST.get('myRange')
        libros = libros.filter(precio__lte = rango)
    
    return render(
        request=request, 
        template_name="busquedas/resultados.html",
        context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType }
    )

def limpiarFiltros(request):
    global libros, librosBU,searched,searchType,orderType,filterType
    isCleanFilters = True
    return render(
        request=request, 
        template_name="busquedas/resultados.html",
        context={'searched': searched, 'searchType': searchType, 'resultados': librosBU, 'orderType': orderType, 'filterType': filterType, 'limpiarFil': isCleanFilters }
    )

