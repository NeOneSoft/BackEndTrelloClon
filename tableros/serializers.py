from rest_framework import serializers
from core.serializers import UserSerializer
from .models import Tablero


class TableroSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    dueño = UserSerializer(read_only=True)
    favoritos = UserSerializer(many=True, read_only=True)
    miembros = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Tablero
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'dueño', 'favoritos', 'miembros')


class CreateTableroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tablero
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'dueño', 'favoritos', 'miembros')
