# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bereken', '0004_kosten_regiotoeslag_gas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiotoeslag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jaar', models.CharField(max_length=4)),
                ('regio_1', models.FloatField()),
                ('regio_2', models.FloatField()),
                ('regio_3', models.FloatField()),
                ('regio_4', models.FloatField()),
                ('regio_5', models.FloatField()),
                ('regio_6', models.FloatField()),
                ('regio_7', models.FloatField()),
                ('regio_8', models.FloatField()),
                ('regio_9', models.FloatField()),
                ('regio_10', models.FloatField()),
                ('leverancier', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bereken.Leveranciers')),
            ],
        ),
        migrations.RemoveField(
            model_name='kosten',
            name='regiotoeslag_gas',
        ),
    ]
