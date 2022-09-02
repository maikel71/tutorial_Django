"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_productos.views import *

urlpatterns = [
    #================ URLS CON VISTAS BASADAS EN FUNCIONES=============#
    path('admin/', admin.site.urls),
    path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inico"),
    path('logout/', logout_view, name="vista_logout"),

    #================ URLS CON VISTAS BASADAS EN CLASES=============#

    path('lista_proveedor/', login_required(ListadoProveedor.as_view()),
         name="listar_proveedor"),
    path('crear_proveedor/', login_required(CrearProveedor.as_view()),
         name="crear_proveedor")
]

admin.site.site_header = 'SISTEMA DE GESTION DE PRODUCTOS'
