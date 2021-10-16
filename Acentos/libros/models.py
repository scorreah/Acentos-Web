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
    titulo = models.CharField(max_length=100, blank=True)
    editorial = models.CharField(max_length=50, blank=True)
    
    categoria = models.CharField(max_length=50, blank=True)
    puntuacion = models.FloatField(null=True, blank=True)
    edicion = models.CharField(max_length=20, null=True)
    idioma = models.CharField(max_length=20, blank=True)
    noPaginas = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    nuevo = models.BooleanField(default=False)
    preventa = models.BooleanField(default=False)
    portada = models.ImageField(
        upload_to='libros/pictures',
        
    )

    class Presentacion(models.TextChoices):
        TDURA = 'TD', _('Tapa dura')
        TBLANDA = 'TB', _('Tapa blanda')
        NONE = 'NN', _('None')

    presentacion = models.CharField(
        max_length=2,
        choices=Presentacion.choices,
        default=Presentacion.NONE
    )

    url_libro = models.CharField(max_length=80, blank=True)

    fecha_publicacion = models.DateField()

    class Meta:
        db_table = "Libro"

class Autor(models.Model):
    nombre = models.CharField(max_length=80, null=False)
    biografia = models.TextField(null=True, blank=True)
    fechaNacimiento = models.DateField()

    libros = models.ManyToManyField(Libro)
    class Meta:
        db_table = "Autor"

class Resena(models.Model):
    comentario = models.CharField(max_length=280, null=True, blank=True)
    puntuacion = models.FloatField(null=True, blank=True)

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "Resena"