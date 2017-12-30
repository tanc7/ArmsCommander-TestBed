#!/bin/sh

if sudo cat /sys/class/net/wlan1/operstate | grep -xqFe up
then
	echo "Connected to Target. Autohacking"
	python /usr/local/bin/pexpect_rsf_concept.py >> /home/pi/autorsf.log
else
	echo "No networks detected"
fi

if sudo cat /sys/class/net/wlan0/operstate | grep -xqFe up
then
	echo "Connected to Target."
	python /usr/local/bin/pexpect_rsf_concept.py >> /home/pi/autorsf.log
else
	echo "No networks detected"
fi
