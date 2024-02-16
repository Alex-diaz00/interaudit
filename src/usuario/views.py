from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django_tables2 import SingleTableView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .forms import PermisoForm, RegistrationForm, RolForm
from .serializers import UsuarioAllFieldsSerializer, RolSerializer, PermisoSerializer
from usuario.models import Usuario, Permiso, Rol
import django_tables2 as tables

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
    return redirect("/home/usuarios")

def delete_permiso(request, id):
    obj = get_object_or_404(Permiso, id=id)
    obj.delete()
    return redirect("/home/permisos")

def delete_rol(request, id):
    obj = get_object_or_404(Rol, id=id)
    obj.delete()
    return redirect("/home/roles")

@api_view(['POST'])
def insertar_permiso(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = PermisoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("/home/permisos")
class UsuarioTView(SingleTableView):
    model = Usuario
    table_class = UsuarioTable
    template_name = 'pages/usuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_form = RegistrationForm()
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
        return redirect("/home/usuarios")
    else:
        errors = form.errors
        usuarios = Usuario.objects.all()
        usuario_form = RegistrationForm()
        table_usuarios = UsuarioTable(usuarios)
        extra_context = {'parent': 'pages', 'segment': 'tables',  'object_list': usuarios,
                         'form': form, 'errors': errors, 'table': table_usuarios,
                         'usuario_form': usuario_form}

        return render(request, 'pages/usuario.html', extra_context)


class PermisoTView(SingleTableView):
    model = Permiso
    table_class = PermisoTable
    template_name = 'pages/permiso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        permiso_form = PermisoForm()
        context['parent'] = 'pages'
        context['segment'] = 'permisos'
        context['permiso_form'] = permiso_form
        return context

class RolTView(SingleTableView):
    model = Rol
    table_class = RolTable
    template_name = 'pages/rol.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol_form = RolForm()
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
    return redirect("/home/roles")