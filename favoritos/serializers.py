from rest_framework import serializers

from .models import Favorito


class FavoritoSerializer(serializers.ModelSerializer):
    """
    General purpose
    """

    class Meta:
        model = Favorito
        fields = ('favoritos', 'usuario',)


class CreateFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ('favoritos', 'usuario',)
