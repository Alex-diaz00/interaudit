
from django.db import models


class GacetaOficial(models.Model):
    fecha_publicacion = models.DateField()
    numero = models.IntegerField()
    edicion = models.CharField()

    class Meta:
        db_table = 'gaceta_oficial'


class Emisor(models.Model):
    descripcion = models.CharField(verbose_name="Emisor")

    class Meta:
        db_table = 'emisor'


class TipoDisposicionFuncion(models.Model):
    descripcion = models.CharField(verbose_name="Disposición")

    class Meta:
        db_table = 'tipo_disposicon_funcion'


class TipoDisposicionEmite(models.Model):
    descripcion = models.CharField(verbose_name="Disposición")

    class Meta:
        db_table = 'tipo_disposicon_emite'


class TiempoDisposicionEstado(models.Model):

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        db_table = 'tiempo_disposicion_estado'


class EstadoDisposicion(models.Model):
    descripcion = models.CharField(verbose_name="Nombre de estado de disposición")
    id_tiempo = models.ForeignKey(TiempoDisposicionEstado, on_delete=models.CASCADE, db_column='id_tiempo_disposicion_estado',
                               blank=True, null=True)
    class Meta:
        db_table = 'estado_disposicion'


class Disposicion(models.Model):
    estado = models.BooleanField(default=True)
    resumen = models.TextField(blank=True, max_length=1000)
    numero = models.IntegerField()
    fecha_emision = models.DateField()
    fecha_vigor = models.DateField()
    id_gaceta = models.ForeignKey(GacetaOficial, on_delete=models.CASCADE, db_column='id_gaceta',
                               blank=True, null=True)
    emisor = models.ManyToManyField(Emisor)
    tipo_disposicion_funcion = models.ManyToManyField(TipoDisposicionFuncion)
    id_tipo_disposicion_emite = models.ForeignKey(TipoDisposicionEmite, on_delete=models.CASCADE,
                                                  db_column='id_tipo_disposicion_emite')
    estado_disposicion = models.ManyToManyField(EstadoDisposicion)


    class Meta:
        db_table = 'disposicion'


class NotaCambio(models.Model):
    descripcion = models.CharField()
    id_disposicion = models.ForeignKey(Disposicion, on_delete=models.CASCADE,
                                                  db_column='id_disposicion')
    class Meta:
        db_table = 'nota_cambio'