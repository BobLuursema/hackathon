# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0006_auto_20171028_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1),
            preserve_default=False,
        ),
    ]
