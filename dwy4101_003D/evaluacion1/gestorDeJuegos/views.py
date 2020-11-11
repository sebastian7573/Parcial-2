from django.shortcuts import render, redirect, get_object_or_404
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
from django.db.models import Q
#PA LOS MENSAJES    
from django.contrib import messages



# Create your views here.

#CREAR UNA RESERVA
def reserva(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        categoria = request.POST["categoria"]
        plataforma = request.POST["plataforma"]
        imagen = request.POST["imagen"]
        Reserva.objects.create(nombre=nombre,categoria=categoria,plataforma=plataforma,imagen=imagen)
    return render(request,'registrojuegos.html',{} )




#MOSTRAR RESERVA DE JUEGOS
def reservasdejuegos(request):
    juegos = Reserva.objects.all()

    return render(request, 'reserva.html',{"juegos":juegos})

#MODIFICAR RESERVA
def modificarreserva(request, nombre):
    juegos = get_object_or_404(Reserva, nombre=nombre)

    variables = {

         Reserva(instance=juegos)
    }



    return render(request,'modificarreserva.html',variables)



def buscareserva(request):
    busqueda = request.POST.get("buscar")
    juegos = Reserva.objects.all()
    if busqueda:
        juegos = Reserva.objects.filter(
            Q(nombre__icontains = busqueda) | 
            Q(categoria__icontains = busqueda) |
            Q(plataforma__icontains = busqueda) 
          #  Q(correo_electronico__icontains = busqueda)
        ).distinct()
         
    return render(request, 'reserva.html', {'juegos':juegos})
#BUSCAR POR NOMBRE 



#ELIMINAR RESERVA DE JUEGOS
def eliminarjuegos(request, nombre):
    #Buscar el juego que vamos a eliminar
    juego = Reserva.objects.get(nombre=nombre)

    try:
        juego.delete()
        mensaje = "Su reserva ha sido eliminada con exito "
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar su reserva de juego, vuelva a intentarlo"
        messages.error(request, mensaje)
#IMPLEMENTAR
    return redirect('/reservasdejuegos')



     
    

#PAGINA INDEX
def index(request):
    return render(request,'index.html', )
     
#LOGIN  
def sesioniniciada(request):
    # Si estamos identificados devolvemos la portada
   # if request.user.is_authenticated:
       return render(request,'sesioniniciada.html',{})
     # En otro caso redireccionamos al login
   # return redirect('/inicio')


#PAGINA DE INICIO
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


#REGISTRO DE USUARIOS
def registro(request):
    if request.method == "POST":
        nombre = request.POST["nombreuser"]
        correo = request.POST["correo"]
        clave =  request.POST["password"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))
        return redirect(settings.LOGIN_REDIRECT_URL1, request.path)
    return render(request,'registro.html',{})


#CERRAR SESIÓN
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

    
