# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-23 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0031_auto_20161122_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropositionSupportOppose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support_oppose', models.CharField(blank=True, choices=[('S', 'Support'), ('O', 'Oppose')], help_text='support or oppose', max_length=1, verbose_name='support or oppose')),
            ],
        ),
        migrations.RemoveField(
            model_name='propositioncommittee',
            name='opposes',
        ),
        migrations.RemoveField(
            model_name='propositioncommittee',
            name='supports',
        ),
        migrations.AddField(
            model_name='propositionsupportoppose',
            name='committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calaccess_processed.PropositionCommittee'),
        ),
        migrations.AddField(
            model_name='propositionsupportoppose',
            name='proposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calaccess_processed.Proposition'),
        ),
        migrations.AddField(
            model_name='propositioncommittee',
            name='propositions',
            field=models.ManyToManyField(through='calaccess_processed.PropositionSupportOppose', to='calaccess_processed.Proposition'),
        ),
    ]
