# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0021_auto_20180606_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='my_sum',
            field=models.IntegerField(default=0),
        ),
    ]
