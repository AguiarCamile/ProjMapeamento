"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import home, index, login, create_cultura, create_proprietario, create_propriedade
from app.views import viewdados_cultura, viewdados_proprietario, viewdados_propriedade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('app.urls')),
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('create_cultura/', create_cultura, name='create_cultura'),
    path('create_proprietario/', create_proprietario, name='create_proprietario'),
    path('create_propriedade/', create_propriedade, name='create_propriedade'),
    path('viewdados_cultura/', viewdados_cultura, name='viewdados_cultura'),
    path('viewdados_proprietario/', viewdados_proprietario, name='viewdados_proprietario'),
    path('viewdados_propriedade/', viewdados_propriedade, name='viewdados_propriedade'),

]


