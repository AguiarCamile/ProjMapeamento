from django.shortcuts import render, redirect
from app.form import CulturasForm, ProprietariosForm
from app.models import Culturas, Proprietarios

def home (request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Culturas.objects.filter(Cultura__icontains=search)
    else:
        data['db'] = Culturas.objects.all()
    return render (request, 'index.html', data)

def form(request):
    data={}
    data['form'] = CulturasForm()
    return render(request, 'form.html', data)

def create(request):
    form = CulturasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Culturas.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Culturas.objects.get(pk=pk)
    data['form'] = CulturasForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Culturas.objects.get(pk=pk)
    form = CulturasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Culturas.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def home2 (request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Proprietarios.objects.filter(nomeProprietario__icontains=search)
    else:
        data['db'] = Proprietarios.objects.all()
    return render (request, 'index.html', data)

def form2 (request):
    data = {}
    data['form'] = ProprietariosForm()
    return render(request, 'form2.html', data)

def create2 (request):
    form = ProprietariosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def view2 (request, pk):
    data = {}
    data['db'] = Proprietarios.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit2 (request, pk):
    data = {}
    data['db'] = Proprietarios.objects.get(pk=pk)
    data['form'] = ProprietariosForm(instance=data['db'])
    return render(request, 'form2.html', data)

def update2 (request, pk):
    data = {}
    data['db'] = Proprietarios.objects.get(pk=pk)
    form = ProprietariosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete2 (request, pk):
    db = Proprietarios.objects.get(pk=pk)
    db.delete()
    return redirect('home')
