# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djmail', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at'], 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterField(
            model_name='message',
            name='priority',
            field=models.SmallIntegerField(choices=[(20, 'Low'), (50, 'Standard')], default=50),
        ),
    ]
