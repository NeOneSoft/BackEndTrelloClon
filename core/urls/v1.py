from django.urls import path, include
from rest_framework import routers

from comentarios.views import ComentarioViewSet
from core.views import UserViewSet
from favoritos.views import FavoritoViewSet
from listas.views import ListaViewSet
from miembros.views import MiembroViewSet
from tableros.views import TableroViewSet
from tarjetas.views import TarjetaViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'tableros', TableroViewSet)
routers.register(r'favoritos', FavoritoViewSet)
routers.register(r'miembros', MiembroViewSet)
routers.register(r'listas', ListaViewSet)
routers.register(r'tarjetas', TarjetaViewSet)
routers.register(r'comentarios', ComentarioViewSet)
urlpatterns = [
    path('', include(routers.urls))
]