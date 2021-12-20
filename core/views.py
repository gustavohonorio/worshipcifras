from django.shortcuts import render, redirect
from wccifras.models import Cifra
from wcartista.models import Artista


def index(request):
    cifras = Cifra.objects.filter(status__icontains='A')
    top_cifras = Cifra.objects.all()[:5]
    artistas = Artista.objects.all()
    top_artistas = Artista.objects.all()[:5]

    if request.GET.get('buscar_n'):
        if "Buscar" in request.GET.get('buscar_n'):
            buscar = request.GET.get('buscar_n').split('Buscar ')
            if buscar[1]:
                buscar_artista = Artista.objects.filter(nome__icontains=buscar[1])
                if buscar_artista:
                    return redirect('artista', id=buscar_artista[0].id, nome_artista=str(buscar_artista[0].nome))
        else:
            buscar = request.GET.get('buscar_n').split(' - ')
            if buscar[0]:
                buscar_cifra = Cifra.objects.filter(nome__icontains=buscar[0])
                if buscar_cifra:
                    return redirect('cifras_busca',
                                    artista=str(buscar_cifra[0].wc_artista).replace(' ', '-').lower(),
                                    cifra_id=buscar_cifra[0].id,
                                    cifra_nome=str(buscar_cifra[0].nome).replace(' ', '-').lower(),)

    return render(request, 'index.html', {'top_cifras': top_cifras, 'top_artistas': top_artistas, 'cifras': cifras,
                                          'artistas': artistas})
