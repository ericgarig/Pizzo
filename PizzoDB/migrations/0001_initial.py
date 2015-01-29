# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('hours', models.FloatField(default=8)),
                ('cost_per_day', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
                ('date_birth', models.DateField(null=True)),
                ('date_hire', models.DateField(auto_now=True)),
                ('date_fire', models.DateField(null=True)),
                ('rate_hourly', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('rate_increate_date', models.DateField()),
                ('address_street', models.CharField(max_length=255)),
                ('address_city', models.CharField(max_length=255)),
                ('address_state', models.CharField(max_length=2)),
                ('address_zip', models.CharField(max_length=5)),
                ('phone_cell', models.CharField(max_length=10)),
                ('phone_home', models.CharField(max_length=10)),
                ('is_pancho', models.BooleanField(default=0)),
                ('is_temp_layoff', models.BooleanField(default=0)),
                ('deleted', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('abbr', models.CharField(max_length=5)),
                ('cost', models.DecimalField(max_digits=7, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=8)),
                ('date_start', models.DateField()),
                ('proposed_cost', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_category_id',
            field=models.ForeignKey(to='PizzoDB.Employee_Category', null=True),
            preserve_default=True,
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
