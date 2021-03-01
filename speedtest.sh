#!/bin/sh

DATE=$(date)
#SPEED=$(speedtest -f csv --output-header)
SPEED=$($HOME/bin/speedtest -f csv)

echo "\"${DATE}\",${SPEED}"
