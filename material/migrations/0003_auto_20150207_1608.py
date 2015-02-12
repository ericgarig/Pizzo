# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_auto_20150207_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.CharField(default=b'NULL', max_length=255, null=True, blank=True),
        ),
    ]
