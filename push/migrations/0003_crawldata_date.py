# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 15:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0002_auto_20160919_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawldata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 20, 0, 39, 26, 589597)),
        ),
    ]
