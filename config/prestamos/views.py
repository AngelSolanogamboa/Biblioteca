# views.py
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import PrestamoForm
from .models import Prestamo
from libros.models import Libro
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

@login_required
def registrar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.usuario = request.user
            prestamo.save()
            libro = prestamo.libro
            libro.disponible = False
            libro.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'prestamos/registrar.html', {'form': form})

@login_required
def registrar_prestamo_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if libro.disponible:
        prestamo = Prestamo.objects.create(
            usuario=request.user,
            libro=libro,
            fecha_vencimiento=date.today() + timedelta(days=7)
        )
        prestamo.save()
        libro = prestamo.libro
        libro.disponible = False
        libro.leido = True
        libro.save()
        return redirect('lista_prestamos')
    else:
        return render(request, 'libros/detalle_libro.html', {'libro': libro, 'error': 'El libro no está disponible para préstamo.'})    


@login_required
def lista_prestamos(request):
    prestamos = Prestamo.objects.filter(usuario=request.user)
    return render(request, 'prestamos/lista.html', {'prestamos': prestamos})

def DBlista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/listaDB.html', {'prestamos': prestamos})

def marcar_como_devuelto(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    prestamo.devuelto = True
    prestamo.save()
    prestamo.libro.disponible = True  # opcional: marcar libro disponible de nuevo
    prestamo.libro.save()
    return redirect('DBlista_prestamos')