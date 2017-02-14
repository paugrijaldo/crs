# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('year_level', models.PositiveIntegerField(default=1)),
                ('sex', models.CharField(default=b'Undisclosed', max_length=1, choices=[(b'U', b'Undisclosed'), (b'F', b'Female'), (b'M', b'Male')])),
                ('date_of_birth', models.DateField()),
                ('student_number', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
