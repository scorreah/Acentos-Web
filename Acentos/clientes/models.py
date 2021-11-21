"""Clientes models"""

# Django
from django.db import models

# Models
from libros.models import Libro
from usuarios.models import User

# Utils
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Carrito(models.Model):
    """Modelo Carrito."""

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

    historial = models.CharField(max_length=500, blank=True, default="")

    carrito = models.OneToOneField(Carrito, models.CASCADE)
    reseñas = models.ManyToManyField(Libro, through="Resena")

    reservas = models.ManyToManyField('administradores.Administrador', through="Reserva")

    def __str__(self):
        texto = "{0} (NI: {1})"
        return texto.format(self.user.username, self.pk)

    class Meta:
        db_table = "Cliente"

class Resena(models.Model):
    """Modelo de Resena."""
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

class Reserva (models.Model):
    """Modelo de Reserva."""
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    administrador_id = models.ForeignKey('administradores.Administrador', on_delete=models.CASCADE, null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Estado(models.TextChoices):
        NEW = 'NW', _('Nuevo')
        OKAY = 'OK', _('Aceptado')
        DENIED = 'DN', _('Rechazado')
        ONGOING = 'OG', _('En Proceso')
        DELIVERED = 'DL', _('Entregado')

    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.NEW
    )

    autor = models.CharField(max_length=80, null=True)
    ISBN = models.CharField(max_length=13)
    titulo = models.CharField(max_length=100)

    def __str__(self):
        texto = "Reserva on '{1}' (By {0} on {2})"
        return texto.format(self.cliente_id.user.username, self.titulo, self.fecha_creacion)

    class Meta:
        db_table = "Reserva"