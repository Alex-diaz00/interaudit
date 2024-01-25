from rest_framework import serializers

from disposicion.models import GacetaOficial, Emisor, TipoDisposicionFuncion, TipoDisposicionEmite, \
    TiempoDisposicionEstado, EstadoDisposicion, Disposicion, NotaCambio


class GacetaOficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = GacetaOficial
        fields = '__all__'


class EmisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emisor
        fields = '__all__'


class TipoDisposicionFuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDisposicionFuncion
        fields = '__all__'


class TipoDisposicionEmiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDisposicionEmite
        fields = '__all__'


class TiempoDisposicionEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiempoDisposicionEstado
        fields = '__all__'


class EstadoDisposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDisposicion
        fields = '__all__'


class DisposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disposicion
        fields = '__all__'


class NotaCambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaCambio
        fields = '__all__'


