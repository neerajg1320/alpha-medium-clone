build:
	docker compose -f local.yml build 

build-helpers:
	docker compose -f helpers.yml build 

up:
	docker compose -f local.yml up -d

up-helpers:
	docker compose -f helpers.yml up -d	--remove-orphans

up-api:
	docker compose -f local.yml up api

up-postgres:
	docker compose -f local.yml up postgres

shell-api:
	docker compose -f local.yml run api bash

shell-api-container:
	docker exec -it project-api-1 bash

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs api

makemigrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

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

check-api:
	docker compose -f helpers.yml run --rm monitor sh -c 'nc -zvw10 192.168.48.4 8000'

check-noserver:
	docker compose -f helpers.yml run --rm monitor sh -c 'nc -zvw10 192.168.48.4 8010'