from django.urls import path
from . import views




urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('inicio', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('sesioniniciada', views.sesioniniciada, name='sesioniniciada'),
    path('registrojuegos', views.reserva, name='registrojuegos')
    
   
   
]

#127.0.0.1:8000/plantilla
#127.0.0.1:8000/p