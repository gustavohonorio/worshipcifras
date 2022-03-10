from random import randint

from django.contrib import messages
from django.shortcuts import render

from wclogon.models import Usuario
from wclogon.utils import user_functions
from .models import Ministerio, MinisterioIntegrantes
from .forms import MinisterioForm, IntegranteForm


# TODO : ADICAO DE INTEGRANTES NO MINISTERIO
def ministerios(request):
    ministerio = Ministerio.objects.filter(owner=request.user.id)
    m_selecionado = ministerio.order_by('op_data')[:1]

    form = MinisterioForm()
    form_integrante = IntegranteForm()

    if request.GET.get('filter'):
        m_selecionado = ministerio.filter(nome__icontains=request.GET.get('filter'))

    integrantes = []

    for i in MinisterioIntegrantes.objects.filter(co_ministerio=m_selecionado[0].id):
        user = Usuario.objects.filter(id=i.co_integrante)
        integrantes.append(user[0].first_name)

    print(integrantes)

    if request.method == 'POST':
        if 'convidar-integrante' in request.POST:
            form_integrante = IntegranteForm(request.POST)
            if form_integrante.is_valid():
                email = form_integrante.cleaned_data['email']

                form_integrante.send_email(email, m_selecionado[0].nome, user_functions.usuario_existe(email))

                messages.success(request, 'Convite enviado com sucesso.')

                return render(request, 'meus_ministerios.html',
                              {'ministerio': ministerio, 'm_selecionado': m_selecionado,
                               'integrantes': integrantes, 'form': form,
                               'form_i': form_integrante})
        else:
            form = MinisterioForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                descricao = form.cleaned_data['descricao']
                genero = form.cleaned_data['genero']

                novo_ministerio = Ministerio(nome=nome, descricao=descricao, genero=genero, owner=request.user.id,
                                             co_invite=str(randint(1000, 9999)))
                novo_ministerio.save()

                messages.success(request, 'Ministério cadastrado com sucesso.')

                return render(request, 'meus_ministerios.html', {'ministerio': ministerio, 'm_selecionado': m_selecionado,
                                                                 'integrantes': integrantes, 'form': form,
                                                                 'form_i': form_integrante})

    return render(request, 'meus_ministerios.html', {'ministerio': ministerio, 'm_selecionado': m_selecionado,
                                                     'integrantes': integrantes, 'form': form,
                                                     'form_i': form_integrante})
