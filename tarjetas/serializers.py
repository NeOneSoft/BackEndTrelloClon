from rest_framework import serializers

from core.serializers import UserSerializer
from .models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):
    """
    General purpose
    """

    Dueño = UserSerializer(read_only=True)
    Miembros = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Tarjeta
        fields = ('nombre', 'lista', 'descripcion', 'Miembros', 'Dueño', 'fecha_creacion', 'fecha_vencimiento', 'posicion', )


class CreateTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('nombre', 'lista', 'descripcion', 'Miembros', 'Dueño', 'fecha_creacion', 'fecha_vencimiento', 'posicion', )