from django.contrib import admin

from .models import Trailer

class TrailerAdmin(admin.ModelAdmin):
    list_display = ['title','create_at','image_tag', 'status']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    
admin.site.register(Trailer,TrailerAdmin)
