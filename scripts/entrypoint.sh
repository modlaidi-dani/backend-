#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python3  -m erp.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

exec poetry run daphne erp.core.asgi:application -p 8000 -b 0.0.0.0 //TODO Fix this when we are in productions
