
from django_tables2 import tables
from usuario.models import Usuario, Permiso, Rol



class UsuarioTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_usuario" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_user" record.id %}" name="{{ record.username }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')

    class Meta:
        model = Usuario
        template_name = "django_tables2/bootstrap4.html"
        fields = ('username', 'email', 'estado', 'rol')
        order_by = ('username', 'email','rol',)
        per_page = 10
        attrs = {"class": "my-4 border-collapse table-auto table-striped text-xl table-bordered", "style": "width: 90%;"}
        paginate_by = 5

class PermisoTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_permiso" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_permiso" record.id %}" name="{{ record.nombre }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    class Meta:
        model = Permiso
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nombre', 'estado')
        per_page = 10
        order_by = ('nombre',)
        attrs = {"class": "my-4 border-collapse table-auto table-striped text-xl table-bordered", "style": "width: 90%;"}


class RolTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_rol" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_rol" record.id %}" name="{{ record.nombre }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    class Meta:
        model = Rol
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nombre', 'id_permiso', 'estado')
        per_page = 10
        order_by = ('nombre',)
        attrs = {"class": "mb-4 border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}

