from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreateForm, UsuarioChangeForm
from .models import Usuario, Vigencia, Perfil


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreateForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ('first_name', 'last_name', 'email', 'celular', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'celular')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfil', 'descricao', 'status', 'vigencia', 'op_user')


admin.site.register(Vigencia)
# admin.site.register(Perfil, PerfilAdmin)
