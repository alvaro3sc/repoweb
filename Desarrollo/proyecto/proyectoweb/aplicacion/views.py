from django.shortcuts import render
def noticia_list(request):
    return render (request, 'aplicacion/post_list.html',{})
# Create your views here.
