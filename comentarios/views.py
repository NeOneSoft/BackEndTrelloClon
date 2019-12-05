from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer, CreateComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    """
           retrieve:
              Regresa un comentario
          list:
              Regresa la lista de comentarios.
          update:
              Actualiza un coemntario.
          delete:
              Elimina un coemnatrio.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateComentarioSerializer
        return ComentarioSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        if self.action == 'create':
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]