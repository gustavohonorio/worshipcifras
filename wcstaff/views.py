from django.shortcuts import render, redirect, get_object_or_404
from wcartista.models import Artista
from wclogon.models import Usuario
from wccifras.models import Cifra
from .forms import ArtistaForm, CifraForm


# DEFAULT
def staff(request):
    a = Artista.objects.count()
    c = Cifra.objects.count()
    u = Usuario.objects.count()

    return render(request, 'staff.html', {'artistas_count': a, 'cifras_count': c, 'usuarios_count': u})


# ARTISTAS
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


# CIFRAS
def cifras(request):
    c = Cifra.objects.all()
    return render(request, 'read/r-cifras.html', {'cifras': c})


# TODO : CRIAR METODO PARA ATUALIZAR A CIFRA E CASO TENHO ALGO PREENCHICO NA PARTE PREMIUM, CRIAR UM REGISTRO DE
#        CIFRA VERIFICADA
def e_cifras(request, id):
    a = Artista.objects.all()
    c = get_object_or_404(Cifra, id=id)
    form = CifraForm(instance=c)

    if request.method == 'POST':
        form = CifraForm(request.POST, instance=c)
        if form.is_valid():
            c.save()
            return redirect('s-cifras')

    return render(request, 'edit/e-cifras.html', {'form': form, 'cifra': c, 'artistas': a})


# USUARIOS
def usuarios(request):
    u = Usuario.objects.all()
    return render(request, 'read/r-usuarios.html', {'usuarios': u})


