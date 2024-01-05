"""
URL configuration for Web1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Web1.views import inicio, contacto_view, simulador_view, simulador1_view
from gestionPedidos import views ## Otra manera de importar



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', inicio),
    path('formulario/', views.busqueda_productos), ## Otra manera de importar 
    path('buscar/', views.buscar),
    path('contactanos/', contacto_view, name='contactanos'),
    path('simulador/', simulador_view, name='simulador'),
    path('simulador1/', simulador1_view, name='simulador1'),
]