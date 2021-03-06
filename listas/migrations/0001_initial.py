# Generated by Django 2.2.7 on 2019-12-03 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tableros', '0002_tablero_dueño'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
                ('posicion', models.IntegerField()),
                ('tablero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableros.Tablero')),
            ],
        ),
    ]
