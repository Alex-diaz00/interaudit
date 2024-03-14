from django_tables2 import tables

from disposicion.models import TipoDisposicionFuncion, TipoDisposicionEmite, EstadoDisposicion, Emisor


class TipoDisposicionFuncionTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_tipo_disposicion_funcion" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_tipo_disposicion_funcion" record.id %}" name="{{ record.descripcion }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    class Meta:
        model = TipoDisposicionFuncion
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('descripcion',)
        per_page = 10
        order_by = ('descripcion',)
        attrs = {"class": "text-center my-4 border-collapse table-auto table-striped text-xl table-bordered", "style": "width: 90%;"}


class TipoDisposicionEmiteTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_tipo_disposicion_emite" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_tipo_disposicion_emite" record.id %}" name="{{ record.descripcion }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    class Meta:
        model = TipoDisposicionEmite
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('descripcion',)
        per_page = 10
        order_by = ('descripcion',)
        attrs = {"class": "text-center my-4 border-collapse table-auto table-striped text-xl table-bordered", "style": "width: 90%;"}


class EstadoDisposicionTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_estado_disposicion" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_estado_disposicion" record.id %}" name="{{ record.descripcion }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    class Meta:
        model = EstadoDisposicion
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('descripcion',)
        per_page = 10
        order_by = ('descripcion',)
        attrs = {"class": "text-center my-4 border-collapse table-auto table-striped text-xl table-bordered", "style": "width: 90%;"}


class EmisorTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_emisor" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_emisor" record.id %}" name="{{ record.descripcion }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    class Meta:
        model = Emisor
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('descripcion',)
        per_page = 10
        order_by = ('descripcion',)
        attrs = {"class": "text-center my-4 border-collapse table-auto table-striped text-xl table-bordered", "style": "width: 90%;"}

