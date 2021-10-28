from django import forms
from .models import Cifra
from wcartista.models import Artista


class CifraForm(forms.ModelForm):
    tom_choices = (
        ('0', 'Selecionar tom'),
        ('1', 'A'),
        ('2', 'Bb'),
        ('3', 'B'),
        ('4', 'C'),
        ('5', 'Dd'),
        ('6', 'D'),
        ('7', 'Eb'),
        ('8', 'E'),
        ('9', 'F'),
        ('10', 'G'),
        ('11', 'Ab'),
    )
    tom = forms.ChoiceField(choices=tom_choices, initial=0, )

    capotraste_choices = (
        ('0', 'Sem capotraste'),
        ('1', '1º Casa'),
        ('2', '2º Casa'),
        ('3', '3º Casa'),
        ('4', '4º Casa'),
        ('5', '5º Casa'),
    )
    capotraste = forms.ChoiceField(choices=capotraste_choices, initial=0, )

    afinacao_choices = (
        ('0', 'Afinação'),
        ('1', 'E A D G B E'),
        ('2', 'Eb Ab Db Gb Bb Eb'),
        ('3', 'D G C F A D'),
        ('4', 'Db Gb Cb Fb Ab Db'),
        ('5', 'C F Bb Eb G C'),
    )
    afinacao = forms.ChoiceField(choices=afinacao_choices, initial=0, )

    versao_choices = (
        ('0', 'Versão'),
        ('1', 'Ao vivo'),
        ('2', 'Completa'),
        ('3', 'Simplificada'),
        ('4', 'Acústico'),
        ('5', 'Padrão'),
    )
    versao = forms.ChoiceField(choices=versao_choices, initial=0, )

    # wc_artista = forms.ModelChoiceField(queryset=Artista.objects.all())

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Nome da música*'}))

    genero_choices = (
        ('0', 'Gênero principal'),
        ('1', 'Worship'),
        ('2', 'Clássicos'),
        ('3', 'Poprock'),
        ('4', 'Rock'),
        ('5', 'Reggae'),
    )
    genero = forms.ChoiceField(choices=genero_choices, )

    cifra = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; border: none; outline: none; '
                                                                  'background: #f9f9ff; height: 500px;',
                                                         'placeholder': 'Transcrição da cifra*'}))

    detalhes = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; border: none; outline: none; '
                                                                     'background: #f9f9ff; height: 200px;',
                                                            'placeholder': 'Deseja enviar algum detalhe adicional '
                                                                           'para nossa equipe? (Opcional)'}))

    class Meta:
        model = Cifra
        fields = ['nome', 'wc_artista', 'genero', 'cifra', 'detalhes', 'tom', 'capotraste', 'afinacao', 'versao', ]
