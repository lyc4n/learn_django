# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=300)),
                ('is_done', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(verbose_name='date due_date')),
            ],
        ),
    ]
