# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0009_auto_20180605_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companys.Album'),
        ),
    ]
