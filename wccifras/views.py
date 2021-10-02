from django.shortcuts import render


def cifras(request):
    return render(request, 'cifras.html')


def cadastrar(request):
    return render(request, 'cadastrar.html')
