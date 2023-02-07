import admin_thumbnails
from django.contrib import admin

from Aplicaciones.Contenido.Trailers.models import Trailer
from Aplicaciones.Nubes.GoogleDriver.models import Archivo_En_Google_Driver
from Aplicaciones.Nubes.MediaLife.models import Archivo_En_MediLife
from Aplicaciones.Nubes.Mega.models import Archivo_En_Mega
from .models import Series,ImagesSeries,Temporadas

@admin_thumbnails.thumbnail('image')
class SeriesImageInline(admin.TabularInline):
    model = ImagesSeries
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class SeriesTrailersInline(admin.TabularInline):
    model = Trailer
    readonly_fields = ('id',)
    extra = 1
    
class SeriesTemporadaInline(admin.TabularInline):
    model = Temporadas
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class SeriesGoogleDriverInline(admin.TabularInline):
    model = Archivo_En_Google_Driver
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class SeriesMediaLifeInline(admin.TabularInline):
    model = Archivo_En_MediLife
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class SeriesMegaInline(admin.TabularInline):
    model = Archivo_En_Mega
    readonly_fields = ('id',)
    extra = 1

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title','genero','lugar','puntuacion','create_at','image_tag', 'status']#detail
    list_filter = ['genero']
    inlines = [SeriesImageInline,SeriesTrailersInline,SeriesGoogleDriverInline,SeriesMediaLifeInline,SeriesMegaInline,SeriesTemporadaInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}
    prepopulated_fields = {'keywords': ('title','genero','lugar','puntuacion','actores',)}
    
admin.site.register(Series,SeriesAdmin)