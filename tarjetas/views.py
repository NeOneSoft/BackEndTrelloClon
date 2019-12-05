from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from tarjetas.models import Tarjeta
from tarjetas.serializers import TarjetaSerializer, CreateTarjetaSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
    """
        retrieve:
           Regresa una tarjeta.
       list:
           Regresa la lista de tarjetas.
       update:
           Actualiza una tarjeta.
       delete:
           Elimina una tarjeta
       """
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTarjetaSerializer
        return TarjetaSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        if self.action == 'create':
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]
