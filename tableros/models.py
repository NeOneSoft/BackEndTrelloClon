from django.db import models

from django.contrib.auth.models import User


class Tablero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateField()
    visibilidad = models.CharField(max_length=200)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
