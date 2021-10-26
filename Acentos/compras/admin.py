"""Compras admin classes."""

# Django
from django.contrib import admin

# Models
from compras.models import Carrito, LibroCarrito, Compra

admin.site.register(Carrito)

admin.site.register(LibroCarrito)

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