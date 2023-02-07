import admin_thumbnails
from django.contrib import admin

from Aplicaciones.Contenido.Trailers.models import Trailer
from Aplicaciones.Nubes.GoogleDriver.models import Archivo_En_Google_Driver
from Aplicaciones.Nubes.MediaLife.models import Archivo_En_MediLife
from Aplicaciones.Nubes.Mega.models import Archivo_En_Mega
from .models import Anime,ImagesAnime

@admin_thumbnails.thumbnail('image')
class AnimeImageInline(admin.TabularInline):
    model = ImagesAnime
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class AnimeTrailersInline(admin.TabularInline):
    model = Trailer
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class AnimeGoogleDriverInline(admin.TabularInline):
    model = Archivo_En_Google_Driver
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class AnimeMediaLifeInline(admin.TabularInline):
    model = Archivo_En_MediLife
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class AnimeMegaInline(admin.TabularInline):
    model = Archivo_En_Mega
    readonly_fields = ('id',)
    extra = 1

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title','genero','lugar','puntuacion','create_at','image_tag', 'status']#detail
    list_filter = ['genero']
    inlines = [AnimeImageInline,AnimeTrailersInline,AnimeGoogleDriverInline,AnimeMediaLifeInline,AnimeMegaInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title','genero',)}
    prepopulated_fields = {'keywords': ('title','genero','lugar','puntuacion',)}
    
admin.site.register(Anime,AnimeAdmin)