from django.db import models


class KPI(models.Model):
    id = models.BigAutoField(primary_key=True)
    acessos = models.IntegerField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, auto_now_add=True)
