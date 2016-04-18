# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20160418_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchs', to='service.Match')),
                ('video_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.VideoType')),
            ],
            options={
                'ordering': ['video_type'],
            },
        ),
    ]
