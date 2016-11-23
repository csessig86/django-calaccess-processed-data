# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0026_auto_20161116_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='propositioncommittee',
            name='committee_filer_id',
            field=models.IntegerField(default=1, help_text='Committee id', verbose_name='committee ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propositioncommittee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
