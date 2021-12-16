from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Usuario, UsuarioKPI
from .forms import UsuarioForm, MeuPerfilForm


def register(request):
    form = UsuarioForm()

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                raise ValueError('Confirme a sua senha, e repita igual para ambos campos.')

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            nascimento = form.cleaned_data['nascimento']
            celular = form.cleaned_data['celular']
            email = form.cleaned_data['email']
            password = make_password(password=form.cleaned_data['password'], salt=None, hasher='pbkdf2_sha256')
            novo_usuario = Usuario(username=email, first_name=first_name, last_name=last_name, nascimento=nascimento,
                                   celular=celular, email=email, password=password)

            novo_usuario.save()

            # Criando indice para a tabela KPI dos usuários
            novo_kpi = UsuarioKPI(wc_usuario=novo_usuario)

            novo_kpi.save()

            # TODO : ESTA CHAMANDO DE LOGIN ESTA DANDO ERRO - 'AnonymousUser' object has no attribute '_meta'
            # user = authenticate(username=novo_usuario.email, password=novo_usuario.password)
            # login(request, user)

            return redirect('index')

    return render(request, 'register.html', {'form': form})


def meu_perfil(request):
    u = get_object_or_404(Usuario, id=request.user.id)
    form = MeuPerfilForm(instance=u)

    if request.method == 'POST':
        form = MeuPerfilForm(request.POST, instance=u)
        if form.is_valid():
            u.save()
            return redirect('meu-perfil')
        else:
            # TODO : TRATAR MENSAGEM DE ERRO CASO O FORMULARIO NAO SEJA VALIDO
            return redirect('meu-perfil')
    else:
        return render(request, 'meu_perfil.html', {'form': form})
