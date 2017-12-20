# NETGEAR
# admin:REDACTPW
# M2
# REDACTED_LOGIN:REDACTPW

#route all  traffic via 192.168.1.1 gateway connected via eth0 network interface
ifconfig eth0 up
ifconfig eth0 up
ifconfig eth0 REDACTED_SUBNET.5
service network-manager restart
dhclient eth0

#ifconfig dns0 down
#ifconfig wlan0 down
#ifconfig eth0 up
route add default gw 192.168.1.1
route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw 192.168.1.1
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1

route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw REDACTED_SUBNET.1
route add -net 192.168.1.0 netmask 255.255.255.0 gw REDACTED_SUBNET.1
#        down route del -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw 192.168.1.1
#        down route del -net 192.168.0.0 netmask 255.255.0.0 gw 192.168.1.1

#ip route add 192.168.1.0/24 dev eth0
ip route add REDACTED_SUBNET.0/24 dev eth0
ip route add 192.168.1.0/24 dev eth0
# ip route add 192.168.0.0/16 dev eth0

#service network-manager restart
#dhclient eth0

# verify newly added route
ip route list &
route -n &
netstat -nr &
ip route show &
arp -av &

# # ping M2
# ping 192.168.1.1 &
ping 192.168.1.20 &
# ping REDACTED_SUBNET.1 &
ping REDACTED_SUBNET.20 &

# attempt to login to all router addresses
# firefox 192.168.1.1 &
# firefox 192.168.1.20 &
# firefox REDACTED_SUBNET.1 &
# firefox REDACTED_SUBNET.20 &

# perma add a route
# nano /etc/network/interfaces

# perma get a IP
#iface eth0 inet static
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
