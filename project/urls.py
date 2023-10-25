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
from app.views import login1, process_login, logouts, home, index_cultura, index_proprietario, index_propriedade
from app.views import create_cultura, create_proprietario, create_propriedade
from app.views import viewdados_cultura, viewdados_proprietario, viewdados_propriedade
from app.views import update_cultura, delete_cultura
from app.views import update_proprietario, delete_proprietario
from app.views import update_propriedade, delete_propriedade
from rest_framework import routers
from app.viewsets import CulturasViewSet, ProprietariosViewSet, PropriedadesViewSet

router = routers.DefaultRouter()
router.register(r'cultura', CulturasViewSet, basename="Culturas")
router.register(r'proprietario', ProprietariosViewSet, basename="Proprietarios")
router.register(r'propriedade', PropriedadesViewSet, basename="Propriedades")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', login1, name='login'),
    path('home/', home, name='home'),
    path('login/', login1, name='login'),
    path('process_login/', process_login),
    path('logouts/', logouts, name='logouts'),
    path('create_cultura/', create_cultura, name='create_cultura'),
    path('create_proprietario/', create_proprietario, name='create_proprietario'),
    path('create_propriedade/', create_propriedade, name='create_propriedade'),
    path('viewdados_cultura/<int:pk>/', viewdados_cultura, name='viewdados_cultura'),
    path('viewdados_proprietario/<int:pk>/', viewdados_proprietario, name='viewdados_proprietario'),
    path('viewdados_propriedade/<int:pk>/', viewdados_propriedade, name='viewdados_propriedade'),
    path('index_cultura/', index_cultura, name='index_cultura'),
    path('index_proprietario/', index_proprietario, name='index_proprietario'),
    path('index_propriedade/', index_propriedade, name='index_propriedade'),
    path('update_cultura/<int:pk>/', update_cultura, name='update_cultura'),
    path('update_proprietario/<int:pk>/', update_proprietario, name='update_proprietario'),
    path('update_propriedade/<int:pk>/', update_propriedade, name='update_propriedade'),
    path('delete_cultura/<int:pk>/', delete_cultura, name='delete_cultura'),
    path('delete_proprietario/<int:pk>/', delete_proprietario, name='delete_proprietario'),
    path('delete_propriedade/<int:pk>/', delete_propriedade, name='delete_propriedade'),
    path("api/", include(router.urls))


]


