# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151204_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurringtreatment',
            name='start_time',
        ),
    ]
