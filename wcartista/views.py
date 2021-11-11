from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ArtistaForm
from .models import Artista


def artista(request):
    return render(request, 'artista.html')


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

            return redirect('index')

    return render(request, 'cadastrar_artista.html', {'artistas_similares': artistas_similares, 'form': form})
