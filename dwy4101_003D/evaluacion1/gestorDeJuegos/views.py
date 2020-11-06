from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html',{})
def inicio(request):
    return render(request,'inicio.html',{})
def registro(request):
    if request.method == "POST":
        nombre = request.POST["nombreuser"]
        correo = request.POST["correo"]
        clave =  request.POST["password"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))
        return redirect(settings.LOGIN_REDIRECT_URL, request.path)
    return render(request,'registro.html',{})

