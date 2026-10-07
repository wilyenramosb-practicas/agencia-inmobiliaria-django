from django.shortcuts import render, redirect
from .models import Arriendo
from .forms import FormCrear, FormEditar
# Creamos las vistas (las vistas vienen siendo el intermediario).

def crear_arriendo(request):
    if request.method == 'POST': #si el cliente envia datos
        form = FormCrear(request.POST)
        if form.is_valid(): #valida de que cada uno de los campos corresponde y los valida
            form.save() #guarda el registro en la base de datos
            return redirect('lista_arriendos') #redirige al listado
    else:
        form = FormCrear()
    return render(request, 'crear_arriendo.html', {'form': form})

def editar_arriendo(request,id):
    arriendo = Arriendo.objects.get(id=id) #obtenemos el id del arriendo a editar

    if request.method == 'POST':
        form = FormEditar(request.POST, instance=arriendo) # enviamos lo datos modificamos en el mismo objeto
        if form.is_valid():
            form.save()
            return redirect('lista_arriendos')
    else:
        form = FormEditar(instance=arriendo)
    return render(request, 'editar_arriendo.html', {'form': form})

def listar_arriendo(request):
    lista_arriendos = Arriendo.objects.all()
    return render(request, 'listar_arriendo.html', {'arriendos':lista_arriendos})