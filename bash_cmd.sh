#!/bin/bash
cat /root/.hashcat/hashcat.potfile | awk -F ":" { print | | } | uniq  > /tmp/dumped_passwords.txt
