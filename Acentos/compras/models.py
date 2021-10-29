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

    def __str__(self):
        texto = "Carrito ({0})"
        return texto.format(self.pk)

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

    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)

    carrito = models.OneToOneField(Carrito, models.CASCADE)
    reseñas = models.ManyToManyField(Libro, through="Resena")

    def __str__(self):
        texto = "{0} (NI: {1})"
        return texto.format(self.user.username, self.pk)

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
    
    def __str__(self):
        texto = "Comment on '{1}' (By {0} on {2})"
        return texto.format(self.cliente_id.user.username, self.libro_id.titulo, self.fecha_hora)

    class Meta:
        db_table = "Resena"