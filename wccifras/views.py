from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve

from core.utils.backend import Kpi
from wcstaff.forms import ReportErroForm
from wcstaff.models import ReportErro
from .forms import CifraForm, ComentarioForm
from .models import Cifra, Capotraste, CifraKPI, Comentario
from wcartista.models import Artista
from wclogon.models import Usuario
from .utils import acordes_regras, static_vars
from .utils.acordes_regras import tag_cifra


def cifras(request, artista, cifra_id, cifra_nome, ):
    # TODO : TEMPORARIO : AQUI ESTOU PASSANDO A CIFRA PELO TAG NOVAMENTE, PARA TRATAR OS NOVOS ACORDES QUE TEM SURGIDO
    #        QUANDO ESTABILIZAR A QUESTÃO DOS TONS, É NECESSÁRIO TIRAR ESTE PASSO PARA OTIMIZAR A APLICAÇÃO
    c = get_object_or_404(Cifra, id=cifra_id)
    c.cifra = tag_cifra(c.cifra.split())
    c.cifra = ' '.join(c.cifra)
    c.save()

    cifra = Cifra.objects.get(id=cifra_id)

    # ESTATICOS
    if 'm' in cifra.tom:
        tom = acordes_regras.escalas_menores
    else:
        tom = acordes_regras.escalas_maiores

    capotraste = Capotraste.objects.all()
    modo = static_vars.Vars.modo_choices

    # KPI
    kpi = CifraKPI.objects.filter(wc_cifra=cifra)
    if kpi:
        kpi = CifraKPI.objects.get(id=kpi[0].id)

    CifraKPI.objects.filter(wc_cifra=cifra).update(acessos=F('acessos') + 1)

    # TRATANDO CIFRA PARA SER EXIBIDA EM TELA

    novo_tom = (request.GET.get('tom_n') if request.GET.get('tom_n') else 0)

    cifra_split = cifra.cifra.split()

    if novo_tom:
        novo_tom = novo_tom.replace('Tom original: ', '')
        novo_tom = novo_tom.replace('Tom selecionado: ', '')
        if novo_tom != cifra.tom:
            acordes_regras.transposicao_cifra(cifra_split, cifra.tom, novo_tom)

    modo_default = 'Modo'
    if request.GET.get('modo_n') == 'Cifra':
        modo_default = 'Cifra'
        cifra.cifra = acordes_regras.formatar_cifra(cifra_split)
    elif request.GET.get('modo_n') == 'Letra':
        modo_default = 'Letra'
        cifra.cifra = acordes_regras.formatar_letra(cifra_split)
    else:
        cifra.cifra = acordes_regras.formatar_cifra(cifra_split)

    # EXIBINDO COMENTARIOS
    comentarios = Comentario.objects.filter(wc_cifra=cifra.id)

    form_report = ReportErroForm()

    form = ComentarioForm()
    if request.method == 'POST':
        if 'report' in request.POST:  # FORMULARIO PARA REPORTAR ERRO NA CIFRA
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'WCCifras - Visualizacao de Cifras'
                detalhes_erro = 'ID: ' + str(cifra_id)
                link_erro = resolve(request.path_info).url_name
                titulo_erro = form_report.cleaned_data['titulo_erro']
                descricao_erro = form_report.cleaned_data['descricao_erro']
                novo_report = ReportErro(nome_usuario=nome_usuario, email_usuario=email_usuario,
                                         celular_usuario=celular_usuario, origem_erro=origem_erro,
                                         detalhes_erro=detalhes_erro, link_erro=link_erro, titulo_erro=titulo_erro,
                                         descricao_erro=descricao_erro)
                novo_report.save()
                messages.success(request,
                                 'Problema reportado. Não se preocupe, nosso time irá analisar o mais rápido'
                                 ' possivél, e daremos um retorno sobre sua notificação. Obrigado'
                                 ' por ajudar a comunidade a ser ainda melhor.')
                return render(request, 'cifras.html',
                              {'cifra': cifra, 'form': form, 'tom': tom,
                               'capotraste': capotraste, 'modo': modo, 'modo_default': modo_default, 'kpi': kpi,
                               'comentarios': comentarios, 'artista': artista, 'cifra_nome': cifra_nome,
                               'cifra-id': cifra_id, 'formReport': form_report})
        else:  # FORMULARIO DE COMENTARIO
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.cleaned_data['comentario']
                novo_comentario = Comentario(wc_cifra=cifra, wc_usuario=Usuario.objects.get(id=request.user.id),
                                             nome=request.user.first_name, comentario=comentario)
                novo_comentario.save()

                # ATUALIZANDO KPI USUARIO x ENVIO DE COMENTARIOS
                Kpi.incrementar_usuarios(request.user.id, 4)

                return render(request, 'cifras.html',
                              {'cifra': cifra, 'form': form, 'tom': tom,
                               'capotraste': capotraste, 'modo': modo, 'modo_default': modo_default, 'kpi': kpi,
                               'comentarios': comentarios, 'artista': artista, 'cifra_nome': cifra_nome,
                               'cifra-id': cifra_id, 'formReport': form_report})

    return render(request, 'cifras.html', {'cifra': cifra, 'form': form, 'tom': tom, 'formReport': form_report,
                                           'capotraste': capotraste, 'modo': modo, 'modo_default': modo_default,
                                           'kpi': kpi, 'comentarios': comentarios, 'artista': artista,
                                           'cifra_nome': cifra_nome, 'cifra_id': cifra_id, 'novo_tom': novo_tom})


@login_required
def cadastrar(request):
    if 'term' in request.GET:
        a = Artista.objects.filter(status__icontains='A', nome__icontains=request.GET.get('term'))[:10]
        lista = list()

        for artista in a:
            lista.append(artista.nome)
        return JsonResponse(lista, safe=False)

    cifras_recentes = Cifra.objects.all()[:5]

    artistas = Artista.objects.all()

    form = CifraForm()
    form_report = ReportErroForm()

    if request.method == 'POST':
        if 'report' in request.POST:
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'WCCifras - Cadastro de Cifras'
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

                return redirect('cadastrar_cifra')
        else:
            form = CifraForm(request.POST)
            if form.is_valid():

                nome = form.cleaned_data['nome']
                wc_artista = Artista.objects.filter(status__icontains='A',
                                                    nome__icontains=form.cleaned_data['wc_artista'])[:1]

                if not wc_artista:
                    msg = 'Este artista não existe. Verifique se você digitou corretamente. ' \
                          'Caso seja um novo artista, cadastre-o antes de prosseguir. Ajude a comunidade ' \
                          'e ganhe ainda mais pontos.'

                    messages.warning(request, msg)

                    return render(request, 'cadastrar_cifra.html', {'cifras_recentes': cifras_recentes, 'form': form,
                                                                    'artistas': artistas, 'formReport': form_report, })

                genero = form.cleaned_data['genero']
                cifra = form.cleaned_data['cifra']
                detalhes = form.cleaned_data['detalhes']
                tom = form.cleaned_data['tom']
                capotraste = form.cleaned_data['capotraste']
                afinacao = form.cleaned_data['afinacao']
                versao = form.cleaned_data['versao']

                nova_cifra = Cifra(nome=nome, wc_artista=Artista.objects.get(id=wc_artista[0].id), genero=genero,
                                   cifra=cifra, detalhes=detalhes, tom=tom, capotraste=capotraste, afinacao=afinacao,
                                   versao=versao, )

                nova_cifra.save()

                # CRIANDO INDICE NAS TABELAS KPI's
                novo_kpi_cifra = CifraKPI(wc_cifra=nova_cifra, curtidas=0, acessos=0)

                novo_kpi_cifra.save()

                # DISPARANDO EMAIL PARA O SUPORTE APROVAR
                form.send_email(nova_cifra.id, nova_cifra.nome, wc_artista[0].id)

                # ATUALIZANDO KPI USUARIO x ENVIO DE CIFRAS
                Kpi.incrementar_usuarios(request.user.id, 2)

                messages.success(request, 'Cifra cadastrada com sucesso! Nossa equipe irá analisar e em até 48 horas a '
                                          'sua cifra estará disponível. Continue contribuindo com a comunidade para '
                                          'concorrer a super prêmios.')

                return redirect('index')
            else:
                for campo in form:
                    if campo.errors:
                        messages.error(request, campo.errors)
                        break

    return render(request, 'cadastrar_cifra.html', {'cifras_recentes': cifras_recentes, 'form': form,
                                                    'artistas': artistas, 'formReport': form_report, })
