# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_offering'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offering',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='offering',
            old_name='startTime',
            new_name='start_time',
        ),
    ]
