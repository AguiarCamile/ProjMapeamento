from django.shortcuts import render, redirect, get_object_or_404
from app.form import CulturasForm, ProprietariosForm, PropriedadesForm
from app.models import Culturas, Proprietarios, Propriedades
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login1(request):
    return render(request, 'login.html')

def process_login (request):
    data = {}
    user = authenticate(username=request.POST['nome'], password=request.POST['senha'])
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        data['msg'] = 'Usuário ou senha inválidos'
        data['class'] = 'alert alert-danger'

        return render(request, 'login.html', data)

def logouts(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def create_cultura(request):
    if request.method == 'POST':
        form = CulturasForm(request.POST, request.FILES)
        if form.is_valid():
            cultura = form.save(commit=False)
            cultura.save()
            return redirect('index_cultura')
    else:
        form = CulturasForm()
    return render(request, 'create_cultura.html', {'form': form})

def index_cultura(request):
    search = request.GET.get('search')
    if search:
        cultura = Culturas.objects.filter(TipoCultura__icontains=search)
    else:
        cultura = Culturas.objects.all()
    return render(request, 'index_cultura.html', {'cultura': cultura})

def viewdados_cultura(request, pk):
    cultura = get_object_or_404(Culturas, pk=pk)
    return render(request, 'viewdados_cultura.html', {'cultura': cultura})

def update_cultura(request, pk):
    cultura = get_object_or_404(Culturas, pk=pk)
    if request.method == 'POST':
        form = CulturasForm(request.POST, request.FILES, instance=cultura)
        if form.is_valid():
            form.save()
            return redirect('index_cultura')
    else:
        form = CulturasForm(instance=cultura)
    return render(request, 'create_cultura.html', {'form': form, 'db': cultura})

def delete_cultura(request, pk):
    cultura = get_object_or_404(Culturas, pk=pk)
    cultura.delete()
    return redirect('index_cultura')

def create_proprietario(request):
    if request.method == 'POST':
        form = ProprietariosForm(request.POST, request.FILES)
        if form.is_valid():
            proprietario = form.save(commit=False)
            proprietario.save()
            return redirect('index_proprietario')
    else:
        form = ProprietariosForm()
    return render(request, 'create_proprietario.html', {'form': form})

def index_proprietario(request):
    search = request.GET.get('search')
    if search:
        proprietario = Proprietarios.objects.filter(nomeProprietarios__icontains=search)
    else:
        proprietario = Proprietarios.objects.all()
    return render(request, 'index_proprietario.html', {'proprietario': proprietario})

def viewdados_proprietario(request, pk):
    proprietario = get_object_or_404(Proprietarios, pk=pk)
    return render(request, 'viewdados_proprietario.html', {'proprietario': proprietario})

def update_proprietario(request, pk):
    proprietario = get_object_or_404(Proprietarios, pk=pk)
    if request.method == 'POST':
        form = ProprietariosForm(request.POST or None, instance=proprietario)
        if form.is_valid():
            form.save()
            return redirect('index_proprietario')
    else:
        form = ProprietariosForm(instance=proprietario)
    return render(request, 'create_proprietario.html', {'form': form, 'db': proprietario})

def delete_proprietario(request, pk):
    proprietario = get_object_or_404(Proprietarios, pk=pk)
    proprietario.delete()
    return redirect('index_proprietario')


def create_propriedade(request):
    if request.method == 'POST':
        form = PropriedadesForm(request.POST, request.FILES)
        if form.is_valid():
            propriedade = form.save(commit=False)
            propriedade.save()
            return redirect('index_propriedade')
    else:
        form = PropriedadesForm()

    return render(request, 'create_propriedade.html', {'form': form})

def index_propriedade(request):
    search = request.GET.get('search')
    if search:
        propriedade = Propriedades.objects.filter(app__icontains=search)
    else:
        propriedade = Propriedades.objects.all()
    return render(request, 'index_propriedade.html', {'propriedade': propriedade})

def viewdados_propriedade(request, pk):
    propriedade = get_object_or_404(Propriedades, pk=pk)
    return render(request, 'viewdados_propriedade.html', {'propriedade': propriedade})

def update_propriedade(request, pk):
    propriedade = get_object_or_404(Propriedades, pk=pk)
    if request.method == 'POST':
        form = PropriedadesForm(request.POST or None, instance=propriedade)
        if form.is_valid():
            form.save()
            return redirect('index_propriedade')
    else:
        form = PropriedadesForm(instance=propriedade)
    return render(request, 'create_propriedade.html', {'form': form, 'db': propriedade})

def delete_propriedade(request, pk):
    propriedade = get_object_or_404(Propriedades, pk=pk)
    propriedade.delete()
    return redirect('index_propriedade')
