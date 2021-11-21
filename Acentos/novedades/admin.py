"""Novedades admin classes."""

# Django
from django.contrib import admin

# Models
from novedades.models import Evento, Descuento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """Evento admin."""
    list_display = ('pk', 'nombre', 'administrador_id','fecha_inicio', 'fecha_fin', 'descripcion', 'imagen',)    
    list_display_links = ('pk', 'nombre', 'administrador_id') 
    list_editable = ('fecha_inicio', 'fecha_fin', 'descripcion') 
    search_fields = (
        'pk', 
        'nombre',
    )
    list_filter = (
        'fecha_inicio', 
        'fecha_fin',
    )

    readonly_fields = ('pk',)

@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    """Evento admin."""
    list_display = ('pk', 'evento', 'porcentaje', 'condiciones',)    
    list_display_links = ('pk', 'evento',) 
    list_editable = ('porcentaje', 'condiciones',) 
    search_fields = (
        'porcentaje',
    )
    list_filter = (
        'porcentaje',
        'evento',
    )

    readonly_fields = ('pk', 'evento',)