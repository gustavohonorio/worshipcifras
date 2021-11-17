from django.db.models import F
from django.shortcuts import render, redirect
from .forms import CifraForm, ComentarioForm
from .models import Cifra, Tom, Capotraste, ModoVisualizacao, CifraKPI, Comentario
from wcartista.models import Artista
from wclogon.models import Usuario


def cifras(request, artista, cifra_id, cifra_nome):
    cifra = Cifra.objects.get(id=cifra_id)

    # ESTATICOS
    tom = Tom.objects.all()
    capotraste = Capotraste.objects.all()
    modo = ModoVisualizacao.objects.all()

    # KPI
    kpi = CifraKPI.objects.filter(wc_cifra=cifra)
    if kpi:
        kpi = CifraKPI.objects.get(id=kpi[0].id)

    CifraKPI.objects.filter(wc_cifra=cifra).update(acessos=F('acessos')+1)

    # TRATANDO CIFRA PARA SER EXIBIDA EM TELA
    cifra_exibicao = cifra.cifra.splitlines(True)

    # EXIBINDO COMENTARIOS
    comentarios = Comentario.objects.filter(wc_cifra=cifra.id)

    # FORMULARIO DE COMENTARIO
    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            novo_comentario = Comentario(wc_cifra=cifra, wc_usuario=Usuario.objects.get(id=request.user.id),
                                         nome=request.user.first_name, comentario=comentario)
            novo_comentario.save()
            return render(request, 'cifras.html',
                          {'cifra': cifra, 'cifra_exibicao': cifra_exibicao, 'form': form, 'tom': tom,
                           'capotraste': capotraste, 'modo': modo, 'kpi': kpi,
                           'comentarios': comentarios})

    return render(request, 'cifras.html', {'cifra': cifra, 'cifra_exibicao': cifra_exibicao, 'form': form, 'tom': tom,
                                           'capotraste': capotraste, 'modo': modo, 'kpi': kpi,
                                           'comentarios': comentarios})


def cadastrar(request):
    cifras_recentes = Cifra.objects.all()

    artistas = Artista.objects.all()

    form = CifraForm()

    if request.method == 'POST':
        form = CifraForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            wc_artista = Artista.objects.filter(nome=form.cleaned_data['wc_artista'])[:1]
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

            # Criando indice na tabela de KPI's
            novo_kpi_cifra = CifraKPI(wc_cifra=nova_cifra, curtidas=0, acessos=0)

            novo_kpi_cifra.save()

            return redirect('index')

    return render(request, 'cadastrar_cifra.html', {'cifras_recentes': cifras_recentes, 'form': form, 'artistas': artistas})
