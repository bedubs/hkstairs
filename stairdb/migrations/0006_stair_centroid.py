# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 00:50
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stairdb', '0005_auto_20170306_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='stair',
            name='centroid',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]