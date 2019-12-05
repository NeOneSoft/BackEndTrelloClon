from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from listas.models import Lista
from listas.serializers import ListaSerializer, CreateListaSerializer


class ListaViewSet(viewsets.ModelViewSet):
    """
         retrieve:
            Regresa una lista
        list:
            Regresa la lista de tableros
        update:
            Actualiza una lista
        partial_update:
            Actualiza una seccion de listas
        delete:
            Elimina un tablero
    """

    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateListaSerializer
        return ListaSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]
