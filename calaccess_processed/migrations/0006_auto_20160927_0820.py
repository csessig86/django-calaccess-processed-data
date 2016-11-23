# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0005_candidate_election'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(blank=True, help_text='Office name', max_length=100, verbose_name='office name')),
                ('office_seat', models.CharField(blank=True, help_text='Office seat number', max_length=3, verbose_name='office seat number')),
                ('election', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calaccess_processed.Election')),
            ],
        ),
        migrations.DeleteModel(
            name='Office',
        ),
        migrations.AddField(
            model_name='candidate',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calaccess_processed.Race'),
        ),
    ]
