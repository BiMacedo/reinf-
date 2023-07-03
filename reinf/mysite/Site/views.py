from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import usuario as Mod_usuario

from .forms import login as Form_login

# Create your views here.

def user_login(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'index.html')
    
    elif request.method == 'POST':
        usuario = request.POST['usuario']
        senha   = request.POST['senha']

        auth_usuario = authenticate(request, username=usuario, password=senha)
        
        if auth_usuario is not None:
            login(request, auth_usuario)
            return redirect('logon.html')

        else:

            msg_erro_login = 'Usuário ou Senha inválido!'
            context = { 'erro_login':msg_erro_login }

            return render(request, 'index.html', context=context)


def logon(request):
    if request.method == 'GET':
        return render(request, 'logon.html')
    
    elif request.method == 'POST':
        return redirect(request, 'logon.html')