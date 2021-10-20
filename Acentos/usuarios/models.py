"""Modelos de Usuarios."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
    usuario_cliente = models.BooleanField(default=False)
    usuario_admin= models.BooleanField(default=False)

    def is_client(self):
        return self.usuario_cliente
    def is_admin(self):
        return self.usuario_admin

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = "User"
