from django import forms
from .models import Cifra, Comentario
from wcartista.models import Artista
from django.core.mail.message import EmailMessage
from .utils.static_vars import VarsCifraForm


class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control w-100', 'cols': '30', 'rows': '9',
                                                              'placeholder': 'Escreva seu comentário*'}))

    class Meta:
        model = Comentario
        fields = ['comentario']


class CifraForm(forms.ModelForm):
    tom = forms.ChoiceField(choices=VarsCifraForm.tom_choices, initial=0, )

    capotraste = forms.ChoiceField(choices=VarsCifraForm.capotraste_choices, initial=0, )

    afinacao = forms.ChoiceField(choices=VarsCifraForm.afinacao_choices, initial=0, )

    versao = forms.ChoiceField(choices=VarsCifraForm.versao_choices, initial=0, )

    wc_artista = forms.CharField(widget=forms.TextInput(attrs={'id': 'buscar_artista', 'class': 'single-input', 'placeholder': 'Nome do '
                                                                                                       'artista / '
                                                                                                       'banda',}))

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Nome da música*'}))

    genero = forms.ChoiceField(choices=VarsCifraForm.genero_choices, )

    cifra = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; border: none; outline: none; '
                                                                  'background: #f9f9ff; height: 500px;',
                                                         'placeholder': 'Transcrição da cifra*'}))

    detalhes = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; border: none; outline: none; '
                                                                     'background: #f9f9ff; height: 200px;',
                                                            'placeholder': 'Deseja enviar algum detalhe adicional '
                                                                           'para nossa equipe? (Opcional)'}))

    def send_email(self, id, nome, artista):

        conteudo = f'Olá time, uma nova cifra foi enviada e esta pendente de aprovação.\n\n' \
                   f'ID: {id}, NOME: {nome}, ARTISTA: {artista}.\n\n' \
                   f'Encontre-a no ambiente Staff do sistema, revise e siga com os procedimentos de aprovação.' \
                   f'Caso encontre algum problema, comunique o time de segundo nível.\n\n' \
                   f'O SLA para o atendimento desta solicitação é de 48 horas.\n\n' \
                   f'Atensiosamente, \n\n' \
                   f'Deus abençoe.'

        mail = EmailMessage(
            subject='Nova cifra cadastrada',
            body=conteudo,
            from_email='no-reply@worshipcifras.com.br',
            to=['no-reply@worshipcifras.com.br'],
            headers={'Reply-To': 'no-reply@worshipcifras.com.br'}
        )

        mail.send()

    class Meta:
        model = Cifra
        fields = ['nome', 'genero', 'cifra', 'detalhes', 'tom', 'capotraste', 'afinacao', 'versao', ]
