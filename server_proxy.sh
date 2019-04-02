#!/usr/bin/env bash

read -p "Enter GTid: " GTID

echo Please open your browser at http://localhost:8864/index.html

ssh -L 8864:localhost:9981 "$GTID"@predict2019t3.biosci.gatech.edu

