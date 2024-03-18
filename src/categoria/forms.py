from django import forms

from categoria.models import Subcategoria, Categoria



class SubcategoriaForm(forms.ModelForm):
    required_css_class = 'required'
    categoria = forms.ModelChoiceField(
        label='Categoría asociada',
        queryset=Categoria.objects.all(),
        empty_label = "Seleccione"
    )

    class Meta:
        model = Subcategoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            subcategoria = Subcategoria.objects.get(id=kwargs['instance'].id)
            categoria = subcategoria.categorias.all().values_list('id', 'nombre').first()
            self.fields['categoria'] = forms.ModelChoiceField(
                widget=forms.Select,
                empty_label="Seleccione",
                label='Categoría asociada',
                queryset=Categoria.objects.all().order_by('nombre'),
                initial=categoria
                )


class CategoriaForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Categoria
        fields = ('nombre', 'estado',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
