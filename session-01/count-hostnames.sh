#!/usr/bin/env bash

# Pass in the nmap host discovery scan output file.
# Test to ASCII art provided by http://www.patorjk.com/software/taag/

HOSTS_FILE=$1
i=0, total=0

while read hosts; do
    # Read from nmap host discovery scan
    last=${hosts: -1}
    echo "[+] $hosts, $last"
    if [ "$last" == ")" ]; then
        i=$((i + 1))
    fi
    total=$((total + 1))
done < $HOSTS_FILE

unassigned=$((total - i))

if [ "$unassigned" -gt "$i" ]; then
    GIVEBACK=1
else
    GIVEBACK=0
fi

echo " "
echo " "
echo " ▄ .▄      .▄▄ · ▄▄▄▄▄ ▐ ▄  ▄▄▄· • ▌ ▄ ·. ▄▄▄ ..▄▄ · "
echo "██▪▐█▪     ▐█ ▀. •██  •█▌▐█▐█ ▀█ ·██ ▐███▪▀▄.▀·▐█ ▀. "
echo "██▀▐█ ▄█▀▄ ▄▀▀▀█▄ ▐█.▪▐█▐▐▌▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄▄▀▀▀█▄"
echo "██▌▐▀▐█▌.▐▌▐█▄▪▐█ ▐█▌·██▐█▌▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌▐█▄▪▐█"
echo "▀▀▀ · ▀█▄▀▪ ▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀▀ "
echo " "
echo "[*] ================================================="
echo "[*] Summary Details"
echo "[*]   Host names     : $i"
echo "[*]   Unassigned     : $unassigned"
echo "[*]   IPv4 addresses : $total"
echo "[*] ================================================="
if [ "$GIVEBACK" -eq "1" ]; then
    echo " "
    echo "[WOOH!] Call ARIN and give back a few subnet ranges!"
else
    echo " "
fi
