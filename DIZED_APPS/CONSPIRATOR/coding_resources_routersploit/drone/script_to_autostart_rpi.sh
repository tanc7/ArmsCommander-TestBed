#!/bin/bash
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/home/pi:/root/Cylon-Raider-Lite/project_wardriver_xpress/homepidir
export DISPLAY=:0.0

sudo su
# var_date = $(date)
python /home/pi/rpi_custom_main.py &
python /root/Cylon-Raider-Lite/project_wardriver_xpress/homepidir &
# echo "Wardriver Express started at: " + $var_date >> /tmp/wardriver_express.log
# ps aux | grep besside >> /tmp/wardriver_express.log
