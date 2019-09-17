from django.db import migrations, transaction, IntegrityError
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from ..models import Mineral

class Migration(migrations.Migration):

    def populate_db(apps, schema_editor):
        #Mineral = apps.get_model('minerals', 'Mineral')
        with open(os.path.join(BASE_DIR, "static/minerals/json/minerals.json")) as jsonfile:
            json_reader = json.load(jsonfile)
            for mineral in json_reader:
                try:
                    with transaction.atomic():
                        Mineral.objects.create(**mineral)
                except IntegrityError:
                    print("integrity error")


    dependencies = [
        ('minerals', '0001_mineral'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]

