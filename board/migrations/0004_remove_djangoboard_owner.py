# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_djangoboard_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djangoboard',
            name='owner',
        ),
    ]
