brew install redis
brew services start redis
brew services info redis

python -m venv venv
source venv/bin/activate

pip install django celery redis

django-admin startproject celery_tutorial 
cd celery_tutorial

# Terminal-1
python manage.py shell
from celery_tutorial.celery import debug_task
debug_task.delay()

# Terminal-2
celery -A celery_tutorial.celery worker --loglevel=info
