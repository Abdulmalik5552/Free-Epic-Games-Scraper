#! /usr/bin/env bash

# Let the DB start
python app/utils/backend_pre_start.py

# Run migrations
alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --reload --port 80