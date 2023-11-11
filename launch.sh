#!/usr/bin/bash

docker run -p 5432:5432 -d pgvgdb
sleep 5s
python3 driver.py