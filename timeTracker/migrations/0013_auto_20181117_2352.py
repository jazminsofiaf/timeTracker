# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 23:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeTracker', '0012_auto_20181117_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desarrollador',
            name='horas',
        ),
        migrations.AddField(
            model_name='horas',
            name='desarrollador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timeTracker.Desarrollador'),
        ),
        migrations.AlterField(
            model_name='horas',
            name='tarea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timeTracker.Tarea'),
        ),
    ]
