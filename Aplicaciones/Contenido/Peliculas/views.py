from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .models import Peliculas,ImagesPeliculas,CommentPeliculas,CommentPeliculasForm
from Aplicaciones.Contenido.Documentales.models import Documentales
from Aplicaciones.Contenido.Series.models import Series
from Aplicaciones.Contenido.Anime.models import Anime
from Aplicaciones.Informacion.Categoria.models import Categorias
from Aplicaciones.Informacion.Actores.models import ActoresModelo
from Aplicaciones.Usuarios.Usuarios.models import UserProfile,CuponesForm,Cupones,Lista


def DetallePeliculaViews(request,id,slug):

	pelicula = Peliculas.objects.get(id = id,slug = slug)
	images = ImagesPeliculas.objects.filter(pelicula_id = id)
	peliculas = Peliculas.objects.filter(status = True)
	categoria = Categorias.objects.filter(status = True)
	comentarios = CommentPeliculas.objects.filter(product_id = id)
	current_user = request.user
	if current_user.id:
		lista = Lista.objects.filter(user_id=current_user.id)
		numero=0
		for rs in lista:
			numero += 1 * 1
		profile = UserProfile.objects.get(user_id=current_user.id)
		ctx = {
			'pelicula':pelicula,
			'comentarios':comentarios,
			'images':images,
			'peliculas':peliculas,
			'categoria':categoria,
			'profile':profile,
			'numero':numero,
			'lista':lista,
		}
	else:
		ctx = {
			'comentarios':comentarios,
			'images':images,
			'pelicula':pelicula,
			'peliculas':peliculas,
			'categoria':categoria,
		}
	return render(request,'detalles/detalle-pelicula.html',ctx)

def Peliculas_Page(request):
	current_user = request.user
	peliculas = Peliculas.objects.filter(status = True)
	cate = Categorias.objects.filter(status = True)
	categoria = Categorias.objects.filter(status = True)
	var=0
	for rs in peliculas:
		var += 1 * 1
	if current_user.id:
		lista = Lista.objects.filter(user_id=current_user.id)
		numero=0
		for rs in lista:
			numero += 1 * 1
		profile = UserProfile.objects.get(user_id=current_user.id)
		ctx = {
			'peliculas':peliculas,
			'categoria':categoria,
			'cate':cate,
			'var':var,
			'profile':profile,
			'numero':numero,
			'lista':lista,
		}
	else:
		ctx = {
			'peliculas':peliculas,
			'cate':cate,
			'var':var,
		}
	return render(request,'aplicaciones_page/contenido/peliculas/index-peliculas.html',ctx)