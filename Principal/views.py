from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView

from .forms import SearchForm
from .models import Banner
from Aplicaciones.Contenido.Peliculas.models import Peliculas,ImagesPeliculas,CommentPeliculas,CommentPeliculasForm
from Aplicaciones.Contenido.Documentales.models import Documentales
from Aplicaciones.Contenido.Series.models import Series
from Aplicaciones.Contenido.Anime.models import Anime
from Aplicaciones.Informacion.Categoria.models import Categorias
from Aplicaciones.Informacion.Actores.models import ActoresModelo
from Aplicaciones.Usuarios.Usuarios.models import UserProfile,CuponesForm,Cupones,Lista



def IndexViews(request):
	
	banner = Banner.objects.filter(status = True)
	peliculas = Peliculas.objects.filter(status = True)#.order_by('id')[:4]
	anime = Anime.objects.filter(status = True)#.order_by('id')[:4]
	categoria = Categorias.objects.filter(status = True)
	current_user = request.user
	if current_user.id:
		lista = Lista.objects.filter(user_id=current_user.id)
		numero=0
		for rs in lista:
			numero += 1 * 1
		profile = UserProfile.objects.get(user_id=current_user.id)
		ctx = {
			'peliculas':peliculas,
			'numero':numero,
			'lista':lista,
			'banner':banner,
			'categoria':categoria,
			'profile':profile,
			'anime':anime,
			
		}
	else:
		ctx = {
			'peliculas':peliculas,
			'banner':banner,
			'anime':anime,
			'categoria':categoria,
		}
	return render(request,'index.html',ctx)

def Search(request):
	current_user = request.user
	if current_user.id:
		profile = UserProfile.objects.get(user_id=current_user.id)
		banner = Banner.objects.filter(status='True')
		peliculas = Peliculas.objects.filter(status = True)
		categoria = Categorias.objects.filter(status = True)
		if request.method == 'GET':
			form = SearchForm(request.GET)
			if form.is_valid():
				query = form.cleaned_data['query']
				cantid = form.cleaned_data['cantid']
				if cantid==0:
					p = Peliculas.objects.filter(title__icontains=query) | Peliculas.objects.filter(keywords__icontains=query)
					s = Series.objects.filter(title__icontains=query) | Series.objects.filter(keywords__icontains=query)
					d = Documentales.objects.filter(title__icontains=query) | Documentales.objects.filter(keywords__icontains=query)
					a = Anime.objects.filter(title__icontains=query) | Anime.objects.filter(keywords__icontains=query)
				else:
					p = Peliculas.objects.filter(title__icontains=query,genero_id=cantid)
					s = Series.objects.filter(title__icontains=query,genero_id=cantid) | Series.objects.filter(keywords__icontains=query,genero_id=cantid)
					d = Documentales.objects.filter(title__icontains=query,genero_id=cantid) | Documentales.objects.filter(keywords__icontains=query,genero_id=cantid)
					a = Anime.objects.filter(title__icontains=query,genero_id=cantid) | Anime.objects.filter(keywords__icontains=query,genero_id=cantid)
		ctx = {
			'query':query,
			'p':p,
			's':s,
			'd':d,
			'a':a,
			'profile':profile,
			'categoria':categoria,

		}
		return render(request,'search/resultado-search.html',ctx)

def AgragraComnetarioPelicula(request,id):
	url = request.META.get('HTTP_REFERER')
	current_user = request.user
	if current_user.id:
		if request.method == 'POST':
			form = CommentPeliculasForm(request.POST)
			if form.is_valid():
				data = CommentPeliculas()
				data.subject = current_user.username
				data.email = current_user.email
				data.comment = form.cleaned_data['comment']
				data.rate = form.cleaned_data['rate']
				data.ip = request.META.get('REMOTE_ADDR')
				data.product_id=id
				current_user= request.user
				data.user_id=current_user.id
				data.save()

	else:
		if request.method == 'POST':
			form = CommentPeliculasForm(request.POST)
			if form.is_valid():
				data = CommentPeliculas()
				data.subject = form.cleaned_data['subject']
				#data.email = form.cleaned_data['correo']
				data.comment = form.cleaned_data['comment']
				data.rate = form.cleaned_data['rate']
				data.ip = request.META.get('REMOTE_ADDR')
				data.product_id=id
				data.save()
		return HttpResponseRedirect(url)
	return HttpResponseRedirect(url)

class Error404(TemplateView):
	template_name = "page-error/error-404.html"

class Error500(TemplateView):
	template_name = "page-error/error-500.html"

	@classmethod
	def as_error_view(cls):
		v = cls.as_view()
		def view(request):
			r = v(request)
			r.render()
			return r
		return view
