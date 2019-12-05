from django.contrib.auth.models import User
from django.db import models

from listas.models import Lista
from miembros.models import Miembro
from tableros.models import Tablero


class Tarjeta(models.Model):
    nombre = models.CharField(max_length=200)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    miembros = models.ManyToManyField(Tablero)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    posicion = models.IntegerField()

    def __str__(self):
        return self.nombre
