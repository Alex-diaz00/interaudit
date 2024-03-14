from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view
from django_tables2 import SingleTableView
from rest_framework.response import Response

from disposicion.filters import *
from disposicion.forms import TipoDisposicionFuncionForm, TipoDisposicionEmiteForm, EstadoDisposicionForm, EmisorForm
from disposicion.models import GacetaOficial, Emisor, TipoDisposicionFuncion, TipoDisposicionEmite, \
    TiempoDisposicionEstado, EstadoDisposicion, Disposicion, NotaCambio
from disposicion.serializers import GacetaOficialSerializer, EmisorSerializer, TipoDisposicionFuncionSerializer, \
    TipoDisposicionEmiteSerializer, TiempoDisposicionEstadoSerializer, EstadoDisposicionSerializer, \
    DisposicionSerializer, NotaCambioSerializer
from disposicion.tables import TipoDisposicionFuncionTable, TipoDisposicionEmiteTable, EstadoDisposicionTable, \
    EmisorTable


class GacetaOficialView(ModelViewSet):
    serializer_class = GacetaOficial
    queryset = GacetaOficialSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return GacetaOficialSerializer


class EmisorView(ModelViewSet):
    serializer_class = Emisor
    queryset = EmisorSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return EmisorSerializer


class TipoDisposicionFuncionView(ModelViewSet):
    serializer_class = TipoDisposicionFuncion
    queryset = TipoDisposicionFuncionSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return TipoDisposicionFuncionSerializer

class TipoDisposicionEmiteView(ModelViewSet):
    serializer_class = TipoDisposicionEmite
    queryset = TipoDisposicionEmiteSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return TipoDisposicionEmiteSerializer

class TiempoDisposicionEstadoView(ModelViewSet):
    serializer_class = TiempoDisposicionEstado
    queryset = TiempoDisposicionEstadoSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return TiempoDisposicionEstadoSerializer


class EstadoDisposicionView(ModelViewSet):
    serializer_class = EstadoDisposicion
    queryset = EstadoDisposicionSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return EstadoDisposicionSerializer


class DisposicionView(ModelViewSet):
    serializer_class = Disposicion
    queryset = DisposicionSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return DisposicionSerializer


class NotaCambioView(ModelViewSet):
    serializer_class = NotaCambio
    queryset = NotaCambioSerializer.Meta.model.objects.all()

    def get_serializer_class(self):
        return NotaCambioSerializer

class TipoDisposicionFuncionTView(SingleTableView):
    model = TipoDisposicionFuncion
    table_class = TipoDisposicionFuncionTable
    template_name = 'pages/tipo-disposicion-funcion.html'
    filterset_class = TipoDisposicionFuncionFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disposicion_form = TipoDisposicionFuncionForm()
        filter = TipoDisposicionFuncionFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'tipo_disposicion_funcion'
        context['disposicion'] = disposicion_form
        return context

@api_view(['POST'])
def insertar_tipo_disposicion_funcion(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = TipoDisposicionFuncionForm(request.POST)
    if form.is_valid():
        form.save()

    disposicion = TipoDisposicionFuncion.objects.all()
    disposicion_form = TipoDisposicionFuncionForm()
    table_disposicion = TipoDisposicionFuncionTable(disposicion)
    filter = TipoDisposicionFuncionFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': disposicion,
                    'table': table_disposicion, 'filter': filter,
                     'disposicion': disposicion_form, 'added': True}

    return render(request, 'pages/tipo-disposicion-funcion.html', extra_context)



def editar_tipo_disposicion_funcion(request):
    disposicion = TipoDisposicionFuncion.objects.get(id= int(request.POST['id']))
    disposicion.descripcion = request.POST['descripcion']
    disposicion.save()
    return redirect("/home/tipo-disposicion-funcion")

def edicion_tipo_disposicion_funcion(request, id):
    disposicion = TipoDisposicionFuncion.objects.get(id=id)
    initial_data = {
        'descripcion': disposicion.descripcion,
        }
    disposicion_form = TipoDisposicionFuncionForm(initial=initial_data)
    data = {
        'disposicion': disposicion,
        'disposicion_form': disposicion_form
    }
    return render(request, 'pages/edicion-tipo-disposicion-funcion.html', data)

def delete_tipo_disposicion_funcion(request, id):
    obj = get_object_or_404(TipoDisposicionFuncion, id=id)
    obj.delete()

    disposicion = TipoDisposicionFuncion.objects.all()
    disposicion_form = TipoDisposicionFuncionForm()
    table_disposicion = TipoDisposicionFuncionTable(disposicion)
    filter = TipoDisposicionFuncionFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': disposicion,
                     'table': table_disposicion, 'filter': filter,
                     'disposicion': disposicion_form, 'deleted': True}

    return render(request, 'pages/tipo-disposicion-funcion.html', extra_context)
    # return redirect("/home/tipo-disposicion-funcion")

class TipoDisposicionEmiteTView(SingleTableView):
    model = TipoDisposicionEmite
    table_class = TipoDisposicionEmiteTable
    template_name = 'pages/tipo-disposicion-emite.html'
    filterset_class = TipoDisposicionEmiteFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disposicion_form = TipoDisposicionEmiteForm()
        filter = TipoDisposicionEmiteFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'tipo_disposicion_emite'
        context['disposicion'] = disposicion_form
        return context

@api_view(['POST'])
def insertar_tipo_disposicion_emite(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = TipoDisposicionEmiteForm(request.POST)
    if form.is_valid():
        form.save()

    disposicion = TipoDisposicionEmite.objects.all()
    disposicion_form = TipoDisposicionEmiteForm()
    table_disposicion = TipoDisposicionEmiteTable(disposicion)
    filter = TipoDisposicionEmiteFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': disposicion,
                     'table': table_disposicion, 'filter': filter,
                     'disposicion': disposicion_form, 'added': True}

    return render(request, 'pages/tipo-disposicion-emite.html', extra_context)

    # return redirect("/home/tipo-disposicion-emite")


def editar_tipo_disposicion_emite(request):
    disposicion = TipoDisposicionEmite.objects.get(id= int(request.POST['id']))
    disposicion.descripcion = request.POST['descripcion']
    disposicion.save()
    return redirect("/home/tipo-disposicion-emite")

def edicion_tipo_disposicion_emite(request, id):
    disposicion = TipoDisposicionEmite.objects.get(id=id)
    initial_data = {
        'descripcion': disposicion.descripcion,
        }
    disposicion_form = TipoDisposicionEmiteForm(initial=initial_data)
    data = {
        'disposicion': disposicion,
        'disposicion_form': disposicion_form
    }
    return render(request, 'pages/edicion-tipo-disposicion-emite.html', data)

def delete_tipo_disposicion_emite(request, id):
    obj = get_object_or_404(TipoDisposicionEmite, id=id)
    obj.delete()

    disposicion = TipoDisposicionEmite.objects.all()
    disposicion_form = TipoDisposicionEmiteForm()
    table_disposicion = TipoDisposicionEmiteTable(disposicion)
    filter = TipoDisposicionEmiteFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': disposicion,
                     'table': table_disposicion, 'filter': filter,
                     'disposicion': disposicion_form, 'deleted': True}
    return render(request, 'pages/tipo-disposicion-emite.html', extra_context)
    # return redirect("/home/tipo-disposicion-emite")


class EstadoDisposicionTView(SingleTableView):
    model = EstadoDisposicion
    table_class = EstadoDisposicionTable
    template_name = 'pages/estado-disposicion.html'
    filterset_class = EstadoDisposicionFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disposicion_form = EstadoDisposicionForm()
        filter = EstadoDisposicionFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'estado_disposicion'
        context['disposicion'] = disposicion_form
        return context

@api_view(['POST'])
def insertar_estado_disposicion(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = EstadoDisposicionForm(request.POST)
    if form.is_valid():
        form.save()

    disposicion = EstadoDisposicion.objects.all()
    disposicion_form = EstadoDisposicionForm()
    table_disposicion = EstadoDisposicionTable(disposicion)
    filter = EstadoDisposicionFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': disposicion,
                     'table': table_disposicion, 'filter': filter,
                     'disposicion': disposicion_form, 'added': True}
    return render(request, 'pages/estado-disposicion.html', extra_context)
    # return redirect("/home/estado-disposicion")


def editar_estado_disposicion(request):
    disposicion = EstadoDisposicion.objects.get(id= int(request.POST['id']))
    disposicion.descripcion = request.POST['descripcion']
    disposicion.save()
    return redirect("/home/estado-disposicion")

def edicion_estado_disposicion(request, id):
    disposicion = EstadoDisposicion.objects.get(id=id)
    initial_data = {
        'descripcion': disposicion.descripcion,
        }
    disposicion_form = EstadoDisposicionForm(initial=initial_data)
    data = {
        'disposicion': disposicion,
        'disposicion_form': disposicion_form
    }
    return render(request, 'pages/edicion-estado-disposicion.html', data)

def delete_estado_disposicion(request, id):
    obj = get_object_or_404(EstadoDisposicion, id=id)
    obj.delete()

    disposicion = EstadoDisposicion.objects.all()
    disposicion_form = EstadoDisposicionForm()
    table_disposicion = EstadoDisposicionTable(disposicion)
    filter = EstadoDisposicionFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': disposicion,
                     'table': table_disposicion, 'filter': filter,
                     'disposicion': disposicion_form, 'deleted': True}
    return render(request, 'pages/estado-disposicion.html', extra_context)
    # return redirect("/home/estado-disposicion")

class EmisorTView(SingleTableView):
    model = Emisor
    table_class = EmisorTable
    template_name = 'pages/emisor.html'
    filterset_class = EmisorFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filterset_class(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emisor_form = EmisorForm()
        filter = EmisorFilter()
        context['filter'] = filter
        context['parent'] = 'pages'
        context['segment'] = 'emisor'
        context['emisor'] = emisor_form
        return context

@api_view(['POST'])
def insertar_emisor(request):
    if request.method != "POST":
        return Response({'message': "Tipo de petición no valida"}, status=400)
    form = EmisorForm(request.POST)
    if form.is_valid():
        form.save()

    emisores = Emisor.objects.all()
    emisor_form = EmisorForm()
    table_emisor = EmisorTable(emisores)
    filter = EmisorFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': emisores,
                     'table': table_emisor, 'filter': filter,
                     'emisor': emisor_form, 'added': True}
    return render(request, 'pages/emisor.html', extra_context)
    # return redirect("/home/emisor")


def editar_emisor(request):
    emisor = Emisor.objects.get(id= int(request.POST['id']))
    emisor.descripcion = request.POST['descripcion']
    emisor.save()
    return redirect("/home/emisor")

def edicion_emisor(request, id):
    emisor = Emisor.objects.get(id=id)
    initial_data = {
        'descripcion': emisor.descripcion,
        }
    emisor_form = EmisorForm(initial=initial_data)
    data = {
        'emisor': emisor,
        'emisor_form': emisor_form
    }
    return render(request, 'pages/edicion-emisor.html', data)

def delete_emisor(request, id):
    obj = get_object_or_404(Emisor, id=id)
    obj.delete()

    emisores = Emisor.objects.all()
    emisor_form = EmisorForm()
    table_emisor = EmisorTable(emisores)
    filter = EmisorFilter()
    extra_context = {'parent': 'pages', 'segment': 'tables', 'object_list': emisores,
                     'table': table_emisor, 'filter': filter,
                     'emisor': emisor_form, 'deleted': True}
    return render(request, 'pages/emisor.html', extra_context)
    # return redirect("/home/emisor")


