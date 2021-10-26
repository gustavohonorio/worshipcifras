from django.contrib import admin
from .models import Artista


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nome", "status", "op_data")


admin.site.register(Artista, ArtistaAdmin)



