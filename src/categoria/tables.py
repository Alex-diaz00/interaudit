from django_tables2 import tables

from categoria.models import Categoria, Subcategoria


class CategoriaTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True , template_code='<a href="{% url "delete_categoria" record.id %}" id="btn-delete-table" class="btn btn-danger fa fa-trash fill-red-500" >')
    categoria = tables.columns.Column(accessor="nombre", verbose_name="Categoría")
    # subcategoria = tables.columns.Column(accessor="id_subcategoria", verbose_name="Subcategorías asociadas")
    subcategoria = tables.columns.ManyToManyColumn(
        accessor='id_subcategoria.all',
        verbose_name='Subcategorias',
        transform=lambda id_subcategoria: id_subcategoria.nombre,

    )
    class Meta:
        model = Categoria
        template_name = "django_tables2/bootstrap4.html"
        fields = ( 'categoria', 'subcategoria', 'estado')
        order_by = ('categoria',)
        attrs = {"class": "table border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}



class SubcategoriaTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True , template_code='<a href="{% url "delete_subcategoria" record.id %}" id="btn-delete-table" class="btn btn-danger fa fa-trash fill-red-500" >')
    # categoria = tables.columns.Column(accessor="subcategorias.all", verbose_name="Categoría")
    categoria = tables.columns.ManyToManyColumn(
            accessor='subcategorias.all',  # Acceso al atributo 'permisos' del modelo Rol
            verbose_name='Subcategoria asociada',  # Nombre de la columna
            transform=lambda subcategorias: subcategorias.nombre,  # Función para transformar cada permiso en su nombre
            separator=', ',  # Separador para concatenar los nombres de los permisos
        )
    subcategoria = tables.columns.Column(accessor="nombre", verbose_name="Subcategorías asociadas")

    class Meta:
        model = Subcategoria
        template_name = "django_tables2/bootstrap4.html"
        fields = ( 'categoria', 'subcategoria', 'estado')
        order_by = ('categoria',)
        attrs = {"class": "table border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}
