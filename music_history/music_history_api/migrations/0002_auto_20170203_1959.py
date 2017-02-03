# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 19:59
from __future__ import unicode_literals

from django.db import migrations
import os
from sys import path
from django.core.management import call_command
from django.core import serializers


def load_fixture(apps, schema_editor):
    # fixture_file = os.path.join(fixture_dir, data2.json)
    call_command('loaddata', 'data2.json', app_label='music_history_api')

def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."
    """
    what does the schema_editor argument change? schema obvs, but more specifically?
    """

    Artist = apps.get_model("music_history_api", "Artist")
    Artist.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('music_history_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
