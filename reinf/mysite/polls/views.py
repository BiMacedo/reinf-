from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def login(request):
    
      if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                 login(request, user)
            
           
            return render(request, 'index.html')
        #return render(request,'index.html')
    
def dashboard(request):
      return render(request,'dashboard.html' )
    