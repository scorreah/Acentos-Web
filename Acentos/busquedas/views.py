"""Busquedas views."""

# Django
from django.shortcuts import render, redirect

# Models
from libros.models import Libro, Autor
from clientes.models import Cliente

libros = ""
librosBU = ""
searched = ""
searchType = ""
orderType = ""
filterType = ""
categorias = ""

# Create your views here.

def librosAll(request):
    global libros, librosBU,searched,searchType,orderType,filterType, categorias
    categorias = set(())
    for a in Libro.objects.all():
        categorias.add(a.categoria)
    isLibrosAll = True
    libros = Libro.objects.all()
    librosBU = libros
    return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType, 'librosAll': isLibrosAll, 'categorias':categorias})

def resultados(request):
    """vista resultados"""
    global libros, librosBU,searched,searchType, categorias
    if request.method == "POST":
        categorias = set(())
        for a in Libro.objects.all():
            categorias.add(a.categoria)
        searched = request.POST['searched']
        if request.user.is_authenticated:
            user = request.user
            cliente = Cliente.objects.get(user__exact=user)
            cliente.historial = cliente.historial + "--/--" + searched
            cliente.save()
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
            context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType, 'categorias':categorias })
    else:
        return render(
            request=request, 
            template_name="busquedas/resultados.html", 
            context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType, 'categorias':categorias })

def ordenar(request):
    global libros, librosBU,searched,searchType,orderType,filterType, categorias
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
        context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType, 'categorias':categorias }
    )

def filtrar(request):
    global libros, librosBU,searched,searchType,orderType,filterType , categorias
    if request.method == "POST":
        filterType = request.POST.get('filterType')
        libros = libros.filter(categoria__exact=filterType)
        rango = request.POST.get('myRange')
        libros = libros.filter(precio__lte = rango)
    
    return render(
        request=request, 
        template_name="busquedas/resultados.html",
        context={'searched': searched, 'searchType': searchType, 'resultados': libros, 'orderType': orderType, 'filterType': filterType, 'categorias':categorias }
    )

def limpiarFiltros(request):
    global libros, librosBU,searched,searchType,orderType,filterType, categorias
    isCleanFilters = True
    libros = librosBU
    return render(
        request=request, 
        template_name="busquedas/resultados.html",
        context={'searched': searched, 'searchType': searchType, 'resultados': librosBU, 'orderType': orderType, 'filterType': filterType, 'limpiarFil': isCleanFilters, 'categorias':categorias }
    )

