from rest_framework.viewsets import ModelViewSet, GenericViewSet

from disposicion.models import GacetaOficial, Emisor, TipoDisposicionFuncion, TipoDisposicionEmite, \
    TiempoDisposicionEstado, EstadoDisposicion, Disposicion, NotaCambio
from disposicion.serializers import GacetaOficialSerializer, EmisorSerializer, TipoDisposicionFuncionSerializer, \
    TipoDisposicionEmiteSerializer, TiempoDisposicionEstadoSerializer, EstadoDisposicionSerializer, \
    DisposicionSerializer, NotaCambioSerializer


class GacetaOficialView(ModelViewSet):
    serializer_class = GacetaOficial
    queryset = GacetaOficialSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return GacetaOficialSerializer


class EmisorView(ModelViewSet):
    serializer_class = Emisor
    queryset = EmisorSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return EmisorSerializer


class TipoDisposicionFuncionView(ModelViewSet):
    serializer_class = TipoDisposicionFuncion
    queryset = TipoDisposicionFuncionSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return TipoDisposicionFuncionSerializer

class TipoDisposicionEmiteView(ModelViewSet):
    serializer_class = TipoDisposicionEmite
    queryset = TipoDisposicionEmiteSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return TipoDisposicionEmiteSerializer

class TiempoDisposicionEstadoView(ModelViewSet):
    serializer_class = TiempoDisposicionEstado
    queryset = TiempoDisposicionEstadoSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return TiempoDisposicionEstadoSerializer


class EstadoDisposicionView(ModelViewSet):
    serializer_class = EstadoDisposicion
    queryset = EstadoDisposicionSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return EstadoDisposicionSerializer


class DisposicionView(ModelViewSet):
    serializer_class = Disposicion
    queryset = DisposicionSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return DisposicionSerializer


class NotaCambioView(ModelViewSet):
    serializer_class = NotaCambio
    queryset = NotaCambioSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return NotaCambioSerializer

