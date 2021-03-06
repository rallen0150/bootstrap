# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('position', models.CharField(max_length=2)),
                ('player_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Team')),
            ],
        ),
    ]
