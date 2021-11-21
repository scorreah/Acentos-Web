""""Modelos de Eventos"""

# Django
from django.db import models
# Models
from administradores.models import Administrador
# Create your models here.
class Evento (models.Model):
    """Modelo de Evento."""
    nombre = models.CharField(max_length=100)
    
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    descripcion = models.TextField()

    imagen = models.ImageField(
        upload_to='novedades/banners',
        
    )

    administrador_id = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    class Meta:
        db_table = "Evento"

# Create your models here.
class Descuento (models.Model):
    """Modelo de Evento."""
    
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    descripcion = models.TextField()

    imagen = models.ImageField(
        upload_to='novedades/images',
        
    )

    administrador_id = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    class Meta:
        db_table = "Descuento"
