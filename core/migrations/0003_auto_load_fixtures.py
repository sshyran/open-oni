# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management import call_command
from django.db import migrations, models


class Migration(migrations.Migration):

    def load_data(apps, schema_editor):
        call_command("loaddata", "awardees.json")
        call_command("loaddata", "countries.json")
        call_command("loaddata", "material_types.json")

    dependencies = [
        ('core', '0002_auto_20160713_1509'),
    ]

    operations = [
      migrations.RunPython(load_data)
    ]
