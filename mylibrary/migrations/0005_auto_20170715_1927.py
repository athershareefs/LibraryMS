# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0004_auto_20170711_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookloans',
            name='date_out',
            field=models.DateField(default=datetime.date.today),
        ),
    ]