from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def create(request):
    return render(request, 'homepage/create.html')

def read(request):
    return render(request, 'homepage/read.html')