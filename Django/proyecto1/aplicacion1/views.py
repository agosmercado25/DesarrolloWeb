from django.shortcuts import render
from django.http import HttpResponse
from aplicacion1.models import Webs, Temas
from . import forms

# Create your views here.
def vista1(request):
    return HttpResponse("Hola, buenos días")

def vista2(request):
    return HttpResponse("Adios, hasta la proxima")
"""
def vista3(request):
    diccionario = {'etiqueta':'Este es el valor de la etiqueta'}
    return render(request,"pagina1.html",context=diccionario)
"""
def vista3(request):
    diccionario = {'etiqueta':'Este es el NUEVO VALOR de la etiqueta'}
    return render(request,"aplicacion1/pagina1.html",context=diccionario)

def vista4(request):
    diccionario = {}
    return render(request,"aplicacion1/pagina3.html",context=diccionario)

def vista6(request):
    lista_temas = Temas.objects.all()
    lista_webs = Webs.objects.order_by('nombre')
    diccionario = {'lista_webs':lista_webs,'lista_temas':lista_temas}
    return render(request,"aplicacion1/portada.html",context=diccionario)

def vista7(request):
    formulario = forms.Formulario()
    diccionario = {'formulario':formulario}

    if request.method == 'POST':
        formulario1 = forms.Formulario(request.POST)
        if formulario1.is_valid():
            nombre = formulario1.cleaned_data['nombre']
            correo = formulario1.cleaned_data['email']
            print("Nombre: " + nombre)
            print("Correo electrónico: " + correo)

    return render(request,"aplicacion1/formulario.html",context=diccionario)

def pagina4(request):
    #diccionario = {'texto':'Holas, buenos días', 'numero':300, 'hora':'16:30:00'}
    diccionario = {'texto':'Hola, buenos días', 'numero':300}
    return render(request, "aplicacion1/pagina4.html", context=diccionario)

def pagina5(request):
    diccionario = {}
    return render(request, "aplicacion1/pagina5.html", context=diccionario)

def plantilla(request):
    diccionario = {}
    return render(request, "aplicacion1/plantilla.html",context=diccionario)

def ejercicio1(request):
    diccionario = {'etiqueta':'Este es el NUEVO VALOR de la etiqueta'}
    return render(request, "aplicacion1/ejercicio1.html", context=diccionario)
