# Generated by Django 2.2.7 on 2019-12-05 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarjetas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='miembros',
        ),
    ]
