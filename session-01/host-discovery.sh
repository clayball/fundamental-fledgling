#!/usr/bin/env bash

NECTOR_BACKEND='/data/nector'
DATE=$(date +%Y%m%d)

if [ ! -d $NECTOR_BACKEND ]; then
    echo "[Error] ${NECTOR_BACKEND} does not exist. Please create."
    exit 0
else
    nmap -sL -iL ${NECTOR_BACKEND}/subnets.csv -oN ${NECTOR_BACKEND}/host-discovery-$DATE.txt
fi
