from . import views
from django.contrib import admin
from django.urls import include, path

app_name = 'polls'
urlpatterns = [
 
    path('', views.index, name='index'),
]
