from django.db import models

from tableros.models import Tablero


class Lista(models.Model):
    nombre = models.CharField(max_length=200)
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    posicion = models.IntegerField()

    def __str__(self):
        self.models.nombre
