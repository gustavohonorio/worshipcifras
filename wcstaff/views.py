from django.shortcuts import render
from wcartista.models import Artista
from wclogon.models import Usuario
from wccifras.models import Cifra


def staff(request):
    a = Artista.objects.count()
    c = Cifra.objects.count()
    u = Usuario.objects.count()

    return render(request, 'staff.html', {'artistas_count': a, 'cifras_count': c, 'usuarios_count': u})


def artistas(request):
    a = Artista.objects.all()
    return render(request, 's-artistas.html', {'artistas': a})


def cifras(request):
    c = Cifra.objects.all()
    return render(request, 's-cifras.html', {'cifras': c})


def usuarios(request):
    u = Usuario.objects.all()
    return render(request, 's-usuarios.html', {'usuarios': u})


