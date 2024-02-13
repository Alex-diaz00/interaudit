from django import forms

from categoria.models import Subcategoria, Categoria



class SubcategoriaForm(forms.ModelForm):
    categoria = forms.ChoiceField(
        label='Categoría asociada',
    )

    class Meta:
        model = Subcategoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "ml-2 border rounded border-black"})
        self.fields['categoria'].choices = Categoria.objects.all().values_list('id', 'nombre')


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "ml-2 border rounded border-black"})
