# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file_type',
            field=models.CharField(default='none', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]
