from django import forms
from wcartista.models import Artista
from wccifras.models import Cifra
from wccifras.utils.static_vars import VarsCifraForm


class ArtistaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    integrantes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}), required=False)
    site = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    twitter = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    youtube = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    spotify = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    outro_link = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    igreja = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False, disabled=True)
    op_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False, disabled=True)

    class Meta:
        model = Artista
        fields = ['nome', 'integrantes', 'genero', 'descricao', 'site', 'facebook', 'twitter', 'youtube', 'spotify',
                  'outro_link', 'cidade', 'estado', 'pais', 'igreja', 'status', 'op_user', ]


class CifraForm(forms.ModelForm):
    # geral
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    # wc_artista = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                            'list': 'artista_auto_complete', }), required=False,
    #                              disabled=True)
    genero = forms.ChoiceField(choices=VarsCifraForm.genero_choices,
                               widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    cifra = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}), required=False)

    # adicionais
    tom = forms.ChoiceField(choices=VarsCifraForm.tom_choices,
                            widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    capotraste = forms.ChoiceField(choices=VarsCifraForm.capotraste_choices,
                                   widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    afinacao = forms.ChoiceField(choices=VarsCifraForm.afinacao_choices,
                                 widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    versao = forms.ChoiceField(choices=VarsCifraForm.versao_choices,
                               widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    detalhes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}), required=False)

    # verificada
    capa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    video = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    video_aula = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    compositor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    produtor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    musicos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    bpm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    patrocinada = forms.ChoiceField(choices=VarsCifraForm.patrocinada_choices,
                                    widget=forms.Select(attrs={'class': 'form-control'}), required=False)

    # sitema
    status = forms.ChoiceField(choices=VarsCifraForm.status_choices,
                               widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    op_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False, disabled=True)

    class Meta:
        model = Cifra
        fields = ['nome', 'genero', 'cifra', 'letra', 'acordes', 'tom', 'capotraste', 'afinacao',
                  'versao', 'detalhes', 'capa', 'video', 'video_aula', 'compositor', 'produtor', 'musicos', 'bpm',
                  'patrocinada', 'status', 'op_user']
