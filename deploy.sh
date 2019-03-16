#!/usr/bin/env bash

read -p "Enter GT id: " GTID

echo
echo Copy Frontend Files to /projects/VirtualHost/predictc/html/
echo ------------------
echo

rsync -r -v --delete \
      ./frontend/ \
      "$GTID"@predict2019t3.biosci.gatech.edu:/projects/VirtualHost/predictc/html/

echo
echo ------------------
echo Copy Frontend Files Finished
echo


echo
echo Copy Backend Files to /projects/VirtualHost/predictc/FlaskApp/
echo ------------------
echo

rsync -r -v --delete \
      ./backend/ \
      "$GTID"@predict2019t3.biosci.gatech.edu:/projects/VirtualHost/predictc/FlaskApp/

echo
echo ------------------
echo Copy Backend Files Finished
echo
