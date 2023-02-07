from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from Aplicaciones.Contenido.Peliculas.models import Peliculas
from Aplicaciones.Contenido.Series.models import Series
from Aplicaciones.Contenido.Documentales.models import Documentales
from Aplicaciones.Contenido.Anime.models import Anime
from Aplicaciones.Nubes.Cuentas.models import Cuenta

class Tipo_De_Archivo(models.Model):
    titulo = models.CharField(max_length = 255)
    slug = models.SlugField(null=False, unique=True)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo

class Archivo_En_Google_Driver(models.Model):
    tipo_de_archivo = models.ForeignKey(Tipo_De_Archivo, on_delete=models.CASCADE,null = True,blank=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE,null = True,blank=True)
    titulo=models.CharField(max_length=30,null = True,blank=True)
    pelicula=models.ForeignKey(Peliculas,on_delete=models.CASCADE,null = True,blank=True)
    anime=models.ForeignKey(Anime,on_delete=models.CASCADE,null = True,blank=True)
    series=models.ForeignKey(Series,on_delete=models.CASCADE,null = True,blank=True)
    documentales=models.ForeignKey(Documentales,on_delete=models.CASCADE,null = True,blank=True)
    image=models.ImageField(upload_to='Imagen De Pelicula/',null=False)
    status=models.BooleanField(default=True)
    pixel = models.TextField()
    url_original = models.URLField()
    url_acortada = models.URLField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
    	return self.pelicula

    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="200"/>'.format(self.image.url))
        else:
            return ""