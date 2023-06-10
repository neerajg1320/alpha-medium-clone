django-admin startproject authors_api .

python -c "import secrets; print(secrets.token_urlsafe(38))"

python manage.py startapp users
python manage.py startapp profiles
python manage.py startapp common

# Modify the app.py in the above created apps users, profiles, common
# Move the apps users, profiles, common into core_apps

python manage.py runserver

# Setup logging in base.py

# Setup database once logging is verified 

# Setup Docker with django
mkdir docker && cd docker
mkdir local && cd local
mkdir django && cd django

# We will do multistage build

# Create the env variables

# To check docker compose 
docker compose -f local.yml config

# To build images and run containers.
docker compose -f local.yml up --build -d --remove-orphans