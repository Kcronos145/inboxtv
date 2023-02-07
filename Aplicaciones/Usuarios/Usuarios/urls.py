from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import Update_Form,Perfil_User,Agregra_Lista,Quitar_Lista

urlpatterns = [
	path('update/',Update_Form,name='Update_Form'),
	path('perfil/',Perfil_User,name='Perfil_User'),
	path('agregar-lista/<int:id>',Agregra_Lista,name='Agregra_Lista'),
	path('quitar-lista/<int:id>',Quitar_Lista,name='Quitar_Lista'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)