
from django_tables2 import tables
from usuario.models import Usuario, Permiso, Rol



class UsuarioTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True , template_code='<a href="{% url "delete_user" record.id %}" id="btn-delete-table" class="btn btn-danger fa fa-trash fill-red-500" >')
    class Meta:
        model = Usuario
        template_name = "django_tables2/bootstrap4.html"
        fields = ('username', 'email', 'estado', 'rol')
        order_by = ('username', 'email','rol',)
        attrs = {"class": "table border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}


class PermisoTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True , template_code='<a href="{% url "delete_permiso" record.id %}" id="btn-delete-table" class="btn btn-danger fa fa-trash fill-red-500" >')
    class Meta:
        model = Permiso
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nombre', 'estado')
        order_by = ('nombre',)
        attrs = {"class": "table border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}


class RolTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True , template_code='<a href="{% url "delete_rol" record.id %}" id="btn-delete-table" class="btn btn-danger fa fa-trash fill-red-500" >')
    class Meta:
        model = Rol
        template_name = "django_tables2/bootstrap4.html"
        fields = ( 'nombre', 'id_permiso', 'estado')
        order_by = ('nombre',)

        attrs = {"class": "table border-collapse table-auto	table-striped text-xl table-bordered", "style": "width: 90%;"}
