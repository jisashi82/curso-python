from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def index(request):
    #return HttpResponse('Hola Mundo con Django')
    post =Post.objects.all()
    return render(request, 'index.html', {'posts':post})


def post(request, id):
    post= Post.objects.get(id=id)
    print(post)
    return render(request, 'post.html',{'post':post})