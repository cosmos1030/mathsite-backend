
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create.html/', views.create, name='create'),
    path('read.html/', views.read, name='read'),
]