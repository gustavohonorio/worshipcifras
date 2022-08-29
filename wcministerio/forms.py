from django import forms
from .models import Ministerio
from django.core.mail.message import EmailMessage


class MinisterioForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Nome'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Descrição'}))
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Genero'}))

    class Meta:
        model = Ministerio
        fields = ['nome', 'descricao', 'genero', 'owner', ]


class IntegranteForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Digite o e-mail'}))

    def send_email(self, email, ministerio, is_user):
        if is_user:
            conteudo = f'Olá, você foi adicionado ao ministério {ministerio}.\n\n' \
                       f'Para não perder nenhuma novidade, basta acessar agora a plataforma, ' \
                       f'https://worshipcifras.com.br, e ir até a seção "Meus Ministérios".\n\n' \
                       f'Caso você não queira participar deste ministério, entre em contato com\n\n' \
                       f'contato@worshipcifras.com.br informando o seu desejo.\n\n' \
                       f'Atensiosamente, time Worship Cifras\n\n' \
                       f'Deus abençoe.'
        else:
            conteudo = f'Olá, você foi convidado para fazer parte do ministério {ministerio}.\n\n' \
                       f'Para aceitar, acesse https://worshipcifras.com.br/logon/register/ e crie a sua conta. ' \
                       f'Não se preocupe, é totalmente grátis.\n\n' \
                       f'Caso você não queira participar deste ministério, basta ignorar esta menção.\n\n' \
                       f'Atensiosamente, time Worship Cifras\n\n' \
                       f'Deus abençoe.'

        mail = EmailMessage(
            subject=f'Você foi convidado para fazer parte do ministério {ministerio}',
            body=conteudo,
            from_email='no-reply@worshipcifras.com.br',
            to=['no-reply@worshipcifras.com.br', email],
            headers={'Reply-To': email}
        )

        mail.send()

    class Meta:
        model = Ministerio
        fields = ['email', ]
