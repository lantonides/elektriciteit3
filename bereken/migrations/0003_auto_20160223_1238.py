# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bereken', '0002_kosten_vastrecht'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kosten',
            old_name='vastrecht',
            new_name='vastrecht_elektriciteit',
        ),
        migrations.AddField(
            model_name='kosten',
            name='vastrecht_gas',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
