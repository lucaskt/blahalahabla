# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oneofftreatment',
            name='doctor',
            field=models.ForeignKey(related_name='oneoff_treatments', to='core.Doctor'),
        ),
        migrations.AlterField(
            model_name='oneofftreatment',
            name='medicine',
            field=models.ForeignKey(related_name='oneoff_treatments', to='core.Medicine'),
        ),
        migrations.AlterField(
            model_name='oneofftreatment',
            name='patient',
            field=models.ForeignKey(related_name='oneoff_treatments', to='core.Patient'),
        ),
        migrations.AlterField(
            model_name='pilltaken',
            name='medicine',
            field=models.ForeignKey(related_name='pills_taken', to='core.Medicine'),
        ),
        migrations.AlterField(
            model_name='pilltaken',
            name='patient',
            field=models.ForeignKey(related_name='pills_taken', to='core.Patient'),
        ),
        migrations.AlterField(
            model_name='recurrenttreatment',
            name='doctor',
            field=models.ForeignKey(related_name='recurrent_treatments', to='core.Doctor'),
        ),
        migrations.AlterField(
            model_name='recurrenttreatment',
            name='medicine',
            field=models.ForeignKey(related_name='recurrent_treatments', to='core.Medicine'),
        ),
        migrations.AlterField(
            model_name='recurrenttreatment',
            name='patient',
            field=models.ForeignKey(related_name='recurrent_treatments', to='core.Patient'),
        ),
    ]
