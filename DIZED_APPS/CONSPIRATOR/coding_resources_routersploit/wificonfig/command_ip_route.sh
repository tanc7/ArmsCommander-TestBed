#ip route add 192.168.1.0/24 dev eth1
ip route add REDACTED_SUBNET.0/24 dev eth1
ip route add 192.168.1.0/24 dev eth1
ip route add 192.168.0.0/16 dev eth1
# ip route add 192.168.0.0/16 dev eth1
echo "########## IP ROUTE LIST ###########" >> /root/Desktop/nmap_error_log.log
ip route list  |& tee -a /root/Desktop/nmap_error_log.log &
echo "########## IP ROUTE SHOW ###########" >> /root/Desktop/nmap_error_log.log
ip route show  |& tee -a /root/Desktop/nmap_error_log.log &
