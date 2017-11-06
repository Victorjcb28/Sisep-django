# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0009_examen_realizado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(blank=True, max_length=200, null=True)),
                ('p2', models.CharField(blank=True, max_length=200, null=True)),
                ('p3', models.CharField(blank=True, max_length=200, null=True)),
                ('p4', models.CharField(blank=True, max_length=200, null=True)),
                ('p5', models.CharField(blank=True, max_length=200, null=True)),
                ('p6', models.CharField(blank=True, max_length=200, null=True)),
                ('p7', models.CharField(blank=True, max_length=200, null=True)),
                ('p8', models.CharField(blank=True, max_length=200, null=True)),
                ('p9', models.CharField(blank=True, max_length=200, null=True)),
                ('p10', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='cargopostualado',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='examen',
            old_name='cargopostulado',
            new_name='cargo',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='postulante',
        ),
        migrations.AlterField(
            model_name='examen',
            name='p1',
            field=models.CharField(blank=True, choices=[('opt0', 'ADMINISTRADOR'), ('opt1', 'SECRETARIA')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postulante.Cargo'),
        ),
    ]
