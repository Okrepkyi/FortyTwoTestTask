# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0011_auto_20160110_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='personmodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
    ]
