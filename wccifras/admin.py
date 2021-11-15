from django.contrib import admin
from .models import Cifra


class CifraAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "wc_artista", "status", "op_user", "op_data")


admin.site.register(Cifra, CifraAdmin)

