# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 01:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_pub',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_pub',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 4, 1, 12, 21, 737497, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 4, 1, 12, 29, 45703, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
