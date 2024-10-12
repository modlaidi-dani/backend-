.PHONY: run-server

run-server:
	poetry run python erp/manage.py runserver 127.0.0.1:8000

.PHONY: install
install:
	poetry install
.PHONY: migrations
migrations:
	poetry run python -m erp/manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python -m erp/manage.py migrate
.PHONY: superuser
superuser:
	 poetry run python -m erp/manage.py createsuperuser
.PHONY: update
update: install migrate install-pre-commit ;

