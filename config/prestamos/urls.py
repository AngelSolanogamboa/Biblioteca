# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/registrar/', views.registrar_prestamo, name='registrar_prestamo'),
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('DBprestamos/', views.DBlista_prestamos, name='DBlista_prestamos'),
    path('prestamos/<int:prestamo_id>/devolver/', views.marcar_como_devuelto, name='marcar_devuelto'),
    path('prestamos/registrar/<int:libro_id>/', views.registrar_prestamo_libro, name='registrar_prestamo_libro'),
]
