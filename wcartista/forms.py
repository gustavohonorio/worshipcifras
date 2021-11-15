from django import forms
from .models import Artista, Comentario


class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control w-100', 'cols': '30', 'rows': '9',
                                                              'placeholder': 'Escreva seu comentário*'}))

    class Meta:
        model = Comentario
        fields = ['comentario']


class ArtistaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Nome do Artista / '
                                                                                                 'Banda*'}))

    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Gênero(s)* '
                                                                                                   'Exemplo: Worship,'
                                                                                                   ' Adoração, etc'}))

    class Meta:
        model = Artista
        fields = ['nome', 'genero', ]
