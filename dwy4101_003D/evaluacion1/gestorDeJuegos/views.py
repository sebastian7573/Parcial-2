from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html',{})
def inicio(request):
    return render(request,'inicio.html',{})
def registro(request):
    return render(request,'registro.html',{})

