from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login1, name='login1'),
    #path('index', views.index, name='index'),
    #path('login', views.login, name='login'),
    #path('create_cultura', views.create_cultura, name='create_cultura'),
    #path('create_proprietario', views.create_proprietario, name='create_proprietario'),
    #path('create_propriedade', views.create_propriedade, name='create_propriedade'),
]