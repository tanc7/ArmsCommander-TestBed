cd /root/Desktop/route_commands_m2/ssh_tunnel
# logs into Ubiquiti M2 Bullet in the background and generates a SSH tunnel
echo "DEBUG: Opening SSH Tunneling, enter PASSWORD"
ssh -f -N -D 1080  REDACTED_LOGIN@REDACTED_SUBNET.1
echo "Proxy tunnel opened on 127.0.0.1 PORT 1080"
echo "DEBUG: Sudoing to superuser"
# sudo su
# saves a copy of previous proxychains config
echo "DEBUG: Backing up old proxychains conf if it exists"
cp -r /etc/proxychains.conf /etc/proxychains.conf.save
cat /root/Desktop/route_commands_m2/ssh_tunnel/default_config.conf > /etc/proxychains.conf
# echos a new proxychains file, completely replacing the old config


echo "$default_config" > /etc/proxychains.conf

echo "Copied new proxychains config, default proxy port: 1080"
# tells user how to use proxychains

echo "Setup complete, please precede all of your commands with 'proxychains <cmd>'"

# any additional scripts that I want to run

	# assault mode script. Auto starts besside-ng, comment out to disable
proxychains python /root/Desktop/route_commands_m2/Cylon-Raider-Lite/project_wardriver_xpress/m2_main.py
