"""Libros admin classes."""

# Django
from django.contrib import admin

# Models
from libros.models import Libro

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    """Libro admin."""

    