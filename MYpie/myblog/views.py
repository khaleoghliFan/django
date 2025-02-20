from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from .models import Post,Item,Book,Author
from django.urls import reverse_lazy

class Create(CreateView):
    model=Author
    template_name = 'create.html'
    fields = ["name"]
    success_url = reverse_lazy('home')
def home(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'home.html', {'posts': posts})
# Create your views here.

def blog(request):
    i=Item.objects.all()
    return(render(request,'blog.html',{'item':i}))

def home_detail(request,pk):
    model=get_object_or_404(Post,pk=pk)
    return render(request,'extra.html',{"objects":model})
def book(request):
    book = Book.objects.all()  # Fetch all posts
    return render(request, 'book.html', {'books': book})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_detail.html', {'book': book})


