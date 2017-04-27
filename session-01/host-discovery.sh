#!/usr/bin/env bash

DATE=`date +%Y%m%d`

nmap -sL -iL /data/scans/ips-by-subnet.txt -oN /data/scans/results/host-discovery-$DATE.txt