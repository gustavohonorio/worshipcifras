from wclogon.models import Usuario


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
