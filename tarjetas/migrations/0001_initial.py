# Generated by Django 2.2.7 on 2019-12-05 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miembros', '0001_initial'),
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('posicion', models.IntegerField()),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listas.Lista')),
                ('miembros', models.ManyToManyField(to='miembros.Miembro')),
            ],
        ),
    ]