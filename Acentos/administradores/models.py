"""Administradores models."""

# Django
from django.db import models
from django.apps import apps

# Models
#from usuarios.models import User

# Create your models here.
class Administrador (models.Model):
    """Modelo de admin."""
    
    user = models.OneToOneField('usuarios.User', models.CASCADE)

    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        texto = "{0} (pk: {1})"
        return texto.format(self.user.username, self.pk)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        db_table = "Administrador"
