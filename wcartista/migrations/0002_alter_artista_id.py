# Generated by Django 3.2.8 on 2021-10-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcartista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
