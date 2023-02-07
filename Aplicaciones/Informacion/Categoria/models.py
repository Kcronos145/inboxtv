from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

class Categorias(models.Model):
	STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
	title = models.CharField(max_length=150)
	keywords = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	image=models.ImageField(upload_to='Categorias/',null=False)
	slug = models.SlugField(null=False, unique=True)
	status=models.BooleanField(default=True)
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
	def image_tag(self):
		if self.image.url is not None:
			return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
		else:
			return ""
