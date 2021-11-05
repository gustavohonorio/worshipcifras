from django import forms
from .models import Artista


class ArtistaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Nome do Artista / '
                                                                                                 'Banda*'}))

    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Gênero(s)* '
                                                                                                   'Exemplo: Worship,'
                                                                                                   ' Adoração, etc'}))

    class Meta:
        model = Artista
        fields = ['nome', 'genero', ]
