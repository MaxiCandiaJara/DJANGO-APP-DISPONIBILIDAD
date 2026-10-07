"""
URL configuration for hermanos project.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Admin de Django
    path('admin/', admin.site.urls),

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Páginas principales
    path('', views.index, name="index"),
    path('agregarHermano', views.agregarHermano, name="AgHer"),
    path('listarHermanos', views.listarHermanos, name="listar"),
    path('buscar', views.buscar, name="buscar"),
    path('editar', views.editar, name="editar"),
    path('editarHermano', views.editarHermano, name="editando"),
    path('eliminarHermano', views.eliminarHermano, name="eliminar"),
    path('mensajes', views.mensajes, name="Mensajes"),
    path('elegirMes', views.elegirMes, name="elegirMes"),
    path('agregar', views.agregar, name="agregar"),
    path('wsp', views.wspMensaje, name="wsp"),

    # Hoja de cálculo y datos
    path('disponibilidad', views.hojaCalculo, name="disponibilidad"),
    path('importar', views.importarJSON, name="importar"),

    # ===== ADMINISTRAR INFO =====
    path('admin-info', views.adminInfo, name="adminInfo"),
    path('exportar/hermanos', views.exportarHermanos, name="exportarHermanos"),
    path('exportar/casas', views.exportarCasas, name="exportarCasas"),
    path('importar/casas', views.importarCasas, name="importarCasas"),


    # ===== CASAS =====
    path('casas/agregar', views.agregarCasa, name="agregarCasa"),
    path('casas/agregarPost', views.agregarCasaPost, name="agregarCasaPost"),
    path('casas/listar', views.listarCasas, name="listarCasas"),
    path('casas/buscar', views.buscarCasa, name="buscarCasa"),
    path('casas/editar', views.editarCasaSearch, name="editarCasaSearch"),
    path('casas/editarPost', views.editarCasaPost, name="editarCasaPost"),
    path('casas/eliminar', views.eliminarCasa, name="eliminarCasa"),
    path('casas/disponibilidad', views.disponibilidadCasas, name="disponibilidadCasas"),
    path('casas/elegirMes', views.elegirMesCasas, name="elegirMesCasas"),
    path('casas/mensajes', views.mensajesCasas, name="mensajesCasas"),
]
