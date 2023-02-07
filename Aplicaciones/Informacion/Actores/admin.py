from django.contrib import admin

from .models import ActoresModelo

class ActoresModeloAdmin(admin.ModelAdmin):
	list_display = ['nombre','apellido','nacionalidad','facha_nacimiento','create_at','image_tag', 'status']
	list_filter = ['nombre']
	readonly_fields = ('image_tag',)
	prepopulated_fields = {'slug': ('nombre','apellido','facha_nacimiento',)}

admin.site.register(ActoresModelo,ActoresModeloAdmin)