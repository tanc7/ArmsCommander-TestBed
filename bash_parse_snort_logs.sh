#!/bin/bash
SHELL=/bin/bash

# cd /var/log;egrep -irh "Ban" fail2ban* --color | awk -F "NOTICE" '{ print $2 }' | uniq -c > banned-ips.txt && cat banned-ips.txt | awk '{ print $4 }' | strings > /tmp/default_target_list.txt
cd /var/log/snort;egrep -irh " -> *.*.*.*" * --color | sort -k 2 | awk -F "->" '{ print $1 $2 }'| awk -F " " '{ print $2 "|" $3 }' | awk -F ":" '{ print $1 }' >> /tmp/default_target_list.txt
