import os
import sys
import operator
import socket
import time

def reboot():
    print("Rebooting RPI in 10 seconds...")
    time.sleep(10)
    os.system('reboot')
    return

def bash_command(cmd):
    proc = subprocess.call(cmd,shell=True,executable='/bin/bash')
    return proc
def make_threaded_process():
    return
def pip_installs():

    pip_freeze_list = [
        "automationhat==0.0.4",
        "blinker==1.3",
        "blinkt==0.1.0",
        "Cap1xxx==0.1.3",
        "chardet==2.3.0",
        "click==6.6",
        "colorama==0.3.7",
        "cryptography==1.7.1",
        "drumhat==0.0.5",
        "enum34==1.1.6",
        "envirophat==0.0.6",
        "ExplorerHAT==0.4.2",
        "Flask==0.12.1",
        "fourletterphat==0.0.2",
        "gpiozero==1.4.0",
        "idna==2.2",
        "ipaddress==1.0.17",
        "itsdangerous==0.24",
        "Jinja2==2.8",
        "keyring==10.1",
        "keyrings.alt==1.3",
        "lxkeymap==0.1",
        "MarkupSafe==0.23",
        "mcpi==0.1.1",
        "microdotphat==0.1.3",
        "mote==0.0.3",
        "motephat==0.0.2",
        "numpy==1.12.1",
        "oauthlib==2.0.1",
        "phatbeat==0.0.2",
        "pianohat==0.0.5",
        "picamera==1.13",
        "picraft==1.0",
        "piglow==1.2.4",
        "pigpio==1.35",
        "Pillow==4.0.0",
        "pyasn1==0.1.9",
        "pycrypto==2.6.1",
        "pygame==1.9.3",
        "pygobject==3.22.0",
        "pyinotify==0.9.6",
        "PyJWT==1.4.2",
        "pyOpenSSL==16.2.0",
        "pyserial==3.2.1",
        "pyxdg==0.25",
        "rainbowhat==0.0.2",
        "requests==2.12.4",
        "requests-oauthlib==0.7.0",
        "RPi.GPIO==0.6.3",
        "RTIMULib==7.2.1",
        "scrollphat==0.0.7",
        "scrollphathd==1.0.1",
        "SecretStorage==2.3.1",
        "sense-emu==1.0",
        "sense-hat==2.2.0",
        "simplejson==3.10.0",
        "six==1.10.0",
        "skywriter==0.0.7",
        "sn3218==1.2.7",
        "spidev==3.0",
        "touchphat==0.0.1",
        "twython==3.4.0",
        "urllib3==1.19.1",
        "urwid==1.3.1",
        "Werkzeug==0.11.15",
        "wicd==1.7.4"
    ]


    print "INSTALLATION: Python Modules"
    for item in pip_freeze_list:
        print "Now installing: %s" % str(item)
        cmd = "pip install %s" % str(item)
        bash_command(cmd)

    return
def git_installs():
    git_urls_list = ['https://github.com/reverse-shell/routersploit',
        'https://github.com/tanc7/Arms-Commander',
        'https://github.com/tanc7/Cylon-Raider'
    ]

    print "INSTALLATION: GitHub Repositories and subrequirements"
    for item in git_urls_list:
        print "URL: %s" % str(item)
        cmd = "git clone %s" % str(item)
        bash_command(cmd)
    return
def apt_installs():
    apt_reqs = """
    wicd_curses wicd wicd-cli wpagui dotdotpwn aircrack-ng
    """

    cmd = "apt-get update && apt-get install -y {}".format(str(apt_reqs))
    bash_command(cmd)
    return

def install_crontabs(crontab_line):
    default_path_export = "\r\nPATH=/home/pi:/usr/local/bin:/usr/bin:/sbin:/bin:/usr/sbi\r\nSHELL=/bin/bash\r\n"
    crontab_line = """
    @reboot /etc/init.d/ssh restart
    @reboot python {}/rpi_custom_main.py >> /tmp/wardriving.log
    @reboot ifconfig wlan0 up
    @reboot ifconfig wlan1 up
    """.format(
        str('/usr/local/bin')
    )


    return
def change_configuration(original_file_dir, new_file):
    original_file_list = [
        '/etc/sudoers',
        '/boot/cmdline.txt'

    ]
    save_file_dir = str(original_file_dir) + ".save"
    print save_file_dir

    for str(original_file_dir) in original_file_list:
        cmd = """mv "{original_file_dir}" "{save_file_dir}";cp -r "{new_file}" "{original_file_dir}"
        """.format(str(original_file_dir), str(save_file_dir), str(new_file), str(original_file_dir))
        print cmd
        bash_command(cmd)
        print """Moved {0} to {1} as a backup. If you see any problems on reboot, please rename {1} back into {0}
        """.format(
            str(original_file_dir),
            str(new_file)
        )
    return

def sed_edit_line(old_line,new_line,filetoworkon):
    #     template_str = "root	ALL=(ALL:ALL) ALL"
    #     user_priv = """# User privilege specification
    # root	ALL=(ALL:ALL) ALL
    # """
    #     sudo_spec = """# Allow members of group sudo to execute any command
    # %sudo	ALL=(ALL:ALL) ALL"""
    #
    #     toadd = """# Allow members of group sudo to execute any command\r\n{new_sudoer}	ALL=(ALL:ALL) AL
    #     """.format(
    #         str(new_sudoer)
    #     )


    cmd = """sed -i '/"{toreplace}"/c\{toadd}' {filetoworkon}""".format(
        str(old_line),
        str(new_line),
        str(filetoworkon)
    )
    bash_command(cmd)
    return

def give_full_root(user):
    user_str = "{user}:x:{uid}:{gid}:root::{home_dir}:{shell}".format(
        str(user),
        '0',
        '0',
        str(home_dir = '/home/' + user),
        '/bin/bash'
    )

    # change /etc/sudoers
    old_line = "# Allow members of group sudo to execute any command"
    new_line = """# Allow members of group sudo to execute any command\r\n{new_user}	ALL=(ALL:ALL) ALL\n""".format(str(user))
    filetoworkon = "/etc/sudoers"

    old_line = "root:x:0:0:root:/root:/bin/bash"
    new_line = "root:x:0:0:root:/root:/bin/bash\r\n{user_str}\n".format(str(user_str))
    sed_edit_line(str(old_line),str(new_line),str(filetoworkon))

    print("Replaced {old_line} with {new_line}".format(
        str(old_line),
        str(new_line)
    ))
    # change /etc/password file

# sudoers line
    old_line = "# Allow members of group sudo to execute any command"
    new_line = """# Allow members of group sudo to execute any command\r\n{new_user}	ALL=(ALL:ALL) ALL\r\n""".format(str(user))
    filetoworkon = "/etc/sudoers"
    cmd = """echo {user_str} >> /etc/passwd"""
    sed_edit_line(str(old_line),str(new_line),str(filetoworkon))
    print("Replaced {old_line} with {new_line}".format(
        str(old_line),
        str(new_line)
    ))
# user privilege line
    old_line = """# User privilege specification
root	ALL=(ALL:ALL) ALL"""

    new_line = """# User privilege specification
root	ALL=(ALL:ALL) ALL\r\n{new_user}    ALL=(ALL:ALL) ALL\r\n""".format(str(user))
    filetoworkon = "/etc/sudoers"
    sed_edit_line(str(old_line),str(new_line),str(filetoworkon))
    print("Replaced {old_line} with {new_line}".format(
        str(old_line),
        str(new_line)
    ))
    return

def copy_files():
    executables_list = [
        "manualresetmonmode.sh",
        "switch_mon_off.sh",
        "add_car_network.sh",
        "wlan0_ubiquity_m2_bullet_login.sh",
        "Wifiphisher_ap_wlan1_deauth_wlan2.sh",
        "virtualenvwrapper.sh",
        "virtualenvwrapper_lazy.sh",
        "traversal_scan_all.sh",
        "ssh_tunnel_create.sh",
        "routersploit.sh",
        "no_upstream_mana_toolkit_upstream.sh",
        "mount_all_drives_2017.sh",
        "mana_toolkit_upstream.sh",
        "install_script_for_laptop.sh",
        "impersonate_cisco_ap_bridge.sh",
        "IDS_flooder.sh",
        "get_all_pages.sh",
        "get_pub_ip.sh",
        "eth1_ubiquity_m2_bullet_login.sh",
        "eth0_ubiquity_m2_bullet_login.sh",
        "DotDotPwnScript.sh",
        "DN_auto_directory_traversal_exploit.sh",
        "command_ip_route.sh",
        "change_mac.sh",
        "iconfigupdown.sh",
        "ifupscript.sh",
        "rsf.py",
        "action_wpa.sh",
        "functions.sh",
        "ifupdown.sh"
    ]

    for item in executables_list:
        item = "./executables/{}".format(str(item))
        cmd = "chmod 755 {item};cp -r {item} /usr/local/bin".format(str(item))
        bash_command(cmd)
        print("Copied: {item} to /usr/local/bin".format(str(item)))
    #wpa_supplicant -D wext -i wlan0 -c /etc/network/interfaces -dd
    return
def main():

    # generate all the necessary info for rpi connection
    apt_installs()
    git_installs()
    pip_installs()
    copy_files()
    change_configuration(original_file_dir)
    add_root_user()
    give_full_root()
    reboot()
    # move the original conf files to the sideline.
    return
#main()



def scraps_do_not_delete():
    apt_reqs = """
    wicd_curses wicd wicd-cli wpagui
    """
    # /boot/cmdline.txt
    boot_file = """
    net.ifnames=0 dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
    """
    sudoers_file = """
    #includedir /etc/sudoers.d
    root@raspberrypi:/etc# cat sudoers
    #
    # This file MUST be edited with the 'visudo' command as root.
    #
    # Please consider adding local content in /etc/sudoers.d/ instead of
    # directly modifying this file.
    #
    # See the man page for details on how to write a sudoers file.
    #
    Defaults	env_reset
    Defaults	mail_badpass
    Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

    # Host alias specification
    {}   ALL=(ALL:ALL) ALL
    # User alias specification

    # Cmnd alias specification

    # User privilege specification
    root	ALL=(ALL:ALL) ALL

    # Allow members of group sudo to execute any command
    %sudo	ALL=(ALL:ALL) ALL

    # See sudoers(5) for more information on "#include" directives:

    """.format(str(pi_root_user))

    # env variable from env command
    rpi_env = """
    LANG=en_GB.UTF-8
    SUDO_GID=1000
    USERNAME=root
    SUDO_COMMAND=/bin/su
    USER=root
    PWD=/etc/ssh
    HOME=/root
    LC_CTYPE=en_US.UTF-8
    SUDO_USER=pi
    SUDO_UID=1000
    MAIL=/var/mail/root
    SHELL=/bin/bash
    TERM=xterm-256color
    SHLVL=1
    LOGNAME=root
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    _=/usr/bin/env
    OLDPWD=/etc

    """
    # allows autostarts of ssh services
    # /etc/crontab, unique to rpi3
    crontab_line = """
    PATH=/home/pi:/usr/local/bin:/usr/bin:/sbin:/bin:/usr/sbin
    @reboot service ssh restart
    @reboot python /home/pi/{}/rpi_custom_main.py >> /tmp/wardriving.log
    @reboot ifconfig wlan0 up
    @reboot ifconfig wlan1 up
    """.format(str(wardriver_express_path))

    # /etc/wpa_supplicant/wpa_supplicant.conf
    wpa_supplicant_first_line = """
    ctrl_interface=/run/wpa_supplicant
    update_config=1
    """
    wpa_supplicant_net_creds = """

    network={
        ssid="{essid}"
        psk="{psk}"
        key_mgmt=WPA-PSK
    }

    """.format(str(essid),str(psk))
    # to be saved in usr/local/bin in case user forget to add cracked passwords
    manual_connect_cmd = """
    essid="{essid}"
    pass="{psk}"

    killall -9 besside-ng
    airmon-ng stop wlan1mon
    airmon-ng stop wlan0mon
    killall -9 wicd

    sudo ip link set wlan1 down
    sudo iw link set wlan0 down
    sudo iw wlan1 set type managed
    sudo iw wlan0 set type managed
    sudo ip link set wlan1 up
    sudo ip link set wlan0 up

    iw dev
    service wpa_supplicant restart
    dhclient wlan1 up
    dhclient wlan0 up

    wpa_supplicant -Bwext -iwlan0 "$essid" "$pass"
    wpa_supplicant -Bwext -iwlan1 "$essid" "$pass"

    """.format(str(essid),str(psk))

    # /etc/network/interfaces
    interfaces_file_template = """
    auto lo

    iface lo inet loopback
    iface eth0 inet dhcp

    allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp

    allow-hotplug wlan1
    iface wlan1 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp

    """

    # /etc/ssh/*
    ssh_config = """
    # This is the ssh client system-wide configuration file.  See
    # ssh_config(5) for more information.  This file provides defaults for
    # users, and the values can be changed in per-user configuration files
    # or on the command line.

    # Configuration data is parsed as follows:
    #  1. command line options
    #  2. user-specific file
    #  3. system-wide file
    # Any configuration value is only changed the first time it is set.
    # Thus, host-specific definitions should be at the beginning of the
    # configuration file, and defaults at the end.

    # Site-wide defaults for some commonly used options.  For a comprehensive
    # list of available options, their meanings and defaults, please see the
    # ssh_config(5) man page.

    Host *
    #   ForwardAgent no
    #   ForwardX11 no
    #   ForwardX11Trusted yes
    #   RhostsRSAAuthentication no
    #   RSAAuthentication yes
    #   PasswordAuthentication yes
    #   HostbasedAuthentication no
    #   GSSAPIAuthentication no
    #   GSSAPIDelegateCredentials no
    #   GSSAPIKeyExchange no
    #   GSSAPITrustDNS no
    #   BatchMode no
    #   CheckHostIP yes
    #   AddressFamily any
    #   ConnectTimeout 0
    #   StrictHostKeyChecking ask
    #   IdentityFile ~/.ssh/identity
    #   IdentityFile ~/.ssh/id_rsa
    #   IdentityFile ~/.ssh/id_dsa
    #   IdentityFile ~/.ssh/id_ecdsa
    #   IdentityFile ~/.ssh/id_ed25519
    #   Port 22
    #   Protocol 2
    #   Cipher 3des
    #   Ciphers aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,aes128-cbc,3des-cbc
    #   MACs hmac-md5,hmac-sha1,umac-64@openssh.com,hmac-ripemd160
    #   EscapeChar ~
    #   Tunnel no
    #   TunnelDevice any:any
    #   PermitLocalCommand no
    #   VisualHostKey no
    #   ProxyCommand ssh -q -W %h:%p gateway.example.com
    #   RekeyLimit 1G 1h
        SendEnv LANG LC_*
        HashKnownHosts yes
        GSSAPIAuthentication yes

    """
    sshd_config = """

    # This is the sshd server system-wide configuration file.  See
    # sshd_config(5) for more information.

    # This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

    # The strategy used for options in the default sshd_config shipped with
    # OpenSSH is to specify options with their default value where
    # possible, but leave them commented.  Uncommented options override the
    # default value.

    Port 22
    #AddressFamily any
    #ListenAddress 0.0.0.0
    #ListenAddress ::

    #HostKey /etc/ssh/ssh_host_rsa_key
    #HostKey /etc/ssh/ssh_host_ecdsa_key
    #HostKey /etc/ssh/ssh_host_ed25519_key

    # Ciphers and keying
    #RekeyLimit default none

    # Logging
    #SyslogFacility AUTH
    #LogLevel INFO

    # Authentication:

    #LoginGraceTime 2m
    PermitRootLogin yes
    #StrictModes yes
    #MaxAuthTries 6
    #MaxSessions 10

    #PubkeyAuthentication yes

    # Expect .ssh/authorized_keys2 to be disregarded by default in future.
    #AuthorizedKeysFile	.ssh/authorized_keys .ssh/authorized_keys2

    #AuthorizedPrincipalsFile none

    #AuthorizedKeysCommand none
    #AuthorizedKeysCommandUser nobody

    # For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
    #HostbasedAuthentication no
    # Change to yes if you don't trust ~/.ssh/known_hosts for
    # HostbasedAuthentication
    #IgnoreUserKnownHosts no
    # Don't read the user's ~/.rhosts and ~/.sh",osts files
    #IgnoreRhosts yes

    # To disable tunneled clear text passwords, change to no here!
    PasswordAuthentication yes
    #PermitEmptyPasswords no

    # Change to yes to enable challenge-response passwords (beware issues with
    # some PAM modules and threads)
    ChallengeResponseAuthentication no

    # Kerberos options
    #KerberosAuthentication no
    #KerberosOrLocalPasswd yes
    #KerberosTicketCleanup yes
    #KerberosGetAFSToken no

    # GSSAPI options
    #GSSAPIAuthentication no
    #GSSAPICleanupCredentials yes
    #GSSAPIStrictAcceptorCheck yes
    #GSSAPIKeyExchange no

    # Set this to 'yes' to enable PAM authentication, account processing,
    # and session processing. If this is enabled, PAM authentication will
    # be allowed through the ChallengeResponseAuthentication and
    # PasswordAuthentication.  Depending on your PAM configuration,
    # PAM authentication via ChallengeResponseAuthentication may bypass
    # the setting of "PermitRootLogin without-password".
    # If you just want the PAM account and session checks to run without
    # PAM authentication, then enable this but set PasswordAuthentication
    # and ChallengeResponseAuthentication to 'no'.
    UsePAM yes

    AllowAgentForwarding yes
    AllowTcpForwarding yes
    #GatewayPorts no
    X11Forwarding yes
    X11DisplayOffset 10
    #X11UseLocalhost yes
    PermitTTY yes
    PrintMotd no
    PrintLastLog yes
    TCPKeepAlive yes
    #UseLogin no
    #UsePrivilegeSeparation sandbox
    PermitUserEnvironment no
    #Compression delayed
    #ClientAliveInterval 0
    #ClientAliveCountMax 3
    #UseDNS no
    #PidFile /var/run/sshd.pid
    #MaxStartups 10:30:100
    #PermitTunnel no
    #ChrootDirectory none
    #VersionAddendum none

    # no default banner path
    #Banner none

    # Allow client to pass locale environment variables
    AcceptEnv LANG LC_*

    # override default of no subsystems
    Subsystem	sftp	/usr/lib/openssh/sftp-server

    # Example of overriding settings on a per-user basis
    #Match User anoncvs
    #	X11Forwarding no
    #	AllowTcpForwarding no
    	PermitTTY yes
    #	ForceCommand cvs server

    """
