#!/usr/bin/env bash

set -e
trap 'kill $(jobs -p)' EXIT

#. ./backend/venv/bin/activate
VENV_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/backend/venv
FLASK_BIN=$VENV_PATH/bin/flask

cd backend

FLASK_APP=server.py FLASK_RUN_PORT=9981 \
  $FLASK_BIN run --host=0.0.0.0 &

wait
