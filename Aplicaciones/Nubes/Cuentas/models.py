from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from Aplicaciones.Usuarios.Usuarios.models import UserProfile

class TipoCuenta(models.Model):
    titulo = models.CharField(max_length = 255)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo

class Cuenta(models.Model):
    tipo_de_cuenta = models.ForeignKey(TipoCuenta,on_delete=models.CASCADE,null=True,blank=True)
    cuenta = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null = True,blank=True)
    correo = models.CharField(max_length = 255)
    contraseña = models.CharField(max_length = 255)
    status=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
    	return self.correo

    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="200"/>'.format(self.image.url))
        else:
            return ""