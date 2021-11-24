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
@login_required
def carrito(request):
    """Se encarga de los detalles del carrito."""
    userInstance = request.user
    user = Cliente.objects.get(user__exact=userInstance)
    libros = user.carrito.libros.all()
    cantidadLibros = libros.count()
    libros_carrito = LibroCarrito.objects.filter()
    
    precioTotal = 0
    for i in libros:
        precioTotal = i.precio
    precioEnvio = precioTotal + 8500 + 5000

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
        cliente = Cliente.objects.get(user = request.user)
        tel = request.POST.get('Teléfono de contacto')
        mde = request.POST.get('MDE')
        mdp = ""
        if request.POST.get('MDPCT'):
            mdp = "Tarjeta de credito"
        elif request.POST.get('MDPCE'):
            mdp = "Contra-Entrega"
        elif request.POST.get('MDPCD'):
            mdp = "Tarjeta de debito"
        elif request.POST.get('MDPCP'):
            mdp = "Paypal"
        costo = 100000
        
        val = request.POST.get('MDE')
        if val == "RT":
            metodoEnvio = "Recoger en tienda"
        elif val == "EO":
            metodoEnvio = "Envio"
        print(metodoEnvio)
        print(mdp)
        compra = {
            'metodo_pago': mdp,
            'metodo_envio': metodoEnvio,
            'costo_total': costo,
            'fecha_compra': datetime.date.today,
            'cliente': cliente,
        }
        purchase = Compra.objects.create(**compra)
        purchase.save()
    return render(request=request,template_name='compras/compra.html')
    
@login_required
def anadirCarrito(request, titulo):
    """Se encarga de funcionalidad de anadir al carrito."""
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    user.carrito.libros.add(libroInstance)

    return redirect ('novedades:home')

@login_required
def eliminarCarrito(request, titulo):
    """Se encarga de funcionalidad de eliminar al carrito."""
    libroInstance = Libro.objects.get(titulo__exact=titulo)
    userInstance = request.user 
    user = Cliente.objects.get(user__exact=userInstance)
    libroEliminar = user.carrito.librocarrito_set.first()
    libroEliminar.delete()
    return redirect ('compras:carrito')


