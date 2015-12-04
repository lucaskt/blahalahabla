# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151204_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='tag',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
