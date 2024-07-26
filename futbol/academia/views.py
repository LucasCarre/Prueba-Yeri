from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido a la página de inicio")

def categorias(request):
    return HttpResponse("Vista categorias")

def alumnos(request):
    return HttpResponse("Vista alumnos")

def profesores(request):
    return HttpResponse("Vista profesores")