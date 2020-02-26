#!/bin/sh
#Author: Asif Rasheed

COMMAND='python3 /home/pi/RAT.py'
LOGFILE=log.txt

now=`date`
echo "$now: Started \n" >> log.txt
while true ; do
  $COMMAND
  now=`date`
  echo "$now: Exited with status $? \n" >> log.txt 
  echo "Restarting" 
done
