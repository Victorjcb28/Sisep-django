# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0018_auto_20171003_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='cargos/'),
        ),
    ]
