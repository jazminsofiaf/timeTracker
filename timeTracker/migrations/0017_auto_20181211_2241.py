# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-11 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeTracker', '0016_tarea_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
