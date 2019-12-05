from rest_framework import serializers

from .models import Tablero


class TableroSerializer(serializers.ModelSerializer):
    """
    General purpose
    """

    class Meta:
        model = Tablero
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'visibilidad', 'dueño', )


class CreateTableroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tablero
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'visibilidad', 'dueño', )
