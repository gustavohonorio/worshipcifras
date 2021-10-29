from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import UsuarioForm


# nao esta cadastrando o usuario =/
def register(request):
    # print(f'############ funcao register request = {request}')
    form = UsuarioForm()

    if request.method == 'POST':
        # print(f'############ entrou no post - request = {request}')
        form = UsuarioForm(request.POST)
        # print(f'############ form.isvalid = {form.errors}')
        if form.is_valid():
            # print(f'############ form é valido')
            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                raise ValueError('Confirme a sua senha, e repita igual para ambos campos.')
            # print(f'############ senhas validas')

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            nascimento = form.cleaned_data['nascimento']
            celular = form.cleaned_data['celular']
            email = form.cleaned_data['email']
            password = make_password(password=form.cleaned_data['password'], salt=None, hasher='pbkdf2_sha256')
            # print(f'############ senha hash = {password}')
            novo_usuario = Usuario(username=email, first_name=first_name, last_name=last_name, nascimento=nascimento,
                                   celular=celular, email=email, password=password)

            if novo_usuario.save():
                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect('index')

    return render(request, 'register.html', {'form': form})
