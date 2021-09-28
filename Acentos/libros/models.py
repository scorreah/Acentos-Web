"""Libros models."""

# Django
from django.db import models

# Create your models here.
class Libro(models.Model):
    """Modelo libro."""

    ISBN = models.CharField(max_length=13)
    sinopsis = models.TextField(blank=True)
    