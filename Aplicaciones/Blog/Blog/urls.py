from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import Blog,Blog_Detail
urlpatterns = [
	path('',Blog,name='Blog'),
	path('Blog_Detail/<int:id>/<slug:slug>',Blog_Detail,name='Blog_Detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)