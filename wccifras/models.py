from django.db import models
from wcartista.models import Artista


class CifraVerificada(models.Model):
    id = models.BigAutoField(primary_key=True)
    capa = models.TextField(blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    video_aula = models.TextField(blank=True, null=True)
    compositor = models.TextField(blank=True, null=True)
    produtor = models.TextField(blank=True, null=True)
    musicos = models.TextField(blank=True, null=True)
    bpm = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    patrocinada = models.BooleanField(default=False)
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=True, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)


class Cifra(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField(blank=False, null=False)
    wc_artista = models.ForeignKey(Artista, on_delete=models.CASCADE, default=None)
    genero = models.TextField(blank=False, null=False)
    cifra = models.TextField(blank=False, null=False)
    letra = models.TextField(blank=True, null=False)
    acordes = models.TextField(blank=True, null=False)
    tom = models.TextField(blank=False, null=False)
    capotraste = models.TextField(blank=False, null=False, default='Sem capotraste')
    afinacao = models.TextField(blank=False, null=False)
    versao = models.TextField(blank=False, null=False)
    detalhes = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    wc_cifra_verificada = models.ForeignKey(CifraVerificada, on_delete=models.CASCADE, null=True, default=5)
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=True, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.nome
