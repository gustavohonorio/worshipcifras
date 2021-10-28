from django.shortcuts import render
from wccifras.models import Cifra


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return self.count


def index(request):
    top_cifras = Cifra.objects.all()

    return render(request, 'index.html', {'top_cifras': top_cifras, 'top_cifras_count': Counter})
