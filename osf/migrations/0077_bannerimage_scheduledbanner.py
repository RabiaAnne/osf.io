# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import osf.utils.fields
import osf.utils.storage


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0076_action_rename'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=256, unique=True)),
                ('image', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=256)),
                ('start_date', osf.utils.fields.NonNaiveDateTimeField()),
                ('end_date', osf.utils.fields.NonNaiveDateTimeField()),
                ('color', models.CharField(max_length=7)),
                ('license', models.CharField(blank=True, max_length=256, null=True)),
                ('default_photo', models.FileField(storage=osf.utils.storage.BannerImageStorage(), upload_to='')),
                ('default_alt_text', models.TextField()),
                ('mobile_photo', models.FileField(storage=osf.utils.storage.BannerImageStorage(), upload_to='')),
                ('mobile_alt_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'permissions': (('view_scheduledbanner', 'Can view scheduled banner details'),),
            },
        ),
    ]
