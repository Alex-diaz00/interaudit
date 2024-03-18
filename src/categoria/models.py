from django.db import models


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=500)
    estado = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        db_table = 'subcategoria'

    def __str__(self):
        return self.nombre

class Categoria (models.Model):
    nombre = models.CharField(max_length=500)
    estado = models.BooleanField(default=True, verbose_name="Activo")
    id_subcategoria = models.ManyToManyField(Subcategoria, verbose_name='Subcategorías asociadas',
                                             related_name='categorias')
    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre



