from rest_framework import serializers

from .models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    class Meta:
        model = Tarjeta
        fields = ('nombre', 'lista', 'descripcion', 'miembros', 'dueño', 'fecha_creacion', 'fecha_vencimiento', 'posicion', )


class CreateTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('nombre', 'lista', 'descripcion', 'miembros', 'dueño', 'fecha_creacion', 'fecha_vencimiento', 'posicion', )