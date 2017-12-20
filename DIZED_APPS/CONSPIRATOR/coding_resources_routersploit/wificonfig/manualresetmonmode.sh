essid=""
pass=""

killall -9 besside-ng
airmon-ng stop wlan1mon
airmon-ng stop wlan0mon
killall -9 wicd

sudo ip link set wlan1 down
sudo iw link set wlan0 down
sudo iw wlan1 set type nmanaged
sudo iw wlan0 set type managed
sudo ip link set wlan1 up
sudo ip link set wlan0 up

iw dev
service wpa_supplicant restart
dhclient wlan1 up
dhclient wlan0 up

wpa_supplicant -B -i wlan0 $essid $pass
wpa_supplicant -B -i wlan1 $essid $pass
