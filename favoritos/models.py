from django.contrib.auth.models import User
from django.db import models

from tableros.models import Tablero


class Favorito(models.Model):

    favoritos = models.ManyToManyField(Tablero)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.favoritos
