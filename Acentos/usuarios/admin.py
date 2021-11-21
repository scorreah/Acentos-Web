"""User admin classes."""

# Django
from django.contrib import admin

# Models
from usuarios.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email','usuario_cliente', 'usuario_admin', 'created', 'modified',)  
    list_display_links = ('pk', 'username')                                     
    list_editable = ('usuario_cliente', 'usuario_admin')
    
    readonly_fields = ('created', 'modified',)