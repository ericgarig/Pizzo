# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssn', models.CharField(max_length=9, null=True)),
                ('name_last', models.CharField(max_length=255, null=True)),
                ('name_first', models.CharField(max_length=225, null=True)),
                ('name_nick', models.CharField(max_length=255, null=True)),
                ('date_birth', models.DateField(null=True)),
                ('date_hire', models.DateField(auto_now=True)),
                ('date_fire', models.DateField(null=True)),
                ('rate_hourly', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('date_rate_increase', models.DateField()),
                ('address_street', models.CharField(max_length=255, null=True)),
                ('address_city', models.CharField(max_length=255, null=True)),
                ('address_state', models.CharField(max_length=2, null=True)),
                ('address_zip', models.CharField(max_length=5, null=True)),
                ('phone_cell', models.CharField(max_length=10, null=True)),
                ('phone_home', models.CharField(max_length=10, null=True)),
                ('active', models.BooleanField(default=1)),
                ('pancho', models.BooleanField(default=0)),
                ('daboin', models.BooleanField(default=0)),
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
        migrations.AddField(
            model_name='employee',
            name='employee_category',
            field=models.ForeignKey(to='employee.Employee_Category', null=True),
            preserve_default=True,
        ),
    ]
