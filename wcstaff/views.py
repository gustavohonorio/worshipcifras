from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from wcartista.models import Artista
from wccifras.utils.acordes_regras import tag_cifra
from wclogon.models import Usuario, Perfil
from wccifras.models import Cifra
from .forms import ArtistaForm, CifraForm, UsuarioForm


# DEFAULT
@login_required
def staff(request):
    a = Artista.objects.count()
    c = Cifra.objects.count()
    u = Usuario.objects.count()

    c_pendente = len(Cifra.objects.filter(status='P'))

    return render(request, 'staff.html', {'artistas_count': a, 'cifras_count': c, 'usuarios_count': u,
                                          'cifras_pendentes': c_pendente})


# ARTISTAS
@login_required
def artistas(request):
    a = Artista.objects.all()
    return render(request, 'read/r-artistas.html', {'artistas': a})


@login_required
def e_artistas(request, id):
    a = get_object_or_404(Artista, id=id)
    form = ArtistaForm(instance=a)

    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=a)
        if form.is_valid():
            a.save()
            messages.success(request, 'Artista atualizado com sucesso.')
            return redirect('r-artistas')
        else:
            messages.success(request, 'Erro ao atualizar artista.')
            return redirect('r-artistas')
    else:
        return render(request, 'edit/e-artistas.html', {'form': form, 'artista': a})


# CIFRAS
@login_required
def cifras(request, filtro):
    if filtro == 'p':
        c = Cifra.objects.filter(status='P')
    else:
        c = Cifra.objects.all()
    return render(request, 'read/r-cifras.html', {'cifras': c})


@login_required
def e_cifras(request, id):
    a = Artista.objects.all()
    c = get_object_or_404(Cifra, id=id)
    c.cifra = tag_cifra(c.cifra.split())
    c.cifra = ' '.join(c.cifra)
    form = CifraForm(instance=c)

    if request.method == 'POST':
        form = CifraForm(request.POST, instance=c)
        if form.is_valid():
            c.save()
            messages.success(request, 'Cifra atualizada com sucesso.')
            return redirect('r-cifras', filtro='TODAS')

    return render(request, 'edit/e-cifras.html', {'form': form, 'cifra': c, 'artistas': a})


# USUARIOS
@login_required
def usuarios(request):
    u = Usuario.objects.all()
    return render(request, 'read/r-usuarios.html', {'usuarios': u})


@login_required
def e_usuarios(request, id):
    u = get_object_or_404(Usuario, id=id)

    form = UsuarioForm(instance=u)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=u)
        if form.is_valid():
            u.save()
            messages.success(request, 'Usuário atualizado com sucesso.')
            return redirect('r-usuarios',)

    return render(request, 'edit/e-usuarios.html', {'form': form, 'usuario': u, })
