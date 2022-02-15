from django.db import models

from wclogon.models import Usuario


class Ministerio(models.Model):
    id = models.BigAutoField(primary_key=True)
    co_invite = models.TextField(blank=False, null=False)
    nome = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=False, null=True)
    genero = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default='A')
    dt_criacao = models.DateTimeField(blank=True, auto_now_add=True)
    integrantes = models.ManyToManyField(Usuario)
    owner = models.TextField(blank=True, null=True)
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=False, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.nome


class MusicasFavoritas(models.Model):
    id = models.BigAutoField(primary_key=True)
    co_ministerio = models.IntegerField(blank=True, null=True)
    co_cifra = models.IntegerField(blank=True, null=True)
    tom = models.TextField(blank=True, null=True)
    capotraste = models.TextField(blank=True, null=True)
    modo = models.TextField(blank=True, null=True)
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=False, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)


class Escala(models.Model):
    id = models.BigAutoField(primary_key=True)
    co_ministerio = models.IntegerField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    genero = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default='A')
    integrantes = models.ManyToManyField(Usuario)
    user_owner = models.TextField(blank=True, null=True)
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=False, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)


class EscalaMusicas(models.Model):
    id = models.BigAutoField(primary_key=True)
    co_escala = models.IntegerField(blank=True, null=True)
    co_cifra = models.IntegerField(blank=True, null=True)
    tom = models.TextField(blank=True, null=True)
    capotraste = models.TextField(blank=True, null=True)
    modo = models.TextField(blank=True, null=True)
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_tipo = models.TextField(blank=True, null=False, default='I')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)
