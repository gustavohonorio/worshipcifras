from django.shortcuts import render, redirect, get_object_or_404
from wcartista.models import Artista
from wclogon.models import Usuario
from wccifras.models import Cifra
from .forms import ArtistaForm


def staff(request):
    a = Artista.objects.count()
    c = Cifra.objects.count()
    u = Usuario.objects.count()

    return render(request, 'staff.html', {'artistas_count': a, 'cifras_count': c, 'usuarios_count': u})


def artistas(request):
    a = Artista.objects.all()
    return render(request, 'read/r-artistas.html', {'artistas': a})


def e_artistas(request, id):
    a = get_object_or_404(Artista, id=id)
    form = ArtistaForm(instance=a)

    # TODO : EXIBIR MENSAGEM DE AVISO CASO NADA SEJA ALTERADO / ALGO SEJA ALTERADO
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=a)
        if form.is_valid():
            a.save()
            return redirect('s-artistas')
        else:
            # TODO : TRATAR MENSAGEM DE ERRO CASO O FORMULARIO NAO SEJA VALIDO
            return redirect('s-artistas')
    else:
        return render(request, 'edit/e-artistas.html', {'form': form, 'artista': a})


def cifras(request):
    c = Cifra.objects.all()
    return render(request, 'read/r-cifras.html', {'cifras': c})


def usuarios(request):
    u = Usuario.objects.all()
    return render(request, 'read/r-usuarios.html', {'usuarios': u})


