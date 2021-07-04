from __future__ import absolute_import
import os
from celery import Celery
from celery import shared_task
from django.conf import settings
import requests
import json 
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@shared_task
def debug_task(urllink,catagory,value):
    response = requests.get(str(url))
    data=response.json()
    output_dict = [x for x in data if x[str(catagory)] == value]
    return json.dumps(output_dict)