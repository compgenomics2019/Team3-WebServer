#!/usr/bin/env bash

set -e
trap 'kill $(jobs -p)' EXIT

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

export LD_LIBRARY_PATH=$SCRIPTPATH/lib:$LD_LIBRARY_PATH

#. ./backend/venv/bin/activate
#VENV_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/backend/venv
#FLASK_BIN=$VENV_PATH/bin/flask

cd backend

FLASK_APP=server.py FLASK_RUN_PORT=9981 \
  flask run --host=0.0.0.0 &

wait
