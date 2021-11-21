"""Compras models"""

# Django
from django.db import models

# Models

# Create your models here.

class Compra(models.Model):
    metodo_pago = models.CharField(max_length=25)
    metodo_envio = models.CharField(max_length=25)

    costo_total = models.BigIntegerField()
    
    fecha_compra = models.DateTimeField(auto_now_add=True)

    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "Compra"

class Devolucion (models.Model):
    """Modelo de Devolucion."""
    compra_id = models.OneToOneField(Compra, on_delete=models.CASCADE)
    administrador_id = models.ForeignKey('administradores.Administrador', on_delete=models.CASCADE)
    
    fecha_redaccion = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)

    respondido = models.BooleanField(default=False)

    motivo = models.TextField()
    respuesta = models.TextField()

    class Meta:
        db_table = "Devolucion"
