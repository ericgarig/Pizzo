# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_auto_20150207_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cost',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
