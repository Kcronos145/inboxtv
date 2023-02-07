from django.contrib import admin

from .models import Categorias

class CategoriasAdmin(admin.ModelAdmin):
	list_display = ['title','keywords','description','create_at','image_tag', 'status']
	list_filter = ['title']
	readonly_fields = ('image_tag',)
	prepopulated_fields = {'slug': ('title',)}
	prepopulated_fields = {'keywords': ('title','keywords','description','create_at',)}

admin.site.register(Categorias,CategoriasAdmin)