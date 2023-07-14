from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

#def base(request):
#    return render(request, 'base.html')

#def menu(request):
#    return render(request, 'menu.html')

def create_cultura(request):
    return render(request, 'create_cultura.html')

def create_propriedade(request):
    return render(request, 'create_propriedade.html')

def create_proprietario(request):
    return render(request, 'create_proprietario.html')

def viewdados_cultura(request):
    return render(request, 'viewdados_cultura.html')

def viewdados_proprietario(request):
    return render(request, 'viewdados_proprietario.html')

def viewdados_propriedade(request):
    return render(request, 'viewdados_propriedade.html')
