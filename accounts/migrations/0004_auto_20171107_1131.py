# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_subscription_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='stripe_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscription_end',
        ),
    ]
