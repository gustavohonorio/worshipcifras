import datetime
import random

from wclogon.models import Usuario, EsqueciSenha


#  VALIDA SE USUARIO EXISTE NA BASE
def usuario_existe(email):
    if Usuario.objects.filter(email=email)[:1]:
        return True
    else:
        return False


def usuario_id(email):
    user = Usuario.objects.filter(email=email)[:1]
    if user:
        return user[0].id
    else:
        return 0


def usuario(email):
    user = Usuario.objects.filter(email=email)[:1]
    if user:
        return user[0]
    else:
        return 0


# GERA A CHAVE PARA REDEFINIR A SENHA, NO ESQUECI SENHA
def key_generator():
    return 'W' + str(random.randint(1000, 9999)) + 'C'


def get_key(email):
    key = EsqueciSenha.objects.filter(wc_usuario=usuario(email))[:1]
    if key:
        return key[0].key


# VERIFICA SE A CHAVE DE REDEFINIÇÃO DE SENHA DO USUÁRIO É VÁLIDO
def key_validade(email):
    validade = EsqueciSenha.objects.filter(wc_usuario=usuario(email))[:1]
    if validade:
        r = validade[0].validade - datetime.datetime.now().date()
        if str(r).startswith('-'):
            return 1
        else:
            return 2
    else:
        return 0
