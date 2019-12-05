from django.contrib.auth.models import User
from django.db import models

from tarjetas.models import Tarjeta


class Comentario(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=1000)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField()

    def __int__(self):
        return self.tarjeta
