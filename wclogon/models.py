import datetime
from django.db import models
# CRIANDO MODELO PERSONALIZADO DE USUARIOS
from django.contrib.auth.models import AbstractUser


class Perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    perfil = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    vigencia = models.DateTimeField(auto_now_add=True)
    op_user = models.TextField(default='wcadmin', null=True)
    op_tipo = models.TextField(default='I', null=True)
    op_data = models.DateTimeField(auto_now_add=True)


class Usuario(AbstractUser):
    nascimento = models.DateTimeField(auto_now_add=True)
    genero = models.TextField(blank=True, null=True)
    celular = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    cristao = models.BooleanField(blank=True, null=True)
    igreja = models.TextField(blank=True, null=True)
    funcao = models.TextField(blank=True, null=True)
    op_user = models.TextField(default='wcadmin', null=True)
    op_tipo = models.TextField(default='I', null=True)
    op_data = models.DateTimeField(auto_now_add=True)
    wc_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=2)


class Vigencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    wc_user = models.ForeignKey(Usuario, on_delete=models.CASCADE,default=1)
    wc_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='+', default=1)
    vigencia = models.DateTimeField(auto_now_add=True)
    op_user = models.TextField(default='wcadmin', null=True)
    op_tipo = models.TextField(default='I', null=True)
    op_data = models.DateTimeField(auto_now_add=True)

