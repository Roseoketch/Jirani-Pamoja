# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_auto_20180528_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
