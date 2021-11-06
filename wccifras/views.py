from django.shortcuts import render, redirect
from .forms import CifraForm
from .models import Cifra
from wcartista.models import Artista


def cifras(request, artista, cifra_id, cifra_nome):
    if cifra_id:
        cifra = Cifra.objects.get(id=cifra_id)

        cifra_exibicao = cifra.cifra.splitlines(True)

        return render(request, 'cifras.html', {'cifra': cifra, 'cifra_exibicao': cifra_exibicao, })

    return render(request, 'cifras.html')


def cadastrar(request):
    cifras_recentes = Cifra.objects.all()

    artistas = Artista.objects.all()

    # PRECISO TRATAR O RETORNO DO DATALIST PARA RECUPERAR O OBJETO ARTISTA E NÃO O NOME / ID
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

            return redirect('index')

    return render(request, 'cadastrar_cifra.html', {'cifras_recentes': cifras_recentes, 'form': form, 'artistas': artistas})
