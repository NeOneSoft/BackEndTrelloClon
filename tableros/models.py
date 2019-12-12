from django.db import models
from django.contrib.auth.models import User

VISIBILIDAD = (
    ('V', 'Visible'),
    ('N', 'No Visible'),
)


class Tablero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateField()
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='dueño')
    favoritos = models.ManyToManyField(User, related_name='favoritos')
    visibilidad = models.CharField(max_length=1, choices=VISIBILIDAD)
    miembros = models.ManyToManyField(User, related_name='miembros')

    def __str__(self):
        return self.nombre
