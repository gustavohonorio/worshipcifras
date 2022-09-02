from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import resolve

from core.utils.backend import Kpi
from wccifras.models import Cifra
from wclogon.models import Usuario
from wcstaff.forms import ReportErroForm
from wcstaff.models import ReportErro
from .forms import ArtistaForm, ComentarioForm
from .models import Artista, Comentario, ArtistaKPI

from rest_framework import viewsets
from .serializers import ArtistaSerializer


def artista(request, id, nome_artista):
    a = Artista.objects.get(id=id)

    if Cifra.objects.filter(wc_artista=a):
        cancoes = Cifra.objects.filter(wc_artista=a)[:5]
    else:
        cancoes = ''

    if a.genero:
        generos = a.genero.split(',')
    else:
        generos = ''

    # EXIBINDO COMENTARIOS
    comentarios = Comentario.objects.filter(wc_artista=a.id)

    # REPORTANDO ERRO NO ARTISTA
    form_report = ReportErroForm()

    # FORMULARIO DE COMENTARIO
    form = ComentarioForm()

    if request.method == 'POST':
        if 'report' in request.POST:
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'WCArtista - Visualizacao de Artista'
                detalhes_erro = 'ID: ' + str(id)
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

                return render(request, 'artista.html', {'artista': a, 'generos': generos, 'cancoes': cancoes,
                                                        'comentarios': comentarios, 'formReport': form_report})
        else:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.cleaned_data['comentario']
                novo_comentario = Comentario(wc_artista=a, wc_usuario=Usuario.objects.get(id=request.user.id),
                                             nome=request.user.first_name, comentario=comentario)
                novo_comentario.save()

                # ATUALIZANDO KPI USUARIO x ENVIO DE COMENTARIOS
                Kpi.incrementar_usuarios(request.user.id, 4)
                # ATUALIZANDO KPI ARTISTA
                Kpi.incrementar_artistas(id, 3)

                return render(request, 'artista.html', {'artista': a, 'generos': generos, 'cancoes': cancoes,
                                                        'comentarios': comentarios, 'formReport': form_report})
    # ATUALIZANDO KPI ARTISTA
    Kpi.incrementar_artistas(id, 1)

    return render(request, 'artista.html', {'artista': a, 'generos': generos, 'cancoes': cancoes, 'form': form,
                                            'comentarios': comentarios, 'formReport': form_report})


@login_required
def cadastrar(request):
    form = ArtistaForm()
    form_report = ReportErroForm()

    artistas_similares = Artista.objects.all()[:5]

    if request.method == 'POST':
        if 'report' in request.POST:
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'WCArtista - Cadastro de Artista'
                detalhes_erro = 'cadastrar'
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

                return redirect('cadastrar_artista')
        else:
            form = ArtistaForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                genero = form.cleaned_data['genero']

                novo_artista = Artista(nome=nome, genero=genero)
                novo_artista.save()

                # CRIAR KPI DOS ARTISTAS
                novo_artista_kpi = ArtistaKPI(wc_artista=novo_artista, curtidas=0, comentarios=0, acessos=0)

                novo_artista_kpi.save()

                # ATUALIZANDO KPI USUARIO x ENVIO DE ARTISTAS
                Kpi.incrementar_usuarios(request.user.id, 3)

                messages.success(request, 'Artista cadastrado com sucesso! Continue contribuindo com a comunidade para '
                                          'concorrer a super prêmios.')

                return redirect('cadastrar_artista')
            else:
                for campo in form:
                    if campo.errors:
                        messages.error(request, campo.errors)
                        break

    return render(request, 'cadastrar_artista.html', {'artistas_similares': artistas_similares, 'form': form,
                                                      'formReport': form_report, })


# DRF
class ArtistaAPI(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
