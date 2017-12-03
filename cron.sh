#!/usr/bin/env sh

cd /home/pete/src/git/shed-thermostat
. env/bin/activate
python cron.py
