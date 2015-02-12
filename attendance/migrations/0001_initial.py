# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PizzoDB', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('hours', models.DecimalField(default=8, max_digits=4, decimal_places=2)),
                ('cost_daily', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, blank=True)),
                ('employee', models.ForeignKey(to='employee.Employee')),
                ('project', models.ForeignKey(to='PizzoDB.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
