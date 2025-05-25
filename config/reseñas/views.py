
from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Reseña
from .forms import ReseñaForm
from django.contrib.auth.decorators import login_required

@login_required
def agregar_reseña(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    reseña_existente = Reseña.objects.filter(libro=libro, usuario=request.user).first()

    if request.method == 'POST':
        form = ReseñaForm(request.POST, instance=reseña_existente)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.libro = libro
            reseña.usuario = request.user
            reseña.save()
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = ReseñaForm(instance=reseña_existente)

    return render(request, 'reseñas/agregar_reseña.html', {'form': form, 'libro': libro})
