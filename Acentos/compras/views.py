"""Compras views."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Models
from libros.models import Libro
from clientes.models import Carrito, LibroCarrito, Cliente
from compras.models import Compra
from usuarios.models import User

# Create your views here.
@login_required
def carrito(request):
    """Se encarga de los detalles del carrito."""
    userInstance = request.user
    user = Cliente.objects.get(user__exact=userInstance)
    libros = user.carrito.libros.all()
    cantidadLibros = libros.count()
    precioTotal = 0
    for i in libros:
        precioTotal = i.precio
    precioEnvio = precioTotal + 8500

    return render(
        request=request,
        template_name='compras/carrito.html',
        context={
            'libros': libros,
            'precioT': precioTotal,
            'cantidadLibros': cantidadLibros,
            'precioEnvio': precioEnvio,
            })

def compra(request):
    """Se encarga de confirmar la compra y seleccionar los métodos de envio y pago"""
    if request.method == 'POST':
        nombre = request.POST.get('firstname')
        tel = request.POST.get('Teléfono de contacto')
        mde = request.POST.get('Teléfono de contacto')
        mde = request.POST.get('Teléfono de contacto')
        print("A")
        val = request.POST.get('MDE')
        if val == "CE":
            metodoEnvio = "CE"
        elif val == "EO":
            metodoEnvio = "EO"
    return render(request=request,template_name='compras/compra.html')
    
@login_required
def anadirCarrito(request, titulo):
    """Se encarga de funcionalidad de anadir al carrito."""
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    user.carrito.libros.add(libroInstance)

    return redirect ('busquedas:resultados')

@login_required
def eliminarCarrito(request, titulo):
    """Se encarga de funcionalidad de eliminar al carrito."""
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    libroEliminar = user.carrito.librocarrito_set.all()
    libroEliminar.delete()
    return redirect ('compras:carrito')


