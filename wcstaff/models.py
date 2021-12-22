from django.db import models


# Tabela de report de erro nas telas, feito pelos usuarios
class ReportErro(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_usuario = models.TextField(blank=True, null=True)
    email_usuario = models.TextField(blank=False, null=True)
    celular_usuario = models.TextField(blank=True, null=True)
    origem_erro = models.TextField(blank=True, null=True)
    detalhes_erro = models.TextField(blank=True, null=True)
    link_erro = models.TextField(blank=True, null=True)
    titulo_erro = models.TextField(blank=True, null=True)
    descricao_erro = models.TextField(blank=True, null=True)
    status_erro = models.TextField(blank=True, null=True, default='A')
    op_user = models.TextField(blank=True, null=True, default='wcadmin')
    op_data = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.titulo_erro
