from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post,Item

def home(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'home.html', {'posts': posts})
# Create your views here.

def blog(request):
    i=Item.objects.all()
    return(render(request,'blog.html',{'item':i}))
    #template_name = 'blog.html'

#class Home(TemplateView):
 #   template_name='home.html'


