from django.urls import path
from . import views
from django.shortcuts import render
from .models import Libro


# Vista sencilla para el home
def home_view(request):

    libros = Libro.objects.all()
    return render(request, 'base.html', {'mensaje': 'Bienvenido a la Biblioteca','libros': libros})

urlpatterns = [
    path('', home_view, name='home'),
    path('Catalago/', views.catalago, name='catalago'),
    path('buscar/', views.buscar_libros, name='buscar_libros'),
    path('DBLibros/', views.lista_libros, name='lista_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('editar/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('recomendaciones/', views.recomendaciones_para_usuario, name='recomendaciones'),
    
    
]