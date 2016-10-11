# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-28 04:04
from __future__ import unicode_literals

import django.db.models.deletion
import osf_models.utils.datetime_aware_jsonfield
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('osf_models', '0002_auto_20160927_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxNodeSettings',
            fields=[
                ('id', models.AutoField(auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('folder_id', models.TextField(blank=True, default=None, null=True)),
                ('folder_name', models.TextField(blank=True, null=True)),
                ('folder_path', models.TextField(blank=True, null=True)),
                ('external_account', models.ForeignKey(blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE, to='osf_models.ExternalAccount')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                    to='osf_models.Node')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoxUserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('oauth_grants', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(blank=True,
                    default=dict)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='boxnodesettings',
            name='user_settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                to='box.BoxUserSettings'),
        ),
    ]
