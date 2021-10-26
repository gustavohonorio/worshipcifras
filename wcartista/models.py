from django.db import models


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
    status = models.TextField(blank=True, null=True)
    op_user = models.TextField(blank=True, null=True)
    op_tipo = models.TextField(blank=True, null=False, default='I')
    op_data = models.DateTimeField()

    def __str__(self):
        return self.nome

