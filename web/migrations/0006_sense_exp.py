# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_align_all_example_all_sense_all'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sense_exp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_wd', models.TextField()),
                ('ch_wd', models.TextField()),
                ('pos', models.TextField()),
                ('location', models.TextField()),
                ('number', models.TextField()),
                ('example', models.TextField()),
            ],
        ),
    ]
