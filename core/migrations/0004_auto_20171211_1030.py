# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171207_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
    ]
