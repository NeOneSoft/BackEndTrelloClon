from rest_framework import serializers

from miembros.models import Miembro


class MiembroSerializer(serializers.ModelSerializer):
    """
      General purpose
      """
    class Meta:
        model = Miembro
        fields = ('tablero', 'miembros', )


class CreateMiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ('tablero', 'miembros', )