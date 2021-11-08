from django.db import models
from wclogon.models import Usuario


class Artista(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField(blank=False, null=False)
    integrantes = models.TextField(blank=True, null=True)
    genero = models.TextField(blank=False, null=True)
    descricao = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)
    spotify = models.TextField(blank=True, null=True)
    outro_link = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    igreja = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default='A')
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=False, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.nome


class ArtistaKPI(models.Model):
    id = models.BigAutoField(primary_key=True)
    wc_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    curtidas = models.IntegerField(blank=True, null=True)
    comentarios = models.IntegerField(blank=True, null=True)
    acessos = models.IntegerField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, auto_now_add=True)


class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    wc_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    wc_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='user_comentario')
    nome = models.TextField(blank=True, null=True)
    comentario = models.TextField(blank=False, null=False)
    curtidas = models.IntegerField(blank=True, null=True, default=0)
    descurtidas = models.IntegerField(blank=True, null=True, default=0)
    dt_inclusao = models.DateTimeField(blank=True, auto_now_add=True)
