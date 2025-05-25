from django.db import models


class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    sinopsis = models.TextField()
    disponible = models.BooleanField(default=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
    
    

