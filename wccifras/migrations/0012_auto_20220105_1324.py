# Generated by Django 3.2.8 on 2022-01-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wccifras', '0011_auto_20211114_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cifra',
            name='acordes',
        ),
        migrations.RemoveField(
            model_name='cifra',
            name='letra',
        ),
        migrations.AddField(
            model_name='cifra',
            name='ouvir_agora',
            field=models.TextField(blank=True, null=True),
        ),
    ]
