# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0004_auto_20170830_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargopostulado', models.CharField(max_length=200)),
                ('puntuacion', models.CharField(max_length=200)),
                ('p1', models.CharField(max_length=200)),
                ('p2', models.CharField(max_length=200)),
                ('p3', models.CharField(max_length=200)),
                ('p4', models.CharField(max_length=200)),
                ('p5', models.CharField(max_length=200)),
                ('p6', models.CharField(max_length=200)),
                ('p7', models.CharField(max_length=200)),
                ('p8', models.CharField(max_length=200)),
                ('p9', models.CharField(max_length=200)),
                ('p10', models.CharField(max_length=200)),
                ('postulante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postulante.Postulante')),
            ],
        ),
    ]
