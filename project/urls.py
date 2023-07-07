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
from django.urls import path
from app.views import home, login, form, create, view, edit, update, delete, home2, form2, create2, view2, edit2, update2, delete2, home3, form3, create3, view3, edit3, update3, delete3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('', home2, name='home'),
    path('form2/', form2, name='form2'),
    path('create2/', create2, name='create2'),
    path('view2/<int:pk>/', view2, name='view2'),
    path('edit2/<int:pk>/', edit2, name='edit2'),
    path('update2/<int:pk>/', update2, name='update2'),
    path('delete2/<int:pk>/', delete2, name='delete2'),
    path('', home3, name='home'),
    path('form3/', form3, name='form3'),
    path('create3/', create3, name='create3'),
    path('view3/<int:pk>/', view3, name='view3'),
    path('edit3/<int:pk>/', edit3, name='edit3'),
    path('update3/<int:pk>/', update3, name='update3'),
    path('delete3/<int:pk>/', delete3, name='delete3')
]
