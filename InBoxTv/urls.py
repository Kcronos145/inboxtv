from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

from Principal.views import IndexViews,Search,Error404,Error500
from Aplicaciones.Usuarios.Usuarios.views import Login_Form,Signup_Form,Logout_Form

from django.conf.urls import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),

    #Configuraciones
    #path('Ideomas/',include('Aplicaciones.Configuraciones.Ideoma.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #Contenido
    path('Peliculas/',include('Aplicaciones.Contenido.Peliculas.urls')),
    path('Anime/',include('Aplicaciones.Contenido.Anime.urls')),
    path('Documentales/',include('Aplicaciones.Contenido.Documentales.urls')),
    path('Series/',include('Aplicaciones.Contenido.Series.urls')),
    path('Trailers/',include('Aplicaciones.Contenido.Trailers.urls')),

    #Informacion
    path('Actores/',include('Aplicaciones.Informacion.Actores.urls')),
    path('Categorias/',include('Aplicaciones.Informacion.Categoria.urls')),

    #Nubes
    path('GoogleDriver/',include('Aplicaciones.Nubes.GoogleDriver.urls')),
    path('Mega/',include('Aplicaciones.Nubes.Mega.urls')),
    path('MediaLife/',include('Aplicaciones.Nubes.MediaLife.urls')),

    #Usuarios
    path('Usuarios/',include('Aplicaciones.Usuarios.Usuarios.urls')),
    path('Administradores/',include('Aplicaciones.Usuarios.Administradores.urls')),

    #Blog
    path('Blog/',include('Aplicaciones.Blog.Blog.urls')),

    #Principal
    path('Principal/',include('Principal.urls')),

    #Vistas Generalese
    path('',IndexViews,name = 'Inicio'),
    path('login/',Login_Form,name = 'Login_Form'),
    path('siginup/',Signup_Form,name = 'Signup_Form'),
    path('logout/',Logout_Form,name = 'Logout_Form'),
    path('search/',Search,name = 'Search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = Error404.as_view()
handler500 = Error500.as_error_view()
