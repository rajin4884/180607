# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0020_pay_my_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='my_sum',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
