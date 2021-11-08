# Generated by Django 3.2.8 on 2021-11-08 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wcartista', '0003_auto_20211105_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(blank=True, null=True)),
                ('comentario', models.TextField()),
                ('curtidas', models.IntegerField(blank=True, default=0, null=True)),
                ('descurtidas', models.IntegerField(blank=True, default=0, null=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('wc_artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcartista.artista')),
                ('wc_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comentario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistaKPI',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('curtidas', models.IntegerField(blank=True, null=True)),
                ('comentarios', models.IntegerField(blank=True, null=True)),
                ('acessos', models.IntegerField(blank=True, null=True)),
                ('dt_inicio', models.DateField(auto_now_add=True)),
                ('wc_artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcartista.artista')),
            ],
        ),
    ]
