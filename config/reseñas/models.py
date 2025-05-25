from django.db import models
from accounts.models import User
from libros.models import Libro
# reseñas/models.py
from django.apps import apps

# reseñas/models.py




class Reseña(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reseñas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo}"




# class Reseña(models.Model):
#     # libro = models.ForeignKey('Libro', on_delete=models.CASCADE, related_name='resenas')
#     Libro = apps.get_model('libros', 'Libro')
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     calificacion = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#     comentario = models.TextField()
#     fecha = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('libro', 'usuario')  # Un usuario solo puede reseñar un libro una vez

#     def __str__(self):
#         return f'{self.usuario.username} - {self.libro.titulo} ({self.calificacion})'