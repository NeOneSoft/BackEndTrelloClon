from rest_framework import viewsets

from favoritos.models import Favorito
from favoritos.serializers import FavoritoSerializer, CreateFavoritoSerializer


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializers_class = FavoritoSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateFavoritoSerializer
        return FavoritoSerializer
