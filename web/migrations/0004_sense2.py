# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_align_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sense2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_wd', models.TextField()),
                ('ch_wd', models.TextField()),
                ('pos', models.TextField()),
                ('location', models.TextField()),
                ('number', models.TextField()),
                ('sense', models.TextField()),
            ],
        ),
    ]