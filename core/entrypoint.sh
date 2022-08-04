#!/bin/sh
gunicorn -k uvicorn.workers.UvicornH11Worker -c /navent/core/gunicorn.py main:app
exec "$@"
