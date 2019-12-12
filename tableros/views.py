from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from favoritos.models import Favorito
from favoritos.serializers import FavoritoSerializer
from miembros.models import Miembro
from miembros.serializers import MiembroSerializer
from tableros.models import Tablero
from tableros.serializers import TableroSerializer, CreateTableroSerializer


class TableroViewSet(viewsets.ModelViewSet):
    """
     retrieve:
        Regresa un tablero.
    list:
        Regresa la lista de tableros.
    update:
        Actualiza un tablero.
    partial_update:
        Actualiza una seccion de un tablero.
    delete:
        Elimina un tablero
    """
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTableroSerializer
        return TableroSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        if self.action == 'create':
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]
    """
    @action(detail=True, methods=['GET'])
    def favoritos(self, request, pk=None):
        tablero = self.get_object()
        favoritos = Favorito.objects.filter(favoritos=tablero.id)
        serialized = FavoritoSerializer(favoritos, many=True)
        if not favoritos:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este tablero no tiene favoritos'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def miembros(self, request, pk=None):
        tablero = self.get_object()
        miembros = Miembro.objects.filter(miembros=tablero.id)
        serialized = MiembroSerializer(miembros, many=True)
        if not miembros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este tablero no contiene miembros'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    """