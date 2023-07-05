from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Site'

urlpatterns = [
    path('',views.user_login,name='login'),
   # path('logon/',views.logon,name='logon'),
    path('/logon', login_required(views.logon), name='logon'),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)