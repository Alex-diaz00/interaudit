from django_tables2 import tables

from categoria.models import Categoria, Subcategoria


class CategoriaTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_categoria" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_categoria" record.id %}" name="{{ record.nombre }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
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
        per_page = 10
        attrs = {"class": "my-4 border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}



class SubcategoriaTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_subcategoria" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_subcategoria" record.id %}" name="{{ record.nombre }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'    
                                                         '</div>')

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
        per_page = 10
        attrs = {"class": "my-4 border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}
