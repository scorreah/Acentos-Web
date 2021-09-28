"""Libros models."""

# Django
from django.db import models

# Utils
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Libro(models.Model):
    """Modelo libro."""

    ISBN = models.CharField(max_length=13, primary_key=True)
    sinopsis = models.TextField(blank=True)
    titulo = models.CharField(max_length=100)
    editorial = models.CharField(max_length=50)
    
    categoria = models.CharField(max_length=50)
    puntuacion = models.FloatField()
    edicion = models.CharField(max_length=20, null=True)
    idioma = models.CharField(max_length=20)
    noPaginas = models.IntegerField()
    nuevo = models.BooleanField()
    preventa = models.BooleanField()
    portada = models.ImageField(
        upload_to='libros/pictures',
        blank=True,
        null=True
    )

    class Presentacion(models.TextChoices):
        RDURA = 'TD', _('Tapa dura')
        TBLANDA = 'TB', _('Tapa blanda')

    presentacion = models.CharField(
        max_length=2,
        choices=Presentacion.choices
    )
