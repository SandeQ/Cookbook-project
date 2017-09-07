# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-07 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=64)),
                ('Ingredients', models.CharField(max_length=255)),
                ('Text', models.CharField(max_length=1000)),
                ('Preparation_Time', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]