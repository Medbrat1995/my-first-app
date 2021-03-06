# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_model',
            new_name='model',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_number',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_overweight',
        ),
        migrations.AddField(
            model_name='tippermodel',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='number',
            field=models.CharField(default=3, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tippermodel',
            name='model_name',
            field=models.CharField(max_length=20),
        ),
    ]
