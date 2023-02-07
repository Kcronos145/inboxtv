from django.contrib import admin
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['sub_titulo','titulo','create_at','image_tag', 'status']
    list_filter = ['titulo']
    readonly_fields = ('image_tag',)

admin.site.register(Banner,BannerAdmin)
