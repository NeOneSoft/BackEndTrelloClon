from django.contrib.auth.models import User
from django.db import models

from tableros.models import Tablero


class Miembro(models.Model):
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User)

    def __int__(self):
        return self.miembros
