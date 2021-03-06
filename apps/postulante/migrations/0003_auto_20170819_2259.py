# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0002_postulante_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruccion', models.CharField(max_length=100)),
                ('agraduacion', models.IntegerField()),
                ('contabilidad', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('merito', models.IntegerField()),
                ('curso', models.CharField(max_length=150)),
                ('idioma', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='postulante',
            name='fecha_nacimiento',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='postulante',
            name='sexo',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='domicilio',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='educacion',
            name='postulante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postulante.Postulante'),
        ),
    ]
