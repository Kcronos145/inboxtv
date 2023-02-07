from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from Aplicaciones.Contenido.Peliculas.models import Peliculas

class Banner(models.Model):
    STATUS = (
        ('Publicra', 'Publicra'),
        ('No Publicra', 'No Publicra'),
        ('Estreno', 'Estreno'),
        ('Clausurada', 'Clausurada'),
    )
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE,null=False,blank = False)
    sub_titulo = models.CharField(max_length=25)
    titulo = models.CharField(max_length=10,null = True,blank=True)
    image=models.ImageField(upload_to='Banner/',null=False)
    slug = models.SlugField(null=False, unique=True)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pelicula.title

    class Meta:
    	verbose_name = 'Banner'
    	verbose_name_plural = 'Banners'
    	ordering = ['titulo']


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="200"/>'.format(self.image.url))
        else:
            return ""
