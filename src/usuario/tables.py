
from django_tables2 import tables
from usuario.models import Usuario, Permiso, Rol



class UsuarioTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_usuario" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_user" record.id %}" name="{{ record.username }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    estado = tables.columns.BooleanColumn(verbose_name="Activo", yesno=("Habilitado", "Deshabilitado"), orderable=False )
    email = tables.columns.EmailColumn(verbose_name="Correo electrónico", orderable=False)
    rol = tables.columns.Column(orderable=False, verbose_name='Rol')

    class Meta:
        model = Usuario
        # orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('username', 'email', 'estado', 'rol')
        order_by = ('username',)
        per_page = 10
        attrs = {"class": "text-center my-4 border-collapse table-responsive{-sm|-md|-lg|-xl} table-auto table-hover text-xl table-bordered", "style": "width: 90%;"}
        paginate_by = 5

class PermisoTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_permiso" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_permiso" record.id %}" name="{{ record.nombre }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    estado = tables.columns.BooleanColumn(orderable=False , verbose_name="Activo", yesno=("Habilitado", "Deshabilitado"))
    class Meta:
        model = Permiso
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nombre', 'estado')
        per_page = 10
        order_by = ('nombre',)
        attrs = {"class": "text-center my-4 border-collapse table-responsive{-sm|-md|-lg|-xl} table-auto table-hover text-xl table-bordered", "style": "width: 90%;"}


class RolTable(tables.Table):
    accion = tables.columns.TemplateColumn(verbose_name='Acciones', orderable=False, exclude_from_export=True,
                                           template_code='<div>'
                                                         '<a href="{% url "edicion_rol" record.id %}" id="btn-edit-table" class="btn btn-edit fa fa-edit p-1 m-1 bg-green-500 rounded text-white" >'
                                                         '<a href="{% url "delete_rol" record.id %}" name="{{ record.nombre }}" id="btn-delete-table" class="btn btn-danger fa fa-trash px-2 m-1 bg-red-600 rounded text-white" >'
                                                         '</div>')
    estado = tables.columns.BooleanColumn(verbose_name="Activo", yesno=("Habilitado", "Deshabilitado"), orderable=False)
    class Meta:
        model = Rol
        # orderable = False
        # empty_text = 'No hay datos a mostrar'
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nombre', 'id_permiso', 'estado')
        per_page = 10
        order_by = ('nombre',)
        attrs = {"class": "text-center my-4 border-collapse table-responsive{-sm|-md|-lg|-xl} table-auto table-hover text-xl table-bordered", "style": "width: 90%;"}
