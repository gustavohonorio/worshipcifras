from django.shortcuts import render, redirect
from wccifras.models import Cifra


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return self.count


def index(request):
    cifras = Cifra.objects.all()
    top_cifras = Cifra.objects.all()[:5]

    busca = ['', ]

    if request.GET.get('buscar_n'):
        busca = request.GET.get('buscar_n').split(' - ')

    if busca[0]:
        busca_cifra = Cifra.objects.filter(nome__icontains=busca[0])
        if busca_cifra:
            return redirect('cifras_busca', artista=str(busca_cifra[0].wc_artista).replace(' ', '-').lower(),
                            cifra_id=busca_cifra[0].id, cifra_nome=str(busca_cifra[0].nome).replace(' ', '-').lower())

    return render(request, 'index.html', {'top_cifras': top_cifras, 'top_cifras_count': Counter, 'cifras': cifras})
