"""Compras modelos"""

# Django
from django.db import models
#from django.contrib.auth.models import User

# Models
from libros.models import Libro
from usuarios.models import User

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


class Cliente (models.Model):
    """Modelo de cliente."""

    user = models.OneToOneField(User, models.CASCADE)

    ni = models.CharField(max_length=13, unique=True, primary_key=True)

    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    carrito = models.OneToOneField(Carrito, models.CASCADE)
    reseñas = models.ManyToManyField(Libro, through="Resena")


    class Meta:
        db_table = "Cliente"

class Compra(models.Model):
    metodo_pago = models.CharField(max_length=25)
    metodo_envio = models.CharField(max_length=25)

    costo_total = models.BigIntegerField()
    
    fecha_compra = models.DateTimeField(auto_now_add=True)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "Compra"

class Resena(models.Model):
    comentario = models.CharField(max_length=280, null=True, blank=True)
    puntuacion = models.FloatField(null=True, blank=True)

    fecha_hora = models.DateTimeField(auto_now_add=True)

    libro_id = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta:
        db_table = "Resena"