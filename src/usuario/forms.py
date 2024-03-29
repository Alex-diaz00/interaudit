from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from usuario.models import Permiso, Usuario, Rol


class PermisoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Permiso
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RolForm(forms.ModelForm):
    required_css_class = 'required'
    id_permiso = forms.MultipleChoiceField(
        required=False, label='Permisos:',
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Rol
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_permiso'].choices = Permiso.objects.all().values_list('id', 'nombre').order_by('nombre')

        if kwargs:
            print(kwargs)
            rol = Rol.objects.get(id=kwargs['instance'].id)
            permisos = rol.id_permiso.all().values_list('id', 'nombre')
            self.fields['id_permiso'] = forms.ModelMultipleChoiceField(
                widget=forms.CheckboxSelectMultiple,
                required=False, label='Permisos:',
                queryset=Permiso.objects.all().order_by('nombre'),
                initial=[c[0] for c in permisos])


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label=_("Nombre de usuario"),
        max_length=150,
        error_messages={
            "unique": _("Ya existe un usuario con ese nombre."),
        },
    )
    password1 = forms.CharField(
      label=_("Contraseña"),
      widget=forms.PasswordInput(),

  )
    password2 = forms.CharField(
      label=_("Confirmar Contraseña"),
      widget=forms.PasswordInput(),
  )
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), empty_label="Seleccione")
    email = forms.EmailField(max_length=255, required=True, label='Correo electrónico')
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'rol', 'estado',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class UsuarioEditarForm(forms.ModelForm):

    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), empty_label="Seleccione")
    email = forms.EmailField(max_length=255, required=True, label='Correo electrónico')
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'rol', 'estado',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
