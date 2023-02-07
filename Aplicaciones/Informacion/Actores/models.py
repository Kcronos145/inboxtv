from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

class ActoresModelo(models.Model):
	nombre = models.CharField('Nombre',max_length= 255,blank = True,null = True)
	apellido = models.CharField(max_length= 255,blank = True,null = True)
	nacionalidad = models.CharField(max_length= 255,blank = True,null = True)
	facha_nacimiento = models.CharField(max_length= 255,blank = True,null = True)
	biografia = models.TextField()
	image=models.ImageField(upload_to='Actores/',null=False)
	slug = models.SlugField(null=False, unique=True)
	status=models.BooleanField(default=True)
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.nombre + " " + self.apellido
	def name_complete(self):
		return self.nombre + " " + self.apellido
	def image_tag(self):
		if self.image.url is not None:
			return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
		else:
			return ""
