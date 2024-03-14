from django.shortcuts import get_object_or_404, render, redirect
from django_tables2 import SingleTableView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .filters import PermisoFilter, RolFilter, UsuarioFilter
from .forms import PermisoForm, RegistrationForm, RolForm, UsuarioEditarForm
from .serializers import UsuarioAllFieldsSerializer, RolSerializer, PermisoSerializer
from usuario.models import Usuario, Permiso, Rol

from .tables import UsuarioTable, PermisoTable, RolTable


class RolView(ModelViewSet):
    serializer_class = RolSerializer
    queryset = RolSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return RolSerializer

class Usuarios_Rol(GenericViewSet):
    serializer_class = UsuarioAllFieldsSerializer
    queryset = UsuarioAllFieldsSerializer.Meta.model.objects.all()

    def get_queryset(self):
        if not 'rol' in self.request.data:
            return Response({'message': 'No ha seleccionado un rol'}, status=400)
        queryset = Usuario.objects.filter(rol=self.request.data.rol)
        return queryset


class PermisoView(ModelViewSet):
    serializer_class = PermisoSerializer
    queryset = PermisoSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return RolSerializer

class UsuarioView(ModelViewSet):
    serializer_class = UsuarioAllFieldsSerializer
    queryset = UsuarioAllFieldsSerializer.Meta.model.objects.all()
    template_name = 'pages/usuario.html'

    def get_serializer_class(self):
        return UsuarioAllFieldsSerializer


def delete_user(request, id):
    obj = get_object_or_404(Usuario, id=id)
    obj.delete()

    filter = UsuarioFilter()
    form = RegistrationForm()
    errors = form.errors
    usuarios = Usuario.objects.all()
    usuario_form = RegistrationForm()
    table_usuarios = UsuarioTable(usuarios)
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': usuarios,
                     'form': form, 'errors': errors, 'table': table_usuarios,
                     'usuario_form': usuario_form, 'deleted': True, 'filter': filter}

    return render(request, 'pages/usuario.html', extra_context)

def delete_permiso(request, id):
    obj = get_object_or_404(Permiso, id=id)
    obj.delete()

    filter = PermisoFilter()
    form = PermisoForm()
    permisos = Permiso.objects.all()
    permiso_form = PermisoForm()
    table_permisos = PermisoTable(permisos)
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': permisos,
                     'form': form, 'table': table_permisos,
                     'permiso_form': permiso_form, 'deleted': True, 'filter': filter}

    return render(request, 'pages/permiso.html', extra_context)

def delete_rol(request, id):
    obj = get_object_or_404(Rol, id=id)
    obj.delete()

    filter = RolFilter()
    form = RolForm()
    roles = Rol.objects.all()
    rol_form = RolForm()
    table_roles = RolTable(roles)
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': roles,
                     'form': form, 'table': table_roles,
                     'rol_form': rol_form, 'deleted': True, 'filter': filter}

    return render(request, 'pages/rol.html', extra_context)

@api_view(['POST'])
def insertar_permiso(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = PermisoForm(request.POST)
    if form.is_valid():
        form.save()

    filter = PermisoFilter()
    permisos = Permiso.objects.all()
    permiso_form = PermisoForm()
    table_permisos = PermisoTable(permisos)
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': permisos,
                     'form': form, 'table': table_permisos,
                     'permiso_form': permiso_form, 'added': True, 'filter': filter}

    return render(request, 'pages/permiso.html', extra_context)

class UsuarioTView(SingleTableView):
    model = Usuario
    table_class = UsuarioTable
    template_name = 'pages/usuario.html'
    filterset_class = UsuarioFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_form = RegistrationForm()
        filter = UsuarioFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'usuarios'
        context['usuario_form'] = usuario_form
        return context

@api_view(['POST'])
def insertar_usuario(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)

    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        # return redirect("/home/usuarios")

    filter = UsuarioFilter()
    errors = form.errors
    usuarios = Usuario.objects.all()
    usuario_form = RegistrationForm()
    table_usuarios = UsuarioTable(usuarios)
    extra_context = {'parent': 'pages', 'segment': 'tables',  'object_list': usuarios,
                     'form': form, 'errors': errors, 'table': table_usuarios,
                     'usuario_form': usuario_form, 'added': True, 'filter': filter}

    return render(request, 'pages/usuario.html', extra_context)


class PermisoTView(SingleTableView):
    model = Permiso
    table_class = PermisoTable
    template_name = 'pages/permiso.html'
    filterset_class = PermisoFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        permiso_form = PermisoForm()
        filter = PermisoFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'permisos'
        context['permiso_form'] = permiso_form
        return context

class RolTView(SingleTableView):
    model = Rol
    table_class = RolTable
    template_name = 'pages/rol.html'
    filterset_class = RolFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol_form = RolForm()
        filter = RolFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'roles'
        context['rol_form'] = rol_form
        return context

@api_view(['POST'])
def insertar_rol(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = RolForm(request.POST)
    if form.is_valid():
        rol = form.save(commit=False)
        rol.save()
        form.save_m2m()

    filter = RolFilter()
    roles = Rol.objects.all()
    rol_form = RolForm()
    table_roles = RolTable(roles)
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': roles,
                     'form': form, 'table': table_roles,
                     'rol_form': rol_form, 'added': True, 'filter': filter}

    return render(request, 'pages/rol.html', extra_context)


def editar_permiso(request):
    permiso = Permiso.objects.get(id= int(request.POST['id']))
    permiso.nombre = request.POST['nombre']
    permiso.estado = False
    if "estado" in request.POST:
        permiso.estado = True
    permiso.save()
    return redirect("/home/permisos")

def edicion_permiso(request, id):
    permiso = Permiso.objects.get(id=id)
    initial_data = {
        'nombre': permiso.nombre,
        'estado': permiso.estado,
        }
    permiso_form = PermisoForm(initial=initial_data)
    data = {
        'permiso': permiso,
        'permiso_form': permiso_form
    }
    return render(request, 'pages/edicion-permiso.html', data)


def editar_rol(request):
    rol = Rol.objects.get(id= int(request.POST['id']))
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            rol = form.save()
    return redirect("/home/roles")

def edicion_rol(request, id):
    rol = Rol.objects.get(id=id)
    rol_form = RolForm(instance=rol)
    data = {
        'rol': rol,
        'rol_form': rol_form
    }
    return render(request, 'pages/edicion-rol.html', data)


def editar_usuario(request):
    usuario = Usuario.objects.get(id= int(request.POST['id']))
    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save()
        else:
            for field, errors in form.errors.items():
                print(f"Campo: {field}")
                for error in errors:
                    print(f"Error: {error}")
            data = {
                'usuario': usuario,
                'usuario_form': form
            }
            return render(request, 'pages/edicion-usuario.html', data)
    return redirect("/home/usuarios")

def edicion_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario_form = UsuarioEditarForm(instance=usuario)
    data = {
        'usuario': usuario,
        'usuario_form': usuario_form
    }
    return render(request, 'pages/edicion-usuario.html', data)
