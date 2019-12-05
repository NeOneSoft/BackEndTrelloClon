from rest_framework import viewsets

from miembros.models import Miembro
from miembros.serializers import MiembroSerializer, CreateMiembroSerializer


class MiembroViewSet(viewsets.ModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMiembroSerializer
        return MiembroSerializer
