# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PizzoDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('hours', models.FloatField(default=8)),
                ('cost_per_day', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssn', models.CharField(unique=True, max_length=9)),
                ('name_last', models.CharField(max_length=255)),
                ('name_first', models.CharField(max_length=225)),
                ('name_nick', models.CharField(max_length=255)),
                ('date_birth', models.DateField()),
                ('date_hire', models.DateField()),
                ('rate_hourly', models.FloatField()),
                ('rate_Increate_date', models.DateField()),
                ('address_Street', models.CharField(max_length=255)),
                ('address_City', models.CharField(max_length=255)),
                ('address_State', models.CharField(max_length=2)),
                ('address_Zip', models.CharField(max_length=5)),
                ('phone_cell', models.CharField(max_length=10)),
                ('phone_home', models.CharField(max_length=10)),
                ('isPancho', models.BooleanField(default=0)),
                ('isTempLayoff', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee_id',
            field=models.ForeignKey(to='PizzoDB.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='project_id',
            field=models.ForeignKey(to='PizzoDB.Project'),
            preserve_default=True,
        ),
    ]
