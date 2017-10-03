# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 11:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DRFTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('date_added', models.DateField(default=datetime.datetime(2017, 10, 2, 14, 20, 21, 66904))),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
