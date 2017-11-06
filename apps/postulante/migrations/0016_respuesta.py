# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0015_auto_20170921_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.CharField(blank=True, max_length=200, null=True)),
                ('r2', models.CharField(blank=True, max_length=200, null=True)),
                ('r3', models.CharField(blank=True, max_length=200, null=True)),
                ('r4', models.CharField(blank=True, max_length=200, null=True)),
                ('r5', models.CharField(blank=True, max_length=200, null=True)),
                ('r6', models.CharField(blank=True, max_length=200, null=True)),
                ('r7', models.CharField(blank=True, max_length=200, null=True)),
                ('r8', models.CharField(blank=True, max_length=200, null=True)),
                ('r9', models.CharField(blank=True, max_length=200, null=True)),
                ('r10', models.CharField(blank=True, max_length=200, null=True)),
                ('r11', models.CharField(blank=True, max_length=200, null=True)),
                ('r12', models.CharField(blank=True, max_length=200, null=True)),
                ('r13', models.CharField(blank=True, max_length=200, null=True)),
                ('r14', models.CharField(blank=True, max_length=200, null=True)),
                ('r15', models.CharField(blank=True, max_length=200, null=True)),
                ('r16', models.CharField(blank=True, max_length=200, null=True)),
                ('r17', models.CharField(blank=True, max_length=200, null=True)),
                ('r18', models.CharField(blank=True, max_length=200, null=True)),
                ('r19', models.CharField(blank=True, max_length=200, null=True)),
                ('r20', models.CharField(blank=True, max_length=200, null=True)),
                ('r21', models.CharField(blank=True, max_length=200, null=True)),
                ('r22', models.CharField(blank=True, max_length=200, null=True)),
                ('r23', models.CharField(blank=True, max_length=200, null=True)),
                ('r24', models.CharField(blank=True, max_length=200, null=True)),
                ('r25', models.CharField(blank=True, max_length=200, null=True)),
                ('r26', models.CharField(blank=True, max_length=200, null=True)),
                ('r27', models.CharField(blank=True, max_length=200, null=True)),
                ('r28', models.CharField(blank=True, max_length=200, null=True)),
                ('r29', models.CharField(blank=True, max_length=200, null=True)),
                ('r30', models.CharField(blank=True, max_length=200, null=True)),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postulante.Pregunta')),
            ],
        ),
    ]