from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import AgragraComnetarioPelicula

urlpatterns = [
	path('addcomment/<int:id>',AgragraComnetarioPelicula),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)