#!/bin/sh
SHELL=/bin/sh

PATH=/home/pi:/usr/local/bin:/usr/bin:/sbin:/bin:/usr/sbin

sleep 10
service ssh restart
ifconfig wlan0 REDACTED_SUBNET.50
# /bin/sh /home/pi/add_pi_network.sh
python /home/pi/homepidir/rpi_custom_main.py

route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw REDACTED_SUBNET.20
