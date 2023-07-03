from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required

app_name = 'Site'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('logon', login_required(views.logon), name='logon'),
    

]
