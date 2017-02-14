# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('section', models.PositiveIntegerField()),
                ('slots', models.PositiveIntegerField()),
                ('course', models.ForeignKey(to='course.Course')),
            ],
        ),
    ]
