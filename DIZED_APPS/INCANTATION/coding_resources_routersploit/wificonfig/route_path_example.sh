route add default gw REDACTED_SUBNET.20
route add -net REDACTED_SUBNET.0 netmask 255.255.255.0 gw REDACTED_SUBNET.20
route add -net 192.168.1.0 netmask 255.255.255.0 gw REDACTED_SUBNET.20
route add -net 10.88.0.0 netmask 255.255.255.0 gw REDACTED_SUBNET.20
route add -net 10.88.205.0 netmask 255.255.255.0 gw REDACTED_SUBNET.20
route add -net 10.2.11.0 netmask 255.255.255.0 gw REDACTED_SUBNET.20

