from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Cliente
from inicio.forms import FormularioCreacionCliente

def inicio(request):
    
    clientes = Cliente.objects.all()
    return render(request, 'inicio.html', {'clientes':clientes})

def crear_cliente(request):
    formulario = FormularioCreacionCliente()
    if request.method == 'POST':
        formulario = FormularioCreacionCliente(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            documento = formulario.cleaned_data.get('documento')
            localidad = formulario.cleaned_data.get('localidad')        
            cliente = Cliente(nombre=nombre, apellido=apellido, documento=documento, localidad=localidad)
            cliente.save()
            return redirect('lista')

        
    return render(request, 'crear_cliente.html',{'formulario':formulario})

def lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista.html', {'clientes':clientes})




