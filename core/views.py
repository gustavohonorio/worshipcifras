from django.shortcuts import render, redirect
from wccifras.models import Cifra


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return self.count


def index(request):
    cifras = Cifra.objects.all()

    busca = ['', ]

    if request.GET.get('buscar_n'):
        busca = request.GET.get('buscar_n').split(' - ')

    if busca[0]:
        busca_cifra = Cifra.objects.filter(nome__icontains=busca[0])

        return redirect('cifras_busca', cifra_id=busca_cifra[0].id)

    return render(request, 'index.html', {'top_cifras': cifras, 'top_cifras_count': Counter, 'cifras': cifras})
