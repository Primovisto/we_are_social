# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171107_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
    ]
