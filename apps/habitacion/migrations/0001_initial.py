# Generated by Django 3.1.7 on 2021-03-22 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5)),
                ('estado', models.CharField(max_length=50)),
                ('costo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=80)),
                ('Tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.tipohabitacion')),
            ],
        ),
    ]
