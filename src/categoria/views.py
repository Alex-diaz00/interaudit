from django_tables2 import SingleTableView
from rest_framework.decorators import api_view

from categoria.filters import SubcategoriaFilter, CategoriaFilter
from categoria.forms import CategoriaForm, SubcategoriaForm
from categoria.models import Categoria, Subcategoria
from categoria.tables import CategoriaTable, SubcategoriaTable
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect

class CategoriaTView(SingleTableView):
    model = Categoria
    table_class = CategoriaTable
    template_name = 'pages/categoria.html'
    filterset_class = CategoriaFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_form = CategoriaForm()
        filter = CategoriaFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'categoria'
        context['categoria_form'] = categoria_form
        return context

@api_view(['POST'])
def insertar_categoria(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = CategoriaForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("/home/categorias")

def delete_categoria(request, id):
    obj = get_object_or_404(Categoria, id=id)
    obj.delete()
    return redirect("/home/categorias")


class SubcategoriaTView(SingleTableView):
    model = Subcategoria
    table_class = SubcategoriaTable
    template_name = 'pages/subcategoria.html'
    filterset_class = SubcategoriaFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategoria_form = SubcategoriaForm()
        filter = SubcategoriaFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'subcategoria'
        context['subcategoria_form'] = subcategoria_form
        return context

@api_view(['POST'])
def insertar_subcategoria(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = SubcategoriaForm(request.POST)
    print(request.POST)
    if form.is_valid():

        subcategoria = Subcategoria()
        subcategoria.nombre = request.POST['nombre']
        subcategoria.estado = True
        subcategoria.save()
        categoria = Categoria.objects.filter(id=request.POST['categoria']).first()
        categoria.id_subcategoria.add(subcategoria)
        categoria.save()
        # form.save_m2m()
    return redirect("/home/subcategorias")

def delete_subcategoria(request, id):
    obj = get_object_or_404(Subcategoria, id=id)
    obj.delete()
    return redirect("/home/subcategorias")


def editar_subcategoria(request):
    subcategoria = Subcategoria.objects.get(id= int(request.POST['id']))
    subcategoria.nombre = request.POST['nombre']
    subcategoria.estado = False
    if "estado" in request.POST:
        subcategoria.estado = True
    subcategoria.save()
    return redirect("/home/subcategorias")

def edicion_subcategoria(request, id):
    subcategoria = Subcategoria.objects.get(id=id)
    initial_data = {
        'nombre': subcategoria.nombre,
        'estado': subcategoria.estado,
        }
    subcategoria_form = SubcategoriaForm(initial=initial_data)
    data = {
        'subcategoria': subcategoria,
        'subcategoria_form': subcategoria_form
    }
    return render(request, 'pages/edicion-subcategoria.html', data)


def editar_categoria(request):
    categoria = Categoria.objects.get(id= int(request.POST['id']))
    categoria.nombre = request.POST['nombre']
    categoria.estado = False
    if "estado" in request.POST:
        categoria.estado = True
    categoria.save()
    return redirect("/home/categorias")

def edicion_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    initial_data = {
        'nombre': categoria.nombre,
        'estado': categoria.estado,
        }
    categoria_form = CategoriaForm(initial=initial_data)
    data = {
        'categoria': categoria,
        'categoria_form': categoria_form
    }
    return render(request, 'pages/edicion-categoria.html', data)