# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0005_examen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='p1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p10',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p7',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p8',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='p9',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]