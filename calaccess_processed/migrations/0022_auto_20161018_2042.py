# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0021_auto_20161018_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatescrapedelection',
            old_name='election_id',
            new_name='scraped_id',
        ),
    ]
