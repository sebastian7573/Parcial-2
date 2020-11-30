from django.urls import path, include
from . import views
from .views import buscareserva, ReservaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Reserva', ReservaViewSet )



urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('inicio', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('sesioniniciada', views.sesioniniciada, name='sesioniniciada'),
    path('registrojuegos', views.reserva, name='registrojuegos'),
    path('reservasdejuegos', views.reservasdejuegos, name='reservasdejuegos'),
    path('eliminarjuego/<nombre>/',views.eliminarjuegos, name='eliminarjuego'),
    path('modificarreserva/<nombre>/',views.modificarreserva, name='modificarreserva'),
    path('api/', include(router.urls)),
   
   
]

#127.0.0.1:8000/plantilla
#127.0.0.1:8000/p