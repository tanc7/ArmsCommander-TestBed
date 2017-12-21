#!/bin/sh

killall -9 besside-ng
airmon-ng stop wlan1
airmon-ng stop wlam0

ifconfig wlan1 down
iwconfig wlan1 mode managed
ifconfig wlan1 up

iw wlan1 del
iw wlan0 del

ifconfig wlan0 down
iwconfig wlan0 mode managed
ifconfig wlan0 up

service wpa_supplicant restart
dhclient wlan0
dhclient wlan1

