""""Modelos de Eventos"""

# Django
from django.db import models

# Models
#from usuarios.models import User

# Create your models here.
class Evento(models.Model):
    """Modelo de evento."""
    id = models.AutoField(primary_key=True)
    #admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) quien sabe
    fechaInicio = models.DateTimeField()
    descripcion = models.TextField()
    fechaFin = models.DateTimeField()
    portada = models.ImageField(
        upload_to='libros/pictures', #Cambiar esto por una carpeta que se llame eventos/pictures
    )
    class Meta:
        db_table = "Evento"