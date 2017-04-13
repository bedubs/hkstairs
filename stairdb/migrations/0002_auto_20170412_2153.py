# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stairdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stair',
            name='location',
            field=models.CharField(default='N/A', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stair',
            name='name',
            field=models.CharField(default='N/A', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stair',
            name='stairid',
            field=models.IntegerField(editable=False),
        ),
    ]