# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textin', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
