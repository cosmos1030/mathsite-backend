from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def create(request):
    return render(request, 'homepage/create.html')

def read(request):
    posts = Post.objects.filter()
    return render(request, 'homepage/read.html', {'posts': posts})