# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-06 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default='1988-10-31'),
        ),
    ]
