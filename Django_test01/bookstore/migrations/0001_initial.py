# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-06 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='书名')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='定价')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
