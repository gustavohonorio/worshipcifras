from django import forms
from .models import Cifra, Comentario
from wcartista.models import Artista
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

    class Meta:
        model = Cifra
        fields = ['nome', 'genero', 'cifra', 'detalhes', 'tom', 'capotraste', 'afinacao', 'versao', ]
