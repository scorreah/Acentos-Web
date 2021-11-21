"""Compras admin classes."""

# Django
from django.contrib import admin

# Models
from compras.models import Compra, Devolucion


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    """Compra admin."""

    list_display = ('pk', 'metodo_pago', 'metodo_envio', 'costo_total', 'fecha_compra')    
    list_display_links = ('pk',) 
    list_editable = ('metodo_pago', 'metodo_envio') 
    search_fields = (
        'pk', 
        'fecha_compra',
    )
    list_filter = (
        'fecha_compra',
    )

    readonly_fields = ('pk',)

@admin.register(Devolucion)
class DevolucionAdmin(admin.ModelAdmin):
    """Devolucion admin."""

    list_display = ('pk', 'compra_id', 'administrador_id', 'fecha_redaccion', 'fecha_respuesta', 'respondido', 'motivo', 'respuesta',)    
    list_display_links = ('pk', 'compra_id', 'administrador_id',) 
    list_editable = ('fecha_respuesta', 'respondido', 'respuesta',) 
    search_fields = (
        'pk', 
        'fecha_redaccion',
    )
    list_filter = (
        'fecha_redaccion',
        'respondido',
    )

    readonly_fields = ('pk',)