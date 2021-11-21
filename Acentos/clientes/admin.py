"""Clientes admin classes."""

# Django
from django.contrib import admin

# Models
from clientes.models import Cliente
from clientes.models import Carrito, LibroCarrito

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Cliente admin."""

    list_display = ('pk', 'user', 'direccion', 'telefono')    
    list_display_links = ('pk', 'user') 
    list_editable = ('direccion', 'telefono') 
    search_fields = (
        'pk',
        'user__email', 
        'user__username',
        'user__first_name', 
        'user__last_name', 
    )
    list_filter = (
        'user__usuario_cliente', 
        'user__usuario_admin',
    )
#     fieldsets = (
#         ('Perfil', {
#             'fields': (('ni','user',),)
#         }),
#         ('Información personal', {
#             'fields': (
#                 ('direccion', 'telefono',),
#                 ('carrito', 'libros'))
#         }),
#         ('Metadata', {
#             'fields': (('fecha_registro'),)
#         }),
#     )

admin.site.register(Carrito)

admin.site.register(LibroCarrito)
