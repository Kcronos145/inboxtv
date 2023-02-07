from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from Aplicaciones.Informacion.Actores.models import ActoresModelo
from Aplicaciones.Informacion.Categoria.models import Categorias

class Anime(models.Model):
    STATUS = (
        ('Publicra', 'Publicra'),
        ('No Publicra', 'No Publicra'),
        ('Estreno', 'Estreno'),
        ('Clausurada', 'Clausurada'),
    )
    genero = models.ForeignKey(Categorias, on_delete=models.CASCADE,null = True,blank=True)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    lugar = models.IntegerField(default='1')
    puntuacion = models.IntegerField(default='1')
    image=models.ImageField(upload_to='Anime/',null=False)
    detail=models.TextField()
    slug = models.SlugField(null=False, unique=True)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
    	verbose_name = 'Anime'
    	verbose_name_plural = 'Animes'
    	ordering = ['lugar']


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="200"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class ImagesAnime(models.Model):
    anime=models.ForeignKey(Anime,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='Partes Anime/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
        ordering = ['id']

