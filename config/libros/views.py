from django.shortcuts import render, get_object_or_404
from .models import Libro
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from prestamos.models import Prestamo
from reseñas.models import Reseña
from prestamos.models import Prestamo
from django.db import models

def catalago(request):
    libros = Libro.objects.all()
    return render(request, 'libros/buscar.html', {'libros': libros})

def buscar_libros(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Libro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(genero__icontains=query) |
            Q(sinopsis__icontains=query)
        )
    return render(request, 'libros/buscar.html', {'libros': resultados, 'query': query})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario.html', {'form': form, 'accion': 'Agregar'})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar.html', {'libro': libro})



# def detalle_libro(request, libro_id):
#     libro = get_object_or_404(Libro, id=libro_id)
#     if libro.disponible: 
#         return render(request, 'libros/detalle_libro.html', {'libro': libro,'error': ''})
#     else:
#         return render(request, 'libros/detalle_libro.html', {'libro': libro, 'error': 'El libro no está disponible para préstamo.'})    
    

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    reseñas = Reseña.objects.filter(libro=libro)
    promedio = reseñas.aggregate(models.Avg('calificacion'))['calificacion__avg']
    return render(request, 'libros/detalle_libro.html', {
        'libro': libro,
        'reseñas': reseñas,
        'promedio': promedio
    })



@login_required
def recomendaciones_para_usuario(request):
    # Libros que el usuario ha leído (prestado)
    libros_leidos = Prestamo.objects.filter(usuario=request.user).values_list('libro_id', flat=True)

    # Obtener los autores y géneros de esos libros
    autores_leidos = Libro.objects.filter(id__in=libros_leidos).values_list('autor', flat=True)
    generos_leidos = Libro.objects.filter(id__in=libros_leidos).values_list('genero', flat=True)

    # Buscar libros que tengan el mismo autor o género, que no haya leído aún
    libros_recomendados = Libro.objects.filter(
        Q(autor__in=autores_leidos) | Q(genero__in=generos_leidos)
    ).exclude(id__in=libros_leidos).distinct()[:10]

    return render(request, 'libros/recomendaciones.html', {
        'recomendaciones': libros_recomendados
    })

