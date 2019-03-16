#!/usr/bin/env bash

set -e
trap 'kill $(jobs -p)' EXIT

echo
echo Start Frontend Server
echo ---------------------------------
echo

cd frontend
python3 -m http.server 4444 > /dev/null &
cd ..
python3 -mwebbrowser http://localhost:4444


echo
echo Activate backend venv environment
echo ---------------------------------
echo

. ./backend/venv/bin/activate


echo
echo Start Backend Server
echo ---------------------------------
echo

cd backend
FLASK_APP=server.py FLASK_ENV=development flask run &

echo
echo ---------------------------------
echo

wait
