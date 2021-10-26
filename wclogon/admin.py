from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Usuario, Vigencia, Perfil


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfil', 'descricao', 'status', 'vigencia', 'op_user')


admin.site.register(Usuario, auth_admin.UserAdmin)
admin.site.register(Vigencia)
admin.site.register(Perfil, PerfilAdmin)
