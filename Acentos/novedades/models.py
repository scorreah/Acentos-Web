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

    def __str__(self):
        texto = "Evento ({0} - {1})"
        return texto.format(self.nombre, self.fecha_inicio)

    class Meta:
        db_table = "Evento"


class Descuento (models.Model):
    """Modelo de Descuento."""
    
    porcentaje = models.FloatField()

    condiciones = models.TextField()

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        texto = "Descuento {1} ({0})"
        return texto.format(self.evento, self.porcentaje)

    class Meta:
        db_table = "Descuento"
