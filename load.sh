#!/bin/bash

if [ -z $1 ]; then
  echo "Usage: load.sh <url>"
  exit 1
fi

# Modify sleeptime for more cpu load
sleeptime=0.23

for i in {1..5000}
do
   curl $1 && echo "" &
   echo "Curled $1 $i times. Sleeping $sleeptime"
   sleep $sleeptime
done
