from django.db.models import F
from django.shortcuts import render, redirect
from core.utils.backend import Kpi
from wccifras.models import Cifra
from wclogon.models import Usuario, UsuarioKPI
from .forms import ArtistaForm, ComentarioForm
from .models import Artista, Comentario


def artista(request, id, nome_artista):
    a = Artista.objects.get(id=id)
    generos = a.genero.split(',')
    cancoes = Cifra.objects.filter(wc_artista=a)[:3]

    # EXIBINDO COMENTARIOS
    comentarios = Comentario.objects.filter(wc_artista=a.id)

    # FORMULARIO DE COMENTARIO
    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            novo_comentario = Comentario(wc_artista=a, wc_usuario=Usuario.objects.get(id=request.user.id),
                                         nome=request.user.first_name, comentario=comentario)
            novo_comentario.save()

            # ATUALIZANDO KPI USUARIO x ENVIO DE COMENTARIOS
            Kpi.incrementar_usuarios(request.user.id, 4)

            return render(request, 'artista.html', {'artista': a, 'generos': generos, 'cancoes': cancoes,
                                                    'comentarios': comentarios})

    return render(request, 'artista.html', {'artista': a, 'generos': generos, 'cancoes': cancoes, 'form': form,
                                            'comentarios': comentarios})


def cadastrar(request):
    form = ArtistaForm()

    artistas_similares = Artista.objects.all()

    if request.method == 'POST':
        form = ArtistaForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            genero = form.cleaned_data['genero']

            novo_artista = Artista(nome=nome, genero=genero)
            novo_artista.save()

            # ATUALIZANDO KPI USUARIO x ENVIO DE ARTISTAS
            Kpi.incrementar_usuarios(request.user.id, 3)

            return redirect('index')

    return render(request, 'cadastrar_artista.html', {'artistas_similares': artistas_similares, 'form': form})
