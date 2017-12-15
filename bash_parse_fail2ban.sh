#!/bin/bash
SHELL=/bin/bash
cd /var/log;egrep -irh "Ban" fail2ban* --color | awk -F "NOTICE" '{ print $2 }' | uniq -c > banned-ips.txt && cat banned-ips.txt | awk '{ print $4 }' | strings >> /tmp/default_target_list.txt
