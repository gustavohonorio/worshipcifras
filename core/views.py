from django.shortcuts import render
from wccifras.models import Cifra


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return self.count


def index(request):
    top_cifras = Cifra.objects.all()

    # buscando cifras; preciso alterar para ir para a tela da cifra, mas esta funcionando a busca
    busca = request.GET.get('buscar_n')
    if busca:
        busca_cifra = Cifra.objects.filter(nome__icontains=busca)
        return render(request, 'index.html', {'top_cifras': busca_cifra, 'top_cifras_count': Counter})

    return render(request, 'index.html', {'top_cifras': top_cifras, 'top_cifras_count': Counter})
