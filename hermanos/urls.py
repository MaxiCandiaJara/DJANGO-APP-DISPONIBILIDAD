"""
URL configuration for hermanos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('agregarHermano', views.agregarHermano, name="AgHer"),
    path('listarHermanos', views.listarHermanos, name="listar"),
    path('buscar', views.buscar, name="buscar"),
    path('editar', views.editar, name="editar"),
    path('editarHermano', views.editarHermano, name="editando"),
    path('mensajes', views.mensajes, name="Mensajes"),
    path('elegirMes', views.elegirMes, name="elegirMes"),
    path('github', views.github, name="github" ),
    path('subir', views.subir, name="subir"),
    path('cargar', views.cargar, name="cargar" ),
    path('agregar', views.agregar, name="agregar"),
    path('wsp', views.wspMensaje,name="wsp")
]
