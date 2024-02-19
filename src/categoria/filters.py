from django_filters import FilterSet
from categoria.models import *


class CategoriaFilter(FilterSet):
    class Meta:
        model = Categoria
        fields = {"nombre": ["exact", "contains"], }

class SubcategoriaFilter(FilterSet):
    class Meta:
        model = Subcategoria
        fields = {"nombre": ["exact", "contains"], }