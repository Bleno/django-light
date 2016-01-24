# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LBBase',
            fields=[
                ('id_base', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('struct', models.CharField(max_length=120)),
                ('dt_base', models.DateTimeField()),
                ('idx_exp', models.BooleanField()),
                ('idx_exp_url', models.CharField(max_length=120, null=True)),
                ('idx_exp_time', models.IntegerField()),
                ('file_ext', models.BooleanField()),
                ('file_ext_time', models.IntegerField(null=True)),
                ('txt_mapping', models.CharField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'lb_base',
            },
        ),
    ]
