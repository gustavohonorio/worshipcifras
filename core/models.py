from django.db import models
from stdimage.models import StdImageField
# signals - trata a imagem antes ou depois de inserir na base de dados
from django.db.models import signals
# slug - tecnica para altera o nome dos objetos
from django.template.defaultfilters import slugify


class Base(models.Model):
    status = models.BooleanField('Ativo', default=True)
    op_create = models.DateField('Data da Criação', auto_now_add=True)
    op_update = models.DateField('Data da Modificação', auto_now_add=True)


class KPI(models.Model):
    id = models.BigAutoField(primary_key=True)
    acessos = models.IntegerField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, auto_now_add=True)


class CardDestaque(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.CharField('Descricao', max_length=500)
    link = models.CharField('Link', max_length=300, null=True)
    imagem = StdImageField('Imagem', upload_to='.stdimage_cards_destaque')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.titulo


def card_destaque_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)


signals.pre_save.connect(card_destaque_pre_save, sender=CardDestaque)