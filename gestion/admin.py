from django.contrib import admin
from .models import Hermano, Casa


@admin.register(Hermano)
class HermanoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'comentario')
    search_fields = ('nombre',)


@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'numero', 'comentario')
    search_fields = ('nombre', 'direccion')
