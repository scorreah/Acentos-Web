"""Novedaes views"""

#Django
from django.shortcuts import render
from django.urls import conf
import libros
from libros.models import Libro
from novedades.models import Evento

# Create your views here.
def error_404(request,exception):
    """Muestra la vista por defecto del error 404 o cuando se accede a una página que no está disponible en el dominio web."""
    return render(request=request,template_name='404.html')

def home(request,*args, **kwargs):
    """Muestra la vista para que se logee el cliente"""
    global nuevos, prev
    nuevos = Libro.objects.filter(nuevo=True)
    prev = Libro.objects.filter(preventa=True)
    carousel = Evento.objects.all()
    return render(request=request,
                  template_name='novedades/home.html',
                  context = {
                  'nuevos': nuevos,
                  'preventa': prev,
                  'carousel':carousel
                  })
