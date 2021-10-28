from django.shortcuts import render, redirect
from .forms import CifraForm


def cifras(request):
    return render(request, 'cifras.html')


def cadastrar(request):
    form = CifraForm(request.POST or None)

    if form.is_valid():
        form.save()
        redirect('cadastrar_cifra')

    return render(request, 'cadastrar.html')
