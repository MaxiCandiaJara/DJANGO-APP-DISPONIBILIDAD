from django.contrib import admin
from .models import Hermano


@admin.register(Hermano)
class HermanoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'comentario')
    search_fields = ('nombre',)
