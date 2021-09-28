"""Compras modelos"""

# Django
from django.db import models

# Create your models here.
class carrito(models.Model):
    "Modelo carrito"

    precio = models.DecimalField(max_digits=7, decimal_places=3)


    
