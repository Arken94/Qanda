# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171214_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sender_id',
            field=models.CharField(default='', max_length=2046),
        ),
    ]
