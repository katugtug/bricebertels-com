# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtracker', '0003_auto_20161115_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Unit of Measure', max_length=255)),
                ('multiplier', models.FloatField(help_text='x 100g')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='food',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodtracker.Unit'),
        ),
    ]
