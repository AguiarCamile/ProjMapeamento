from django.shortcuts import render, redirect
from app.form import EstadosForm
from app.models import Estados

def home (request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Estados.objects.filter(Estado__icontains=search)
    else:
        data['db'] = Estados.objects.all()
    return render (request, 'index.html', data)

def form(request):
    data={}
    data['form'] = EstadosForm()
    return render(request, 'form.html', data)

def create(request):
    form = EstadosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Estados.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Estados.objects.get(pk=pk)
    data['form'] = EstadosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Estados.objects.get(pk=pk)
    form = EstadosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Estados.objects.get(pk=pk)
    db.delete()
    return redirect('home')
