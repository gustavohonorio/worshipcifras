from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from worshipcifras.settings import DATE_INPUT_FORMATS
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Nome'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Sobrenome'}))
    nascimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={'class': 'input100 js-datepicker', 'data-target': '#datetimepicker1', 'placeholder': 'Data de nascimento'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Celular'}))
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
