from django.contrib import admin
from .models import Archivo_En_Mega

class Archivo_En_MegaAdmin(admin.ModelAdmin):
    list_display = ['tipo_de_archivo','cuenta','pelicula','image_tag', 'status']
    list_filter = ['tipo_de_archivo']
    readonly_fields = ('image_tag',)


admin.site.register(Archivo_En_Mega,Archivo_En_MegaAdmin)