# Generated by Django 3.2.8 on 2021-10-26 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wccifras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cifra',
            name='wc_cifra_verificada',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='wccifras.cifraverificada'),
        ),
    ]
