from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from worshipcifras import settings
from worshipcifras.settings import DATE_INPUT_FORMATS
from .models import Usuario
from .utils import static_vars


class MeuPerfilForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': ''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': ''}))
    nascimento = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input date', 'placeholder': ''}))
    genero = forms.ChoiceField(choices=static_vars.genero_usuario, initial=0, )
    celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input phone_with_ddd', 'placeholder': ''}))
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': ''}))
    estado = forms.ChoiceField(choices=static_vars.estados, initial=0, )
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': ''}))
    cristao = forms.ChoiceField(choices=static_vars.cristao, initial=0, )
    igreja = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': ''}))
    funcao = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Ex: Líder '
                                                                                                   'Ministerio de Louvor'
                                                                                                   ', Guitarrista, etc'}))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'nascimento', 'genero', 'celular', 'cidade', 'estado', 'pais', 'cristao',
                  'igreja', 'funcao']


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Nome'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Sobrenome'}))
    nascimento = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'input100 date', 'placeholder': 'Data de nascimento'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100 phone_with_ddd', 'placeholder': 'Celular'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Senha'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Confirmar Senha'}))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'nascimento', 'celular', 'email', 'password', ]


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'celular')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'celular')
