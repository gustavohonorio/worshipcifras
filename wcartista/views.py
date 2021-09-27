from django.shortcuts import render


def artista(request):
    return render(request, 'artista.html')
