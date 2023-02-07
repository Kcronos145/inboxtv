from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from Aplicaciones.Contenido.Peliculas.models import Peliculas
# Create your models here.
from django.utils.safestring import mark_safe

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='Pefil/')
    credito = models.IntegerField(default = 20)
    codigo = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Cupones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=15,null=True,blank=True)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username


class CuponesForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['credito']

class Lista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.pelicula