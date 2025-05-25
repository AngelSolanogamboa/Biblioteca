from django.urls import path
from . import views



urlpatterns = [
    path('libro/<int:libro_id>/reseñar/', views.agregar_reseña, name='agregar_reseña'),
]