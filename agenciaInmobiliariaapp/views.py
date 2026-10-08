from django.shortcuts import render, redirect
from .models import Arriendo
from .forms import FormCrear, FormEditar

def crear_arriendo(request):
    if request.method == 'POST':
        form = FormCrear(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_arriendos')  # Usa 'listar_arriendos' igual que en urls.py
    else:
        form = FormCrear()
    return render(request, 'crear_arriendo.html', {'form': form})

def editar_arriendo(request, id):
    arriendo = Arriendo.objects.get(id=id)

    if request.method == 'POST':
        form = FormEditar(request.POST, instance=arriendo)
        if form.is_valid():
            form.save()
            return redirect('listar_arriendos')  # Usa 'listar_arriendos' igual que en urls.py
    else:
        form = FormEditar(instance=arriendo)
    return render(request, 'editar_arriendo.html', {'form': form})

def listar_arriendos(request):
    todos_los_arriendos = Arriendo.objects.all()
    # Enviamos 'arriendos' (en plural) al HTML
    return render(request, 'listar_arriendo.html', {'arriendos': todos_los_arriendos})

def eliminar_arriendo(request, id):
    # Recupera el objeto exacto desde MySQL
    arriendo_obj = Arriendo.objects.get(id=id)

    if request.method == 'POST':
        arriendo_obj.delete()
        return redirect('listar_arriendos')

    # Fíjate en la clave del diccionario: 'arriendo'
    return render(request, 'eliminar_arriendo.html', {'arriendo': arriendo_obj})