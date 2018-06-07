# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0005_auto_20180604_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='companys',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=django.utils.timezone.now, help_text='one word for title alias.', unique=True, verbose_name='SLUG'),
            preserve_default=False,
        ),
    ]
