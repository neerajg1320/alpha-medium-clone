build-up:
	docker compose -f local.yml up -d --build --remove-orphans

build:
	docker compose -f local.yml build 

build-helpers:
	docker compose -f helpers.yml build 

build-es:
	docker compose -f helpers.yml build es

search-index:
	docker compose -f local.yml exec api python manage.py search_index --create

populate-index:
	docker compose -f local.yml exec api python manage.py search_index --populate

up:
	docker compose -f local.yml up -d

up-helpers:
	docker compose -f helpers.yml up -d	--remove-orphans

down-helpers:
	docker compose -f helpers.yml down

shell-monitor:
	docker compose -f helpers.yml run monitor bash

up-nginx:
	docker compose -f local.yml up nginx

up-es:
	docker compose -f local.yml up es

up-api:
	docker compose -f local.yml up api

up-postgres:
	docker compose -f local.yml up postgres

shell-api:
	docker compose -f local.yml run api bash

shell-api-container:
	docker exec -it medium-api-1 bash

shell-nginx-container:
	docker exec -it medium-nginx-1 sh


down:
	docker compose -f local.yml down

down-es:
	docker compose -f local.yml down es

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs api

makemigrations:
	docker compose -f local.yml run --rm api sh -c "python manage.py makemigrations"

makemigrations-users:
	docker compose -f local.yml run --rm api sh -c "python manage.py makemigrations users"

migrate:
	docker compose -f local.yml run --rm api sh -c "python manage.py migrate"

collectstatic:
	docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

volume:
	docker volume inspect src_local_postgres_data

connect-db:
	docker compose -f local.yml exec postgres psql --username=neeraj --dbname=authors-live

flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose -f local.yml exec api isort . --diff --skip venv --skip migrations

isort:
	docker compose -f local.yml exec api isort . --skip venv --skip migrations


remove-volumes:
	docker volume rm medium_local_postgres_data medium_local_postgres_data_backups medium_media_volume medium_static_volume

psql:
	docker compose -f helpers.yml run monitor sh -c 'psql -h postgres -U neeraj authors-live'

ping-api:
	docker compose -f helpers.yml run --rm monitor sh -c 'ping api'

check-api:
	docker compose -f helpers.yml run --rm monitor sh -c 'nc -zvw10 api 8000'

check-noserver:
	docker compose -f helpers.yml run --rm monitor sh -c 'nc -zvw10 api 8010'

code-coverage:
	docker compose -f local.yml run --rm api pytest -p no:warnings --cov=. -v

code-coverage-html:
	docker compose -f local.yml run --rm api pytest -p no:warnings --cov=. --cov-report html