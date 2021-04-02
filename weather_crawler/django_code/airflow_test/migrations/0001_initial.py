# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MwTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('weather_time', models.CharField(max_length=20)),
                ('dist', models.CharField(max_length=20)),
                ('temp_max', models.CharField(max_length=20, blank=True, null=True)),
                ('temp_min', models.CharField(max_length=20, blank=True, null=True)),
                ('weather_sky', models.CharField(max_length=20, blank=True, null=True)),
                ('rnst', models.CharField(max_length=20, blank=True, null=True)),
            ],
            options={
                'db_table': 'mw_table',
                'managed': False,
            },
        ),
    ]
