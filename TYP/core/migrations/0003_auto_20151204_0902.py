# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151129_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringTreatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shots', models.IntegerField(default=0)),
                ('time_interval', models.IntegerField(default=0)),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(related_name='recurrent_treatments', to='core.Doctor')),
                ('medicine', models.ForeignKey(related_name='recurrent_treatments', to='core.Medicine')),
                ('patient', models.ForeignKey(related_name='recurrent_treatments', to='core.Patient')),
            ],
        ),
        migrations.RemoveField(
            model_name='oneofftreatment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='oneofftreatment',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='oneofftreatment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='recurrenttreatment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='recurrenttreatment',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='recurrenttreatment',
            name='patient',
        ),
        migrations.DeleteModel(
            name='OneOffTreatment',
        ),
        migrations.DeleteModel(
            name='RecurrentTreatment',
        ),
    ]
