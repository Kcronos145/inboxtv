from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import DetallePeliculaViews,Peliculas_Page

urlpatterns = [
	path('pelicula-detail/<int:id>/<slug:slug>',DetallePeliculaViews,name='DetallePeliculaViews'),
	path('pelicula-page/',Peliculas_Page,name='Peliculas_Page'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)