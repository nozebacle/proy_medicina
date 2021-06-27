import os 
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicina.settings") 
django.setup()
#from rubricas.models import MyModel

from django.core.management import call_command

call_command('dumpdata', '--output=datadump.json')
