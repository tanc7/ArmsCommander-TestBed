# NETGEAR
# admin:REDACTEDPW
# M2
# REDACTED_LOGIN:REDACTEDPW

#route all  traffic via 192.168.1.1 gateway connected via eth1 network interface
#ifconfig eth0 up
#ifconfig eth1 up
#ifconfig eth1 REDACTED_SUBNET.5
service network-manager restart
#dhclient eth1
#dhclient eth1

#ifconfig dns0 down
#ifconfig wlan0 down
#ifconfig eth1 up
route add default 192.168.1.1
route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 192.168.1.1
route add -net 192.168.1.0 netmask 255.255.255.0 192.168.1.1
route add -net 192.0.0.0 netmask 255.0.0.0 192.168.1.1

route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw 192.168.1.1
route add -net REDACTEDTARGETSUBNET.0 netmask 255.255.0.0 192.168.1.1

#route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
#        down route del -net REDACTED_SUBNET.0 netmask 255.255.255.0 192.168.1.1
#        down route del -net REDACTEDTARGETSUBNET.0 netmask 255.255.0.0 192.168.1.1

#ip route add 192.168.1.0/24 dev eth1
ip route add REDACTED_SUBNET.0/24 dev eth1
ip route add 192.168.1.0/24 dev eth1
ip route add REDACTEDTARGETSUBNET.0/16 dev eth1
# ip route add REDACTEDTARGETSUBNET.0/16 dev eth1

#service network-manager restart
#dhclient eth1

# verify newly added route
echo "########## IP ROUTE LIST ###########" >> /root/Desktop/nmap_error_log.log

ip route list  |& tee -a /root/Desktop/nmap_error_log.log &
echo "########## ROUTE -N ###########" >> /root/Desktop/nmap_error_log.log

route -n  |& tee -a /root/Desktop/nmap_error_log.log &
echo "########## NETSTAT -NR ###########" >> /root/Desktop/nmap_error_log.log

netstat -nr  |& tee -a /root/Desktop/nmap_error_log.log &
echo "########## IP ROUTE SHOW ###########" >> /root/Desktop/nmap_error_log.log


ip route show  |& tee -a /root/Desktop/nmap_error_log.log &
echo "########## ARP -AV ###########" >> /root/Desktop/nmap_error_log.log

arp -av  |& tee -a /root/Desktop/nmap_error_log.log &
a


echo "########## NMAP ###########" >> /root/Desktop/nmap_error_log.log
nmap 192.168.1.0/24 |& tee -a /root/Desktop/nmap_error_log.log &
nmap REDACTEDTARGETSUBNET.0/24 |& tee -a /root/Desktop/nmap_error_log.log &
nmap REDACTED_SUBNET.0/24 |& tee -a /root/Desktop/nmap_error_log.log &
nmap REDACTEDTARGETSUBNET.0/16 |& tee -a /root/Desktop/nmap_error_log.log &
#arp -av |& tee -a /root/Desktop/nmap_error_log.log &

GET -E  REDACTED_SUBNET.20 &
GET -E  192.168 10.1 &
GET -E  192.168.1.1 &
GET -E  192.168.1.1 &
GET -E  192.168.1.3 &
GET -E  REDACTED_SUBNET &
GET -E  192.168.1.6 &

msfconsole -r /root/Desktop/route_commands_m2/check_routes_msf.rc
