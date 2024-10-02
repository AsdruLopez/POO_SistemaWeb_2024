from django.shortcuts import render
#Importamos httpResponse
from django.http import HttpResponse
# Create your views here.
def hola_mundo(request):
    #devolvemos un hola mundo por atraves de un encabezado h1
    return  HttpResponse("<h1>Hola Mundo desde mi aplicacion Web</h1>")


#Crear vista principal
def inicio(request):
    return render(request,'base.html')
