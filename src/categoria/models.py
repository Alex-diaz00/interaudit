from django.db import models


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=500)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'subcategoria'

    def __str__(self):
        return self.nombre

class Categoria (models.Model):
    nombre = models.CharField(max_length=500)
    estado = models.BooleanField(default=True)
    id_subcategoria = models.ManyToManyField(Subcategoria, null=True, verbose_name='Subcategorías asociadas',
                                             related_name='subcategorias')
    class Meta:
        db_table = 'categoria'





