from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.conf import settings
#PAL LOGIN
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
#PAL CRUUUUU
from gestorDeJuegos.models import Reserva


# Create your views here.
def reserva(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        categoria = request.POST["categoria"]
        plataforma = request.POST["plataforma"]
        imagen = request.POST["imagen"]
        Reserva.objects.create(nombre=nombre,categoria=categoria,plataforma=plataforma,imagen=imagen)
    return render(request,'registrojuegos.html',{} )

def listarjuegos(request):
    juegos = Reserva.objects.all()

    return render(request, 'registrojuegos.html',{})

def index(request):
    

    return render(request,'index.html', )
     
   
def sesioniniciada(request):
    # Si estamos identificados devolvemos la portada
   # if request.user.is_authenticated:
       return render(request,'sesioniniciada.html',{})
     # En otro caso redireccionamos al login
   # return redirect('/inicio')


def inicio(request):
     # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            nombreuser = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Verificamos las credenciales del usuario
            user = authenticate(username=nombreuser, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/index')

    # Si llegamos al final renderizamos el formulario
    return render(request,'inicio.html',{'form': form})



def registro(request):
    if request.method == "POST":
        nombre = request.POST["nombreuser"]
        correo = request.POST["correo"]
        clave =  request.POST["password"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))
        return redirect(settings.LOGIN_REDIRECT_URL1, request.path)
    return render(request,'registro.html',{})
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

    
