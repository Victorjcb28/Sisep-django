# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='cedula',
            field=models.IntegerField(default=0),
        ),
    ]
