from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from Aplicaciones.Informacion.Actores.models import ActoresModelo
from Aplicaciones.Contenido.Peliculas.models import Peliculas
from Aplicaciones.Contenido.Series.models import Series
from Aplicaciones.Contenido.Documentales.models import Documentales
from Aplicaciones.Contenido.Anime.models import Anime
from Aplicaciones.Informacion.Categoria.models import Categorias

class Trailer(models.Model):
    STATUS = (
        ('Publicra', 'Publicra'),
        ('No Publicra', 'No Publicra'),
        ('Estreno', 'Estreno'),
        ('Clausurada', 'Clausurada'),
    )
    pelicula=models.ForeignKey(Peliculas,on_delete=models.CASCADE,null = True,blank=True)
    anime=models.ForeignKey(Anime,on_delete=models.CASCADE,null = True,blank=True)
    series=models.ForeignKey(Series,on_delete=models.CASCADE,null = True,blank=True)
    documentales=models.ForeignKey(Documentales,on_delete=models.CASCADE,null = True,blank=True)
    title = models.CharField(max_length=150)
    image=models.ImageField(upload_to='Trailers/',null=False)
    slug = models.SlugField(null=False, unique=True)
    status=models.BooleanField(default=True)
    pixel=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
    	verbose_name = 'Trailer'
    	verbose_name_plural = 'Trailers'
    	ordering = ['id']


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="200"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})