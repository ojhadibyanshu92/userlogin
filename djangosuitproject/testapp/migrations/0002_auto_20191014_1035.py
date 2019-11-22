# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-10-14 05:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='showcase',
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='showcase',
        ),
        migrations.RemoveField(
            model_name='showcase',
            name='country',
        ),
        migrations.RemoveField(
            model_name='showcase',
            name='country2',
        ),
        migrations.RemoveField(
            model_name='showcase',
            name='raw_id_field',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Showcase',
        ),
    ]
