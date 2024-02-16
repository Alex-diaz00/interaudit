from django_tables2 import tables

from categoria.models import Categoria, Subcategoria


class CategoriaTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<a href="{% url "delete_categoria" record.id %}" id="delete" role="button" class="inline-block rounded bg-red-500 text-neutral-50 shadow-[0_4px_9px_-4px_rgba(51,45,45,0.7)] hover:bg-blue-600 hover:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] focus:bg-red-800 focus:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] active:bg-red-700 active:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] px-2 pb-2 pt-2 text-xs font-medium uppercase leading-normal transition duration-150 ease-in-out focus:outline-none focus:ring-0">'
                                                         '<svg class="h-4 fill-[#ffffff]" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">'
                                                         '  <path d="M135.2 17.7C140.6 6.8 151.7 0 163.8 0H284.2c12.1 0 23.2 6.8 28.6 17.7L320 32h96c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 96 0 81.7 0 64S14.3 32 32 32h96l7.2-14.3zM32 128H416V448c0 35.3-28.7 64-64 64H96c-35.3 0-64-28.7-64-64V128zm96 64c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16zm96 0c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16zm96 0c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16z"></path> </svg> </a>')

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
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True ,
    template_code='<a href="{% url "delete_subcategoria" record.id %}" id="delete" role="button" class="inline-block rounded bg-red-500 text-neutral-50 shadow-[0_4px_9px_-4px_rgba(51,45,45,0.7)] hover:bg-blue-600 hover:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] focus:bg-red-800 focus:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] active:bg-red-700 active:shadow-[0_8px_9px_-4px_rgba(51,45,45,0.2),0_4px_18px_0_rgba(51,45,45,0.1)] px-2 pb-2 pt-2 text-xs font-medium uppercase leading-normal transition duration-150 ease-in-out focus:outline-none focus:ring-0">'
                  '<svg class="h-4 fill-[#ffffff]" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">'
                  '  <path d="M135.2 17.7C140.6 6.8 151.7 0 163.8 0H284.2c12.1 0 23.2 6.8 28.6 17.7L320 32h96c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 96 0 81.7 0 64S14.3 32 32 32h96l7.2-14.3zM32 128H416V448c0 35.3-28.7 64-64 64H96c-35.3 0-64-28.7-64-64V128zm96 64c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16zm96 0c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16zm96 0c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16z"></path> </svg> </a>')

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
