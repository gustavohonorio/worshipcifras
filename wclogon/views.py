from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.urls import resolve

from wcstaff.forms import ReportErroForm
from wcstaff.models import ReportErro
from .models import Usuario, UsuarioKPI
from .forms import UsuarioForm, MeuPerfilForm


def register(request):
    form = UsuarioForm()

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if request.POST.get('termos_n') == 'S':
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
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

                    login(request, novo_usuario)

                    messages.success(request, 'Ual, estamos felizes em te-lo conosco, seja bem vindo ao Worship Cifras. '
                                              'Deus abençoe.')

                    form.send_email()

                    return redirect('index')
                else:
                    messages.error(request, 'As senhas não conferem, por favor, valide antes de prosseguir.')
            else:
                for campo in form:
                    if campo.errors:
                        messages.error(request, campo.errors)
                        break
        else:
            messages.error(request, 'Para fazer parte da comunidade, e acessar as funcionalidades,'
                                    ' é necessário aceitar os termos do Worship Cifras.')

    return render(request, 'register.html', {'form': form})


def meu_perfil(request):
    u = get_object_or_404(Usuario, id=request.user.id)
    form = MeuPerfilForm(instance=u)

    form_report = ReportErroForm()

    if request.method == 'POST':
        if 'report' in request.POST:
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'WCLogon - Meu Perfil'
                detalhes_erro = 'meu_perfil'
                link_erro = resolve(request.path_info).url_name
                titulo_erro = form_report.cleaned_data['titulo_erro']
                descricao_erro = form_report.cleaned_data['descricao_erro']

                novo_report = ReportErro(nome_usuario=nome_usuario, email_usuario=email_usuario,
                                         celular_usuario=celular_usuario, origem_erro=origem_erro,
                                         detalhes_erro=detalhes_erro, link_erro=link_erro, titulo_erro=titulo_erro,
                                         descricao_erro=descricao_erro)
                novo_report.save()
                messages.success(request, 'Problema reportado. Não se preocupe, nosso time irá analisar o mais rápido'
                                          ' possivél, e daremos um retorno sobre sua notificação. Obrigado'
                                          ' por ajudar a comunidade a ser ainda melhor.')

                return redirect('meu-perfil')
        else:
            form = MeuPerfilForm(request.POST, instance=u)
            if form.is_valid():
                u.save()
                messages.success(request, 'Perfil atualizado! Continue mantendo o seus dados atualizados.')
                return redirect('meu-perfil')
            else:
                for campo in form:
                    if campo.errors:
                        messages.error(request, campo.errors)
                        break
    else:
        return render(request, 'meu_perfil.html', {'form': form, 'formReport': form_report, })
