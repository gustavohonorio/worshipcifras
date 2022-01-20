from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail.message import EmailMessage
from django import forms
from .models import Usuario
from .utils import static_vars


class RedefinirSenhaForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'single-input', }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'single-input', }))
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'single-input date', }))

    def send_email(self, nome, email):

        conteudo = f'Olá {nome}, a sua senha foi alterada com sucesso.\n\n' \
                   f'Caso não tenha sido você que fez esta solicitação, mande um e-email para ' \
                   f'contato@worshipcifras.com.br, nos informando o acontecido.\n\n' \
                   f'Atensiosamente, time Worship Cifras\n\n' \
                   f'Deus abençoe.'

        mail = EmailMessage(
            subject='Senha alterada com sucesso',
            body=conteudo,
            from_email='no-reply@worshipcifras.com.br',
            to=['no-reply@worshipcifras.com.br', email],
            headers={'Reply-To': email}
        )

        mail.send()

    class Meta:
        model = Usuario
        fields = []


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
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Senha', }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Confirmar Senha',}))

    def send_email(self):
        nome = self.cleaned_data['first_name'] + ' ' + self.cleaned_data['last_name']
        email = self.cleaned_data['email']

        conteudo = f'Olá {nome}, seja bem vindo ao Worship Cifras.\n\n' \
                   f'Em nossa comunidade, buscar a excelência para o nosso momento de adoração é um propósito.\n\n' \
                   f'Conte conosco.\n\n' \
                   f'Deus abençoe.'

        mail = EmailMessage(
            subject='Seja bem vindo à comunidade Worship Cifras',
            body=conteudo,
            from_email='no-reply@worshipcifras.com.br',
            to=['no-reply@worshipcifras.com.br', email],
            headers={'Reply-To': email}
        )

        mail.send()

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
