from django.contrib import admin

# Register your models here.
from .models import UserProfile,Cupones,Lista

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','credito','phone','city','country','image_tag']

class CuponesAdmin(admin.ModelAdmin):
    list_display = ['user','codigo','status','create_at']

class ListaAdmin(admin.ModelAdmin):
    list_display = ['user','pelicula','status','create_at']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Cupones,CuponesAdmin)
admin.site.register(Lista,ListaAdmin)