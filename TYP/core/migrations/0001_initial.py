# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('tag', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OneOffTreatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(to='core.Doctor')),
                ('medicine', models.ForeignKey(to='core.Medicine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_key', models.CharField(unique=True, max_length=255)),
                ('first_name', models.CharField(max_length=128, null=True)),
                ('last_name', models.CharField(max_length=128, null=True)),
                ('birth', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PillTaken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taken_at', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(to='core.Medicine')),
                ('patient', models.ForeignKey(to='core.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='RecurrentTreatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('time_interval', models.IntegerField(default=0)),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('doctor', models.ForeignKey(to='core.Doctor')),
                ('medicine', models.ForeignKey(to='core.Medicine')),
                ('patient', models.ForeignKey(to='core.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='oneofftreatment',
            name='patient',
            field=models.ForeignKey(to='core.Patient'),
        ),
    ]
