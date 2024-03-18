from django import forms

from disposicion.models import TipoDisposicionFuncion, TipoDisposicionEmite, EstadoDisposicion, Emisor


class TipoDisposicionFuncionForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = TipoDisposicionFuncion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class TipoDisposicionEmiteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = TipoDisposicionEmite
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EstadoDisposicionForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = EstadoDisposicion
        fields = ('descripcion',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EmisorForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Emisor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
