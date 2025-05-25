# models.py
from django.db import models
from accounts.models import User
from libros.models import Libro
from datetime import timedelta, date


class Prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    devuelto = models.BooleanField(default=False)

    def esta_vencido(self):
        return date.today() > self.fecha_vencimiento and not self.devuelto

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.usuario.username}"

