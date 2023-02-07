import admin_thumbnails
from django.contrib import admin

from Aplicaciones.Contenido.Trailers.models import Trailer
from Aplicaciones.Nubes.GoogleDriver.models import Archivo_En_Google_Driver
from Aplicaciones.Nubes.MediaLife.models import Archivo_En_MediLife
from Aplicaciones.Nubes.Mega.models import Archivo_En_Mega
from .models import Peliculas,ImagesPeliculas,CommentPeliculas

@admin_thumbnails.thumbnail('image')
class PeliculasImageInline(admin.TabularInline):
    model = ImagesPeliculas
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class PeliculasTrailersInline(admin.TabularInline):
    model = Trailer
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class PeliculasGoogleDriverInline(admin.TabularInline):
    model = Archivo_En_Google_Driver
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class PeliculasMediaLifeInline(admin.TabularInline):
    model = Archivo_En_MediLife
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class PeliculasMegaInline(admin.TabularInline):
    model = Archivo_En_Mega
    readonly_fields = ('id',)
    extra = 1

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ['title','genero','lugar','puntuacion','status_subida','image_tag', 'status']#detail
    list_filter = ['genero']
    inlines = [PeliculasImageInline,PeliculasTrailersInline,PeliculasGoogleDriverInline,PeliculasMediaLifeInline,PeliculasMegaInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}
    
class CommentPeliculasAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at','user']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','product','rate','id')
    
admin.site.register(Peliculas,PeliculasAdmin)
admin.site.register(CommentPeliculas,CommentPeliculasAdmin)
