from django.contrib import admin
from .models import Portada, Devocional, Lider, Mensaje

# Register your models here.

admin.site.register(Portada)
admin.site.register(Devocional)
admin.site.register(Lider)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'motivo', 'fecha', 'leido')
    list_filter = ('leido', 'fecha')
    readonly_fields = ('nombre', 'email', 'telefono', 'motivo', 'cuerpo', 'fecha')