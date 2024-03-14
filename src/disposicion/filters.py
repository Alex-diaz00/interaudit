from django_filters import FilterSet

from disposicion.models import *


class TipoDisposicionFuncionFilter(FilterSet):
    class Meta:
        model = TipoDisposicionFuncion
        fields = {"descripcion": ["exact", "contains"], }

class TipoDisposicionEmiteFilter(FilterSet):
    class Meta:
        model = TipoDisposicionEmite
        fields = {"descripcion": ["exact", "contains"], }

class EstadoDisposicionFilter(FilterSet):
    class Meta:
        model = EstadoDisposicion
        fields = {"descripcion": ["exact", "contains"], }

class EmisorFilter(FilterSet):
    class Meta:
        model = Emisor
        fields = {"descripcion": ["exact", "contains"], }


