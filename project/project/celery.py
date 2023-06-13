import os
from celery import Celery
from django.conf import settings

# TODO: change this in production
print("Setting up the environment var DJANGO_SETTINGS_MODULE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")
print("Env var set")

app = Celery("project")

app.config_from_object("django.config:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)