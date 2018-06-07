# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, verbose_name='회사 이름')),
                ('occ', models.CharField(max_length=50, verbose_name='업무')),
                ('location', models.CharField(max_length=50, verbose_name='주소')),
                ('scale', models.CharField(max_length=50, verbose_name='회사 규모')),
                ('payment', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
