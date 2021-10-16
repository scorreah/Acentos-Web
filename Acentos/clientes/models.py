
# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from compras.models import Carrito
from libros.models import Libro

# Create your models here.
class Cliente (models.Model):
    """Modelo de cliente."""

    user = models.OneToOneField(User, models.CASCADE)

    ni = models.CharField(max_length=13, unique=True)

    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    carrito = models.OneToOneField(Carrito, models.CASCADE)
    clientes = models.ManyToManyField(Libro)

    class Meta:
        db_table = "Cliente"
