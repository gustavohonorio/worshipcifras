from django.db import models
# CRIANDO MODELO PERSONALIZADO DE USUARIOS
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Criando o gerenciador do modelo customizado
class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório.')
        # normalize vai formatar o email para deixar valido e padronizado (ex. tudo minusculo)
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user(email, password, **extra_fields)


class Perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    perfil = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    vigencia = models.DateTimeField(auto_now_add=True)
    op_user = models.TextField(default='wcadmin', null=True)
    op_tipo = models.TextField(default='I', null=True)
    op_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.perfil


class Usuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    nascimento = models.DateField()
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'celular']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    objects = UsuarioManager()


class Vigencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    wc_user = models.ForeignKey(Usuario, on_delete=models.CASCADE,default=1)
    wc_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='+', default=1)
    vigencia = models.DateTimeField(auto_now_add=True)
    op_user = models.TextField(default='wcadmin', null=True)
    op_tipo = models.TextField(default='I', null=True)
    op_data = models.DateTimeField(auto_now_add=True)


class CifraKPI(models.Model):
    id = models.BigAutoField(primary_key=True)
    wc_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acessos = models.IntegerField(blank=True, null=True)
    envio_cifras = models.IntegerField(blank=True, null=True)
    envio_artistas = models.IntegerField(blank=True, null=True)
    envio_comentario = models.IntegerField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, auto_now_add=True)
