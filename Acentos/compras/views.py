"""Compras views."""
# Django
from django.shortcuts import render

# Create your views here.
def carrito(request):
    """Se encarga de los detalles del carrito."""
    return render(request = request, template_name='compras/carrito.html')