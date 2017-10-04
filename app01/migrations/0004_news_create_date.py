# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_remove_news_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
