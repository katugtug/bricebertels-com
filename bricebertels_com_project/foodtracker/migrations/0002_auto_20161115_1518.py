# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 21:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodtracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Food', max_length=255)),
                ('name2', models.CharField(default='Unknown Food', max_length=255)),
                ('amount', models.FloatField(help_text='Amount is a multiplier of the standard 100g.')),
            ],
        ),
        migrations.CreateModel(
            name='FoodBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fat', models.FloatField()),
                ('protein', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fiber', models.FloatField()),
                ('alcohol', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField(default=24, help_text='Hours of the period, typically 24')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('dishes', models.ManyToManyField(to='foodtracker.Dish')),
                ('foods', models.ManyToManyField(to='foodtracker.Food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='foodbase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base', to='foodtracker.FoodBase'),
        ),
        migrations.AddField(
            model_name='dish',
            name='foods',
            field=models.ManyToManyField(to='foodtracker.Food'),
        ),
    ]
