#!/bin/sh

DATE=$(date)
#SPEED=$(speedtest -f csv --output-header)
SPEED=$(speedtest -f csv)

echo "\"${DATE}\",${SPEED}"
