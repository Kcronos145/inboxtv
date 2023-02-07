from django.shortcuts import render

def Blog(request):
	ctx = {
		
	}
	return render(request,'aplicaciones_page/blog/index-blog.html',ctx)

def Blog_Detail(request,id,slug):
	ctx = {
		
	}
	return render(request,'aplicaciones_page/blog/detail-blog.html',ctx)