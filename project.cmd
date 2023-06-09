django-admin startproject authors_api .

python -c "import secrets; print(secrets.token_urlsafe(38))"

python manage.py startapp users
python manage.py startapp profiles
python manage.py startapp common

# Modify the app.py in the above created apps users, profiles, common
# Move the apps users, profiles, common into core_apps

python manage.py runserver