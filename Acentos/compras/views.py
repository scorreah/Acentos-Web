"""Compras views."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Models
from libros.models import Libro
from clientes.models import Carrito, LibroCarrito, Cliente
from compras.models import Compra
from usuarios.models import User

# Util
import datetime

# Create your views here.
def carrito(request):
    """Se encarga de los detalles del carrito."""
    if request.user.is_authenticated:
        userInstance = request.user
        user = Cliente.objects.get(user__exact=userInstance)
        carrito = Carrito.objects.get(cliente__exact=user)
        libros = LibroCarrito.objects.filter(carrito_id__exact=carrito).all()
        cantidadLibros = 0
        precioTotal = 0
        for i in libros:
            precioTotal += i.cantidad * i.libro_id.precio
            cantidadLibros += i.cantidad
        precioEnvio = precioTotal + 8500
        carrito.precio = precioTotal
        carrito.save()
        return render(
            request=request,
            template_name='compras/carrito.html',
            context={
                'libros': libros,
                'precioT': precioTotal,
                'cantidadLibros': cantidadLibros,
                'precioEnvio': precioEnvio,
                })
    else:
        return redirect('clientes:login')

@login_required
def compra(request):
    """Se encarga de confirmar la compra y seleccionar los métodos de envio y pago"""
    userInstance = request.user
    user = Cliente.objects.get(user__exact=userInstance)
    carrito = Carrito.objects.get(cliente__exact=user)
    libros = LibroCarrito.objects.filter(carrito_id__exact=carrito).all()
    precioTotal = 8500
    cantidadLibros = 0
    for i in libros:
        precioTotal += i.cantidad * i.libro_id.precio
        cantidadLibros += i.cantidad
    if request.method == 'POST':
        cliente = Cliente.objects.get(user = request.user)
        tel = request.POST.get('Teléfono de contacto')
        mdp = ""
        if request.POST.get('MDPCT'):
            mdp = "Tarjeta de credito"
        elif request.POST.get('MDPCE'):
            mdp = "Contra-Entrega"
        elif request.POST.get('MDPCD'):
            mdp = "Tarjeta de debito"
        elif request.POST.get('MDPCP'):
            mdp = "Paypal"
        costo = precioTotal
        val = request.POST.get('MDE')
        if val == "RT":
            metodoEnvio = "Recoger en tienda"
        elif val == "EO":
            metodoEnvio = "Envio"
        compra = {
            'metodo_pago': mdp,
            'metodo_envio': metodoEnvio,
            'costo_total': costo,
            'fecha_compra': datetime.date.today,
            'cliente': cliente,
        }
        purchase = Compra.objects.create(**compra)
        purchase.save()
        limpiar = LibroCarrito.objects.filter(carrito_id__exact=carrito).all()
        for libro in limpiar:
            libro.delete()
        carrito.precio = 0
        carrito.save()
        return redirect ('novedades:home')
    else:
        return render(request=request,template_name='compras/compra.html',context={'libros':libros,'precioTotal':precioTotal, 'cantidadLibros':cantidadLibros})
    

def anadirCarrito(request, titulo):
    """Se encarga de funcionalidad de anadir al carrito."""
    if request.user.is_authenticated:
        libroInstance = Libro.objects.get(titulo__exact=titulo)
        userInstance = request.user 
        user = Cliente.objects.get(user__exact=userInstance)
        carrito = Carrito.objects.get(cliente__exact=user)
        existe = LibroCarrito.objects.filter(carrito_id__exact=carrito).filter(libro_id__exact=libroInstance).count()
        if existe > 0:
            libro = LibroCarrito.objects.filter(carrito_id__exact=carrito).get(libro_id__exact=libroInstance)
            libro.cantidad += 1
            libro.save()
        else:
            user.carrito.libros.add(libroInstance)
        return redirect ('compras:carrito') 
    else:
        return redirect('clientes:login')

    

@login_required
def eliminarCarrito(request, titulo):
    """Se encarga de funcionalidad de eliminar al carrito."""
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    carrito = Carrito.objects.get(cliente__exact=user)
    libroEliminar = LibroCarrito.objects.filter(carrito_id__exact=carrito).filter(libro_id__exact=libroInstance)
    libroEliminar.delete()
    return redirect ('compras:carrito')


@login_required
def sumarCantidad(request,titulo):
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    carrito = Carrito.objects.get(cliente__exact=user)
    libro = LibroCarrito.objects.filter(carrito_id__exact=carrito).get(libro_id__exact=libroInstance)
    libro.cantidad += 1
    libro.save()
    return redirect ('compras:carrito')


@login_required
def restarCantidad(request,titulo):
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    carrito = Carrito.objects.get(cliente__exact=user)
    libro = LibroCarrito.objects.filter(carrito_id__exact=carrito).get(libro_id__exact=libroInstance)
    if libro.cantidad > 1:
        libro.cantidad -= 1
        libro.save()
    return redirect ('compras:carrito')


