from django import forms
from wcartista.models import Artista


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
