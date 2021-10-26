"""Libros admin classes."""

# Django
from django.contrib import admin

# Models
from libros.models import Libro, Autor
from compras.models import Resena

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    """Libro admin."""

    list_display = ('ISBN', 'titulo', 'editorial', 'categoria', 'idioma', 'presentacion', 'fecha_publicacion', 'precio')
    list_display_links = ('ISBN', 'titulo')
    list_editable = ('categoria', 'idioma', 'presentacion', 'fecha_publicacion', 'precio')

    search_fields = ('ISBN', 'titulo', 'autor__nombre')
    list_filter = ('precio', 'nuevo', 'preventa', 'puntuacion', 'fecha_publicacion')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechaNacimiento', )
    list_display_links = ('nombre',)

    search_fields = ('nombre', 'libros__titulo')
    list_filter = ('fechaNacimiento',)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    """Libro admin."""

    list_display = ('pk', 'comentario', 'puntuacion', 'fecha_hora',)
    list_display_links = ('pk',)

    search_fields = ('pk', 'comentario', 'fecha_hora',)
    list_filter = ('puntuacion', 'fecha_hora',)
