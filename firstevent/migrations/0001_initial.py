# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='firstevent.Event')),
            ],
        ),
    ]
