from django.contrib import admin
from .models import Cuenta,TipoCuenta

class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ['titulo','create_at', 'status']
    list_filter = ['titulo']

class CuentaAdmin(admin.ModelAdmin):
    list_display = ['cuenta','correo','contraseña','image_tag', 'status']
    list_filter = ['cuenta']
    readonly_fields = ('image_tag',)

admin.site.register(TipoCuenta,TipoCuentaAdmin)
admin.site.register(Cuenta,CuentaAdmin)
