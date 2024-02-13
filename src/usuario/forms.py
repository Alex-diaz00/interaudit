import self as self
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from usuario.models import Permiso, Usuario, Rol


class PermisoForm(forms.ModelForm):

    class Meta:
        model = Permiso
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "ml-2 border rounded border-black"})


class RolForm(forms.ModelForm):
    id_permiso = forms.MultipleChoiceField(
        required=False, label='Permisos:',
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Rol
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "ml-2 border rounded border-black"})
        self.fields["id_permiso"].widget.attrs.update({"class": "ml-2 rounded border-black"})
        self.fields['id_permiso'].choices = Permiso.objects.all().values_list('id', 'nombre').order_by('nombre')


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
      label=_("Contraseña"),
      widget=forms.PasswordInput(),
  )
    password2 = forms.CharField(
      label=_("Confirmar Contraseña"),
      widget=forms.PasswordInput(),
  )
    rol = forms.ModelChoiceField(queryset=Rol.objects.all())
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'rol', 'estado',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "ml-2 border rounded border-black"})
