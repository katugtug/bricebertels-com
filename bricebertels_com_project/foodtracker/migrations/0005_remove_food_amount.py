# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0004_auto_20161117_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='amount',
        ),
    ]