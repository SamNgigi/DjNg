# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
