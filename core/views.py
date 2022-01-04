from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import resolve

from wccifras.models import Cifra
from wcartista.models import Artista
from wcstaff.forms import ReportErroForm
from wcstaff.models import ReportErro


def index(request):
    if 'term' in request.GET:
        c = Cifra.objects.filter(status__icontains='A', nome__icontains=request.GET.get('term'))[:5]
        a = Artista.objects.filter(status__icontains='A', nome__icontains=request.GET.get('term'))[:5]
        lista = list()
        for cifra in c:
            lista.append(cifra.nome + ' - ' + str(cifra.wc_artista))
        for artista in a:
            lista.append('Buscar ' + artista.nome)
        return JsonResponse(lista, safe=False)

    # artistas = Artista.objects.all()

    top_cifras = Cifra.objects.all()[:5]
    top_artistas = Artista.objects.all()[:5]
    form_report = ReportErroForm()

    if request.GET.get('buscar_n'):
        if "Buscar" in request.GET.get('buscar_n'):
            buscar = request.GET.get('buscar_n').split('Buscar ')
            if buscar[1]:
                buscar_artista = Artista.objects.filter(nome=buscar[1])
                if buscar_artista:
                    return redirect('artista', id=buscar_artista[0].id, nome_artista=str(buscar_artista[0].nome))
        else:
            buscar = request.GET.get('buscar_n').split(' - ')
            if buscar[0]:
                artista_aux = Artista.objects.filter(nome=buscar[1])[:1]
                buscar_cifra = Cifra.objects.filter(nome__icontains=buscar[0], wc_artista=artista_aux)[:1]
                if buscar_cifra:
                    return redirect('cifras_busca',
                                    artista=str(buscar_cifra[0].wc_artista).replace(' ', '-').lower(),
                                    cifra_id=buscar_cifra[0].id,
                                    cifra_nome=str(buscar_cifra[0].nome).replace(' ', '-').lower(),)

    # Reportar um bug
    if request.method == 'POST':
        if 'report' in request.POST:
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'Core - Reportar um bug'
                detalhes_erro = 'footer'
                link_erro = resolve(request.path_info).url_name
                titulo_erro = form_report.cleaned_data['titulo_erro']
                descricao_erro = form_report.cleaned_data['descricao_erro']

                novo_report = ReportErro(nome_usuario=nome_usuario, email_usuario=email_usuario,
                                         celular_usuario=celular_usuario, origem_erro=origem_erro,
                                         detalhes_erro=detalhes_erro, link_erro=link_erro, titulo_erro=titulo_erro,
                                         descricao_erro=descricao_erro)
                novo_report.save()
                messages.success(request, 'Problema reportado. Não se preocupe, nosso time irá analisar o mais rápido'
                                          ' possivél, e daremos um retorno sobre sua notificação. Obrigado'
                                          ' por ajudar a comunidade a ser ainda melhor.')

                return redirect('index')

    return render(request, 'index.html', {'top_cifras': top_cifras, 'top_artistas': top_artistas,
                                          'formReport': form_report, })
