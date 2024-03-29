# Generated by Django 3.2.8 on 2021-10-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('integrantes', models.TextField(blank=True, null=True)),
                ('genero', models.TextField(null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('site', models.TextField(blank=True, null=True)),
                ('facebook', models.TextField(blank=True, null=True)),
                ('twitter', models.TextField(blank=True, null=True)),
                ('youtube', models.TextField(blank=True, null=True)),
                ('spotify', models.TextField(blank=True, null=True)),
                ('outro_link', models.TextField(blank=True, null=True)),
                ('cidade', models.TextField(blank=True, null=True)),
                ('estado', models.TextField(blank=True, null=True)),
                ('pais', models.TextField(blank=True, null=True)),
                ('igreja', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('op_user', models.TextField(blank=True, null=True)),
                ('op_tipo', models.TextField(blank=True, default='I')),
                ('op_data', models.DateTimeField()),
            ],
        ),
    ]
