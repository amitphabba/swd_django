# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171028_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelps',
            name='psStation',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
