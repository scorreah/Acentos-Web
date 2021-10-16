"""Compras modelos"""

# Django
from django.db import models

# Models
from libros.models import Libro
from clientes.models import Cliente

# Create your models here.
class Carrito(models.Model):
    "Modelo Carrito"

    precio = models.IntegerField() 
    libros = models.ManyToManyField(Libro, through="LibroCarrito")

    class Meta:
        db_table = "Carrito"

class LibroCarrito(models.Model):
    carrito_id = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    libro_id = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    class Meta:
        db_table = "LibroCarrito"

class Compra(models.Model):
    metodo_pago = models.CharField(max_length=25)
    metodo_envio = models.CharField(max_length=25)

    costo_total = models.BigIntegerField()
    
    fecha_compra = models.DateTimeField(auto_now_add=True)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "Compra"

