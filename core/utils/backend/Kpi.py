from django.db.models import F

from wcartista.models import ArtistaKPI, Artista
from wclogon.models import UsuarioKPI, Usuario

# VARIAVEIS AUXILIARES
add = 1


def incrementar_usuarios(id_usuario, valor):
    if valor == 1:
        UsuarioKPI.objects.filter(wc_usuario_id=Usuario.objects.get(id=id_usuario)).update(
            acessos=F('acessos') + add)
    elif valor == 2:
        UsuarioKPI.objects.filter(wc_usuario_id=Usuario.objects.get(id=id_usuario)).update(
            envio_cifras=F('envio_cifras') + add)
    elif valor == 3:
        UsuarioKPI.objects.filter(wc_usuario_id=Usuario.objects.get(id=id_usuario)).update(
            envio_artistas=F('envio_artistas') + add)
    else:
        UsuarioKPI.objects.filter(wc_usuario_id=Usuario.objects.get(id=id_usuario)).update(
            envio_comentario=F('envio_comentario') + add)


def incrementar_artistas(id_artista, valor):
    if valor == 1:
        ArtistaKPI.objects.filter(wc_artista=Artista.objects.get(id=id_artista)).update(
            acessos=F('acessos') + add)
    elif valor == 2:
        ArtistaKPI.objects.filter(wc_artista=Artista.objects.get(id=id_artista)).update(
            curtidas=F('curtidas') + add)
    elif valor == 3:
        ArtistaKPI.objects.filter(wc_artista=Artista.objects.get(id=id_artista)).update(
            comentarios=F('comentarios') + add)
