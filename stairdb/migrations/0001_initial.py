# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 03:25
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('thumbnail', models.ImageField(blank=True, max_length=500, null=True, upload_to='photos')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Stair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stairid', models.IntegerField()),
                ('name', models.CharField(default='N/A', max_length=100, null=True)),
                ('type', models.CharField(choices=[('Alley Stairs', 'Alley Stairs'), ('Building Access', 'Building Access'), ('Country Park Stairs', 'Country Park Stairs'), ('Curb Stairs', 'Curb Stairs'), ('Elevated Walkway', 'Elevated Walkway'), ('Escalator', 'Escalator'), ('Footpath', 'Footpath'), ('Maintenance Stairs', 'Maintenance Stairs'), ('Pier Stairs', 'Pier Stairs'), ('Park Stairs', 'Park Stairs'), ('Plaza Stairs', 'Plaza Stairs'), ('Street Stairs', 'Street Stairs'), ('Subway', 'Subway')], max_length=25, null=True)),
                ('location', models.CharField(default='N/A', max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
                ('coords_x', models.FloatField(editable=False, null=True)),
                ('coords_y', models.FloatField(editable=False, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='stairid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stairdb.Stair'),
        ),
    ]
