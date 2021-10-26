from django.contrib import admin
from .models import Cifra, CifraVerificada


class CifraAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "wc_artista", "wc_cifra_verificada", "status", "op_user", "op_data")


class CifraVerificadaAdmin(admin.ModelAdmin):
    list_display = ("id", "compositor", "produtor", "patrocinada", "op_user", "op_data")


admin.site.register(Cifra, CifraAdmin)
admin.site.register(CifraVerificada, CifraVerificadaAdmin)

