"""Administrador admin classes."""

# Django
from django.contrib import admin

# Models
from administradores.models import Administrador

# Register your models here.
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    """Administrador admin."""

    list_display = ('pk', 'user', 'telefono',)    
    list_display_links = ('pk', 'user',) 
    list_editable = ('telefono',) 
    search_fields = (
        'pk',
        'user__email', 
        'user__username',
        'user__first_name', 
        'user__last_name', 
    )
    list_filter = (
        'user__created', 
    )