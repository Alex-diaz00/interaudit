from django import forms

from disposicion.models import TipoDisposicionFuncion, TipoDisposicionEmite, EstadoDisposicion, Emisor


class TipoDisposicionFuncionForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = TipoDisposicionFuncion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs.update({"class": "ml-2 border rounded border-black"})

class TipoDisposicionEmiteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = TipoDisposicionEmite
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs.update({"class": "ml-2 border rounded border-black"})


class EstadoDisposicionForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = EstadoDisposicion
        fields = ('descripcion',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs.update({"class": "ml-2 border rounded border-black"})


class EmisorForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Emisor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs.update({"class": "ml-2 border rounded border-black"})
