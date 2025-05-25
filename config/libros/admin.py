
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'fecha_publicacion')
    search_fields = ('titulo', 'autor', 'genero')
    list_filter = ('genero', 'fecha_publicacion')
    ordering = ('titulo',)
