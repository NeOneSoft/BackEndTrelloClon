from rest_framework import serializers

from .models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    """
    General Purpose
    """
    class Meta:
        model = Comentario
        fields = ('tarjeta', 'mensaje', 'dueño', 'fecha_creacion', )

class CreateComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('tarjeta', 'mensaje', 'dueño', 'fecha_creacion', )