# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20180322_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='txt',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
