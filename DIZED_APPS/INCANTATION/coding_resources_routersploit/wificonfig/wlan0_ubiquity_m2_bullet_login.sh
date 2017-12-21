# NETGEAR
# admin:REDACTED_PW
# M2
# REDACTED_LOGIN:REDACTED_PW

#route all  traffic via 192.168.1.1 gateway connected via wlan0 network interface

#service network-manager restart
# dhclient wlan0

ifconfig dns0 down
route add default gw 192.168.1.1
route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw 192.168.1.1
route add -net 192.168.0.0 netmask 255.255.0.0 gw 192.168.1.1
#        down route del -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw 192.168.1.1
#        down route del -net 192.168.0.0 netmask 255.255.0.0 gw 192.168.1.1

#ip route add 192.168.1.0/24 dev wlan0
ip route add REDACTED_SUBNET.0/24 dev wlan0
# ip route add 192.168.0.0/16 dev wlan0

#service network-manager restart
## dhclient wlan0

# verify newly added route
ip route list &
route -n &
netstat -nr &
ip route show &
arp -av &

# ping M2
ping 192.168.1.1 &
ping 192.168.1.20 &
ping REDACTED_SUBNET.1 &
ping REDACTED_SUBNET.20 &

# attempt to login to all router addresses
# firefox 192.168.1.1 &
# firefox 192.168.1.20 &
# firefox REDACTED_SUBNET.1 &
# firefox REDACTED_SUBNET.20 &

# perma add a route
# nano /etc/network/interfaces

# perma get a IP
#iface wlan0 inet static
#address 192.168.1.2
#netmask 255.255.0.0
#network 192.168.0.0
#broadcast 10.0.255.255
#gateway 192.168.1.1
#dns-nameservers 8.8.8.8
service postgresql start
service metasploit start
msfdb init
msfdb start
firefox REDACTED_SUBNET.20 &
# msfconsole -r /root/Desktop/route_commands_m2/check_routes_msf.rc
