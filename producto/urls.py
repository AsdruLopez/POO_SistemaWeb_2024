#estas son las urls a utilizar para mi aplicacion de productos

from django.urls import path
from producto import views

urlpatterns = [
   path('Holamundo', views.hola_mundo),
   path('', views.inicio) 
]