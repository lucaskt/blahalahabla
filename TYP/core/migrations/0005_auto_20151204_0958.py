# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151204_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dosage',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AlterField(
            model_name='recurringtreatment',
            name='doctor',
            field=models.ForeignKey(related_name='treatments', to='core.Doctor'),
        ),
        migrations.AlterField(
            model_name='recurringtreatment',
            name='medicine',
            field=models.ForeignKey(related_name='treatments', to='core.Medicine'),
        ),
        migrations.AlterField(
            model_name='recurringtreatment',
            name='patient',
            field=models.ForeignKey(related_name='treatments', to='core.Patient'),
        ),
    ]
