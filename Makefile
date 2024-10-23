


.PHONY: run-server

run-server:
	poetry run python3  -m erp.manage runserver 127.0.0.1:8000

.PHONY: install
install:
	poetry install
.PHONY: migrations
migrations:
	poetry run python3 -m erp.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python3 -m erp.manage migrate

.PHONY: superuser
superuser:
	 poetry run python3 -m erp.manage createsuperuser


.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: update
update: install migrate install-pre-commit ;

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose  -f docker-compose.dev.yml up --force-recreate db

export PYTHONPATH=/home/divatech/Desktop/new-erp/backend-/
export PYTHONPATH=./backend-/erp
