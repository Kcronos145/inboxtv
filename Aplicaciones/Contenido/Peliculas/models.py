from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.db.models import Avg, Count

from Aplicaciones.Informacion.Actores.models import ActoresModelo
from Aplicaciones.Informacion.Categoria.models import Categorias

class Peliculas(models.Model):
    STATUS = (
        ('Se Estrenara En', 'Se Estrenara En'),
        ('Proximamante', 'Proximamante'),
        ('Retrasada', 'Retrasada'),
        ('Retrasada 30dias', 'Retrasada 30dias'),
        ('Estreno', 'Estreno'),
        ('Publicada', 'Publicada'), 
        ('Clausurada', 'Clausurada'),
    )
    genero = models.ForeignKey(Categorias, on_delete=models.CASCADE,null = False,blank=False) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    actores = models.ManyToManyField(ActoresModelo)
    lugar = models.IntegerField(default='1')
    puntuacion = models.IntegerField(default='1')
    image=models.ImageField(upload_to='Peliculas/',null=False)
    detail=models.TextField()
    pixel=RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.BooleanField(default=True)
    status_subida=models.CharField(default='Proximamante',choices=STATUS,max_length=20)
    frecha_estreno=models.DateTimeField(auto_now_add=False,blank=True,null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
    	verbose_name = 'Pelicula'
    	verbose_name_plural = 'Peliculas'
    	ordering = ['lugar']


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="200"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
        
    def avaregereview(self):
        reviews = CommentPeliculas.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
            return avg

    def countreview(self):
        reviews = CommentPeliculas.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class ImagesPeliculas(models.Model):
    pelicula=models.ForeignKey(Peliculas,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='Partes Peliculas/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
        ordering = ['id']

class CommentPeliculas(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Peliculas,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True,blank=True)
    subject = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=255, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='True')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentPeliculasForm(ModelForm):
    class Meta:
        model = CommentPeliculas
        fields = ['subject', 'comment', 'rate']