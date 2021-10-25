"""Libros admin classes."""

# Django
from django.contrib import admin

# Models
from libros.models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    """Libro admin."""

    list_display = ('ISBN', 'titulo', 'editorial', 'categoria', 'idioma', 'presentacion', 'fecha_publicacion', 'precio')
    list_display_links = ('ISBN', 'titulo')
    list_editable = ('categoria', 'idioma', 'presentacion', 'fecha_publicacion', 'precio')

    search_fields = ('ISBN', 'titulo', 'autor__nombre')
    list_filter = ('precio', 'nuevo', 'preventa', 'puntuacion', 'fecha_publicacion')

    readonly_fields = ('ISBN',)