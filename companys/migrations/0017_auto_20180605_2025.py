# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0016_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companys',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', null=True, unique=True, verbose_name='SLUG'),
        ),
    ]
