# Generated by Django 3.2.8 on 2021-11-06 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wccifras', '0008_auto_20211106_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cifrakpi',
            name='wc_cifra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wccifras.cifra'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('curtidas', models.IntegerField(blank=True, default=0, null=True)),
                ('descurtidas', models.IntegerField(blank=True, default=0, null=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('wc_cifra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wccifras.cifra')),
                ('wc_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]