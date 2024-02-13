from django_tables2 import SingleTableView
from rest_framework.decorators import api_view
from categoria.forms import CategoriaForm, SubcategoriaForm
from categoria.models import Categoria, Subcategoria
from categoria.tables import CategoriaTable, SubcategoriaTable
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect

class CategoriaTView(SingleTableView):
    model = Categoria
    table_class = CategoriaTable
    template_name = 'pages/categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_form = CategoriaForm()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategoria_form = SubcategoriaForm()
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