# Generated by Django 2.2.7 on 2019-12-02 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favoritos', '0002_auto_20191202_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorito',
            name='nombre',
        ),
    ]
