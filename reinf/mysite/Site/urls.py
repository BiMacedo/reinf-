from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Site'

urlpatterns = [
    path( '', views.inicializar, name='inicializar' ),
    path( 'login/', views.login_usuario, name='login' ),
    path( 'index/', login_required(views.index), name='index' ),
    path('documento/', login_required(views.documento), name='documento'),
    path('profile/', login_required(views.profile), name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)