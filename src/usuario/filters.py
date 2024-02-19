from django_filters import FilterSet
from usuario.models import *


class PermisoFilter(FilterSet):
    class Meta:
        model = Permiso
        fields = {"nombre": ["exact", "contains"], }


class RolFilter(FilterSet):
    class Meta:
        model = Rol
        fields = {"nombre": ["exact", "contains"], }


class UsuarioFilter(FilterSet):
    class Meta:
        model = Usuario
        fields = {"username": ["exact", "contains"], }

