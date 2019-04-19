#!/usr/bin/env bash

## Used on server for running flask in background

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SEARCH_KEY=EFFIIDDLSJIEJBIQOJEFIJWOQ
LOG_FILE=$DIR/server.log

## Kill previous process
ps aux | grep $SEARCH_KEY | awk '{print $2}' | xargs -n 1 kill

cd $DIR
#(cd backend && python3 -m venv venv && ./venv/bin/pip3 install -r requirements.txt)

nohup ./serve.sh $SEARCH_KEY >> $LOG_FILE &

