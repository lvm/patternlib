# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0002_pattern_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
