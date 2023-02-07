from django.contrib import admin

from .models import Archivo_En_Google_Driver,Tipo_De_Archivo

class Tipo_De_ArchivoAdmin(admin.ModelAdmin):
    list_display = ['titulo','slug','create_at','status']
    list_filter = ['titulo']

class Archivo_En_Google_DriverAdmin(admin.ModelAdmin):
    list_display = ['tipo_de_archivo','cuenta','pelicula','image_tag', 'status']
    list_filter = ['tipo_de_archivo']
    readonly_fields = ('image_tag',)


admin.site.register(Tipo_De_Archivo,Tipo_De_ArchivoAdmin)
admin.site.register(Archivo_En_Google_Driver,Archivo_En_Google_DriverAdmin)
