import os
from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")

app = Celery("project")

app.config_from_object("django.config:settings", namespace="CELERY")
app.autodiscover_task(lambda: settings.INSTALLED_APPS)