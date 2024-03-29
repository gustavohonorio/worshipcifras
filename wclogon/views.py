from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import resolve

from wcstaff.forms import ReportErroForm
from wcstaff.models import ReportErro
from .models import Usuario, UsuarioKPI, EsqueciSenha
from .forms import UsuarioForm, MeuPerfilForm, RedefinirSenhaForm, send_email_esqueci_senha
from .utils import user_functions

# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import UsuarioSerializer


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
                    novo_usuario = Usuario(username=email, first_name=first_name, last_name=last_name,
                                           nascimento=nascimento,
                                           celular=celular, email=email, password=password)

                    novo_usuario.save()

                    # Criando indice para a tabela KPI dos usuários
                    novo_kpi = UsuarioKPI(wc_usuario=novo_usuario)

                    novo_kpi.save()

                    login(request, novo_usuario)

                    messages.success(request,
                                     'Ual, estamos felizes em te-lo conosco, seja bem vindo ao Worship Cifras. '
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


def redefinir_senha(request):
    u = get_object_or_404(Usuario, id=request.user.id)
    form = RedefinirSenhaForm(instance=u)

    form_report = ReportErroForm()

    if request.method == 'POST':
        if 'report' in request.POST:
            form_report = ReportErroForm(request.POST)
            if form_report.is_valid():
                nome_usuario = request.user.first_name + ' ' + request.user.last_name
                email_usuario = request.user.email
                celular_usuario = request.user.celular
                origem_erro = 'WCLogon - Redefinir Senha'
                detalhes_erro = 'redefinir_senha'
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
            form = RedefinirSenhaForm(request.POST, instance=u)
            if form.is_valid():
                if request.user.check_password(form.cleaned_data['old_password']):
                    if form.cleaned_data['new_password'] == form.cleaned_data['confirm_password']:
                        nome_aux = u.first_name
                        email_aux = u.email

                        u.password = make_password(password=form.cleaned_data['new_password'], salt=None,
                                                   hasher='pbkdf2_sha256')
                        u.save()

                        messages.success(request, 'Senha atualizada! Entre novamente com a nova senha.')

                        form.send_email(nome=nome_aux, email=email_aux)

                        return redirect('index')
                    else:
                        messages.error(request, 'Ops, as novas senhas não conferem. Por gentileza, valide se as senhas '
                                                'estão iguais.')
                        return redirect('redefinir-senha')
                else:
                    messages.error(request, 'Ops, a sua senha atual não é esta. Por gentileza, digite a senha '
                                            'atual correta.')
                    return redirect('redefinir-senha')
            else:
                for campo in form:
                    if campo.errors:
                        messages.error(request, campo.errors)
                        break
    else:
        return render(request, 'redefinir_senha.html', {'form': form, 'formReport': form_report, })
    return render(request, 'redefinir_senha.html', {'form': form, 'formReport': form_report, })


def esqueci_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email_n')
        if email != '':
            if user_functions.usuario_existe(email):
                key = user_functions.key_generator()

                es = EsqueciSenha(wc_usuario=user_functions.usuario(email), key=key)

                es.save()

                send_email_esqueci_senha(email, key)

                messages.success(request, 'Enviamos um e-mail para a redefinição de sua senha, o seu código terá '
                                          'validade de 24 horas.')
                # return redirect('index')
            else:
                messages.error(request, 'Ops, este e-mail não existe em nossa comunidade. Verifique se digitou '
                                        'corretamente.')
                return redirect('esqueci-senha')

    return render(request, 'esqueci_senha.html', )


def nova_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email_n')
        if email != '':
            if user_functions.usuario_existe(email):
                v = user_functions.key_validade(email)
                if v == 0:
                    messages.info(request, 'Ops, você não solicitou uma redefinição de senha.')
                    return redirect('nova-senha')
                elif v == 1:
                    messages.error(request, 'Ops, o seu código expirou, solicite um novo codigo.')
                    return redirect('esqueci-senha')
                else:
                    key = user_functions.get_key(email)
                    key_in = request.POST.get('key_n')

                    if str(key) == str(key_in):
                        pass_in = request.POST.get('pass_n')
                        passc_in = request.POST.get('passc_n')
                        if pass_in == passc_in:
                            u = get_object_or_404(Usuario, id=user_functions.usuario_id(email))

                            u.password = make_password(password=pass_in, salt=None, hasher='pbkdf2_sha256')

                            u.save()

                            messages.success(request, 'Senha atualizada! Entre com a nova senha.')

                            return redirect('index')
                        else:
                            messages.error(request, 'Ops, as senhas não são iguais, por favor, valide e tente '
                                                    'novamente.')
                    else:
                        messages.error(request, 'Ops, o código esta errado, por favor, valide e tente novamente.')
            else:
                messages.error(request, 'Ops, este e-mail não existe em nossa comunidade. Verifique se digitou '
                                        'corretamente.')
                return redirect('nova-senha')

    return render(request, 'nova_senha.html')


"""
MANEIRA 1 DE FAZER A API

class UsuarioAPI(APIView):
    def get(self, request):
        users = Usuario.objects.all()
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""

"""
MANEIRA 1 DE FAZER A API

class UsuariosAPI(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

"""


# DRF
class UsuarioAPI(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
