"""Compras views."""
# Django
from django.shortcuts import render

# Create your views here.
def carrito(request):
    """Se encarga de los detalles del carrito."""
    return render(request=request, template_name='compras/carrito.html')

def compra(request):
    """Se encarga de confirmar la compra y seleccionar los métodos de envio y pago"""
    metodoEnvio = ""
    if request.method == 'POST':
        val = request.POST.get('searchType')
        if val == "CE":
            metodoEnvio = "CE"
        elif val == "EO":
            metodoEnvio = "EO"
        
    return render(request=request,
                  template_name='compras/compra.html',
                  context={'metodoEnvio':metodoEnvio})

