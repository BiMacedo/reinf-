from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import usuarios
from .models import Empresa as Mod_Empresa

from .forms import login as Form_login

# Create your views here.

def inicializar(request):
    return redirect('Site:login')


def login_usuario(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        usuario = request.POST['usuario']
        senha   = request.POST['senha']

        auth_usuario = authenticate(request, username=usuario, password=senha)
        
        if auth_usuario is not None:
            login(request, auth_usuario)
            return redirect('Site:index')

        else:

            msg_erro_login = 'Usuário ou Senha inválido!'
            context = { 'erro_login':msg_erro_login }

            return render(request, 'index.html', context=context)


def index(request):
    if request.method == 'GET':
        empresas = Mod_Empresa.objects.all()
        context = { 'empresas': empresas }
        return render(request, 'index.html', context=context)
    
    elif request.method == 'POST':
        empresas = Mod_Empresa.objects.all()
        return render(request, 'index.html')


def documento(request):
    if request.method == 'GET':
        return render(request,'documento.html') 
    
    elif request.method == 'POST':
        return render(request,'documento.html') 