from django import forms
from .models import Cifra


class CifraForm(forms.ModelForm):
    class Meta:
        model = Cifra
        fields = "__all__"
