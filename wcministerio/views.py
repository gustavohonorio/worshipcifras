from random import randint

from django.contrib import messages
from django.shortcuts import render

from wclogon.models import Usuario
from wclogon.utils import user_functions
from .models import Ministerio, MinisterioIntegrantes
from .forms import MinisterioForm, IntegranteForm


# TODO : ADICAO DE INTEGRANTES NO MINISTERIO
def ministerios(request):
    form = MinisterioForm()

    ministerio = Ministerio.objects.filter(owner=request.user.id)

    if ministerio:
        return render(request, 'meus_ministerios.html', {'form': form, 'ministerio': ministerio[0]})

    if request.method == 'POST':
        form = MinisterioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            genero = form.cleaned_data['genero']

            novo_ministerio = Ministerio(nome=nome, descricao=descricao, genero=genero, owner=request.user.id,
                                         co_invite='W' + str(randint(1000, 9999)))

            novo_ministerio.save()

            messages.success(request, 'Ministério cadastrado com sucesso.')

            return render(request, 'meus_ministerios.html', {'form': form, })

    return render(request, 'meus_ministerios.html', {'form': form, })
