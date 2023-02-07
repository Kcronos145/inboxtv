import admin_thumbnails
from django.contrib import admin

from Aplicaciones.Contenido.Trailers.models import Trailer
from Aplicaciones.Nubes.GoogleDriver.models import Archivo_En_Google_Driver
from Aplicaciones.Nubes.MediaLife.models import Archivo_En_MediLife
from Aplicaciones.Nubes.Mega.models import Archivo_En_Mega
from .models import Documentales,ImagesDocumentales

@admin_thumbnails.thumbnail('image')
class DocumentalesImageInline(admin.TabularInline):
    model = ImagesDocumentales
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class DocumentalesTrailersInline(admin.TabularInline):
    model = Trailer
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class DocumentalesGoogleDriverInline(admin.TabularInline):
    model = Archivo_En_Google_Driver
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class DocumentalesMediaLifeInline(admin.TabularInline):
    model = Archivo_En_MediLife
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class DocumentalesMegaInline(admin.TabularInline):
    model = Archivo_En_Mega
    readonly_fields = ('id',)
    extra = 1

class DocumentalesAdmin(admin.ModelAdmin):
    list_display = ['title','genero','lugar','puntuacion','create_at','image_tag', 'status']#detail
    list_filter = ['genero']
    inlines = [DocumentalesImageInline,DocumentalesTrailersInline,DocumentalesGoogleDriverInline,DocumentalesMediaLifeInline,DocumentalesMegaInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title','genero','lugar','puntuacion','create_at','actores',)}
    prepopulated_fields = {'keywords': ('title','genero','lugar','puntuacion','actores',)}
    
admin.site.register(Documentales,DocumentalesAdmin)