from rest_framework import serializers

from .models import Lista


class ListaSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    class Meta:
        model = Lista
        fields = ('nombre', 'tablero', 'fecha_creacion', 'posicion', )


class CreateListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ('nombre', 'tablero', 'fecha_creacion', 'posicion', )


