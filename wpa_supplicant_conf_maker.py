import time
import os
import socket
import sys
import operator
import socket
import subprocess
import re
import optparse
from sys import argv
sys.path.append('/root/ArmsCommander')
import toolkits
# this program writes wifi auto-logins for WPA supplicant that can be dragged and dropped for instant, reliable logins to targeted networks for a red team.


potfile = '/root/.hashcat/hashcat.potfile'
dumped_potfile = '/tmp/dumped_passwords.txt'


WPA_connection_mode = 'WPAX_PSK'

WPA_switch = 0

WPA_switch_dict = {
    0: 'WPAX_PSK',
    1: 'WPA2_MGT',
    2: 'WEP',
    3: 'OPEN'
}
#@if WPA_switch != 0:
WPA_connection_mode = WPA_switch_dict[WPA_switch]




# wicd = False
# wicd_question = str(raw_input("Are you by any chance planning to use 'wicd' network manager? 'y' or 'n'"))

answer_key = {
    'y': True,
    'yes': True,
    'Yes': True,
    'n': True,

}

# if answer_key[wicd_question] == True:
#     wicd = True
# else:
#     wicd = False

def bash_command(cmd):
    subprocess.call(cmd, shell=True, executable='/bin/bash')
    return potfile, dumped_potfile,

def convert_hashcat_potfile(potfile,dumped_potfile):

    # debug_str = "DEBUG: reached function def convert_hashcat_potfile(potfile,dumped_potfile):"
    # print toolkits.yellow(debug_str)
    CMD_convert_to_single_lines = """cat {1} | awk -F ":" '{{ print $2 "|" $4 "|" $5 }}' | uniq  > {0}""".format(str(dumped_potfile),str(potfile))
    CMD_convert_to_single_lines = str(CMD_convert_to_single_lines)
    # bash_command("echo '#!/bin/bash' > bash_cmd.sh;echo 'SHELL=/bin/bash' >> /bash_cmd.sh;echo '%s' >> bash_cmd.sh;/bin/bash bash_cmd.sh" % CMD_convert_to_single_lines)
    bash_command(CMD_convert_to_single_lines)
    readlines(potfile,dumped_potfile)
    return potfile, dumped_potfile,

def write_wpa_config(bssid, essid, psk):
    key_mgmt = 'WPA-PSK'
    bssid = str(bssid)
    psk = str(psk)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    timestr = str(timestr)
    CONF_FILE_wpa_supplicant = "/tmp/%s.conf" % essid
    CONF_FILE_wpa_supplicant = CONF_FILE_wpa_supplicant.strip().replace('\n','').replace('\t','').replace('$','').replace('ssid=','')
    print CONF_FILE_wpa_supplicant
    print toolkits.red(timestr)
    essid = '\n\tssid="%s"' % str(essid)
    psk = '\n\tpsk="%s"' % str(psk)
    key_mgmt='\n\tkey_mgmt=%s' % str(key_mgmt)
    DEFAULT_wpa_supplicant_file = "/etc/wpa_supplicant/wpa_supplicant.conf"

    # print toolkits.red("DEBUG:\nessid=%s\npsk=%s\nkey_mgmt=%s" % (str(essid),str(psk),str(key_mgmt)))
    WRITE_STRING_wpa_supplicant_DEBIAN_WPA2PSK = """
    network = {"""
    print toolkits.red(WRITE_STRING_wpa_supplicant_DEBIAN_WPA2PSK)

    w = open(CONF_FILE_wpa_supplicant,'w+')
    x = open(DEFAULT_wpa_supplicant_file,'a+')
    w.write(WRITE_STRING_wpa_supplicant_DEBIAN_WPA2PSK) # writes one copy the backup copies of individual networks

    print toolkits.green('DEBUG: Line written successfully')
    x.write(WRITE_STRING_wpa_supplicant_DEBIAN_WPA2PSK) # writes another copy as a block of setting configurations into wpa_supplicant.conf
    print toolkits.green('DEBUG: Line written successfully')
    w.write(essid)


    print toolkits.green('DEBUG: Line written successfully')
    x.write(essid)

    w.write(psk)

    print toolkits.green('DEBUG: Line written successfully')
    x.write(psk)
    w.write(key_mgmt)

    print toolkits.green('DEBUG: Line written successfully')
    x.write(key_mgmt)
    w.write('\n}')

    print toolkits.green('DEBUG: Line written successfully')
    x.write('\n}')
    w.close()
    x.close()

    move_to_wpa_supplicant_folder = "cp -r %s %s" % (str(CONF_FILE_wpa_supplicant),str('/etc/wpa_supplicant'))
    bash_command(move_to_wpa_supplicant_folder)

    append_to_main_wpa_supplicant_file = "cat /tmp/wpa*.conf >> /etc/wpa_supplicant/wpa_supplicant.conf"
    bash_command(append_to_main_wpa_supplicant_file)
    bash_command("file /etc/wpa_supplicant/*")
    #bash_command("cat %s") % (str(CONF_FILE_wpa_supplicant))

    #     except:
    #         pass
    # else:
    #     pass

    if key_mgmt == "NONE" and username == '' and password == '':
        debug_str = "OPEN NETWORK DETECTED. There is nothing to do here except to pwn everyone on that network. But I will set up WPA supplicant file anyways.\n\n\n Be careful of cybersecurity measures installed, such as Google Starbucks and OpenMesh."

        print toolkits.yellow(debug_str)
        try:
            timestr = time.strftime("%Y%m%d-%H%M%S")
            print toolkits.green("DEBUG: time-string is '%s'" % str(timestr))
            CONF_FILE_wpa_supplicant = "/tmp/wpa_supplicant_{0}_{1}.conf".format(str(essid),str(bssid))
            CONF_FILE_wpa_supplicant = str(CONF_FILE_wpa_supplicant)
            print toolkits.red("DEBUG:\nessid=%s\npsk=%s\nkey_mgmt=%s" % (str(essid),str(psk),str(key_mgmt)))
            timestr = str(timestr)
            print "FILE TO WRITE: %s" % CONF_FILE_wpa_supplicant

            essid = '\n\tssid="%s"' % str(essid)
            psk = '\n\tpsk="%s"' % str(psk)
            key_mgmt='\n\t%s' % str(key_mgmt)

            print toolkits.red("DEBUG:\nessid=%s\npsk=%s\nkey_mgmt=%s" % (str(essid),str(psk),str(key_mgmt)))

            wpa_supplicant_deb_format_OPEN = """
            network = {"""

            wpa_supplicant_deb_format_WPA2_MGT
            w.write(wpa_supplicant_deb_format_OPEN)
            w.write(essid)
            w.write(psk)
            w.write(key_mgmt)
            w.write('\n}')
            w.close()

            print toolkits.green("DEBUG: Finished writing file: {0}" % CONF_FILE_wpa_supplicant)
            move_to_wpa_supplicant_folder = "cp -r %s %s" % (str(CONF_FILE_wpa_supplicant),str('/etc/wpa_supplicant'))
            bash_command(move_to_wpa_supplicant_folder)

            append_to_main_wpa_supplicant_file = "cat /tmp/wpa*.conf >> /etc/wpa_supplicant/wpa_supplicant.conf"
            bash_command(append_to_main_wpa_supplicant_file)
            bash_command("file /etc/wpa_supplicant/*")
        except:
            pass
        return


    return potfile, dumped_potfile

def determine_creds_uncertain_user(psk, wep_key_hex, wep_tx_keyidx, key_mgmt): # entirely different function just for unfamiliar OSes chosen for hacking.:

    print "Please answer the following questions and we will see which conf file we should write to you"

    psk_ques = str(raw_input("Do you have a PSK? If you cracked the password with hashcat, you would have either a PSK, otherwise known as a Pre-shared Key, or a Hexidecimal digit set of numbers or a WPS PIN "))


    WPAX_PSK = True
    WPA2_MGT = False
    WEP = False
    OPEN = False
    if len.psk_ques < 8 or psk_ques == '' or None or 0:
        WPAX_PSK = False

        try:
            mgt_radius_USER = str(raw_input("Are you required to enter BOTH a USERNAME and a PASSWORD, either by login prompt or captive  portal? If so enter the USERNAME HERE: "))
            mgt_radius_PASS == str(raw_input("Enter the PASSWORD here: "))
            if mgt_radius_USER and mgt_radius_PASS != '':
                WPA2_MGT = True
                write_wpa_config(WPA2_MGT,WPAX_PSK,WEP,OPEN)
            else:
                WEP_key_hex = str(raw_input("Are you required to entera  hexidecimal WEP key? Maybe a second key? Put in your WEP hex key here: "))
                WEP_key_tx = str(raw_input("Enter your WEP transmit key if you have one: "))

                if WEP_key_hex != None or 0 and WPAX_PSK and WPA2_MGT == False:
                    WEP = True
                    write_wpa_config(WPA2_MGT,WPAX_PSK,WEP,OPEN)
                else:
                    pass

        except:
            OPEN = True
            print toolkits.red('Looks like you made a  mistake. You are actually targeting a OPEN network. I will send you on your way to making that file')
            psk = ''
            username = ''
            password = ''
            try:
                timestr = time.strftime("%Y%m%d-%H%M%S")
                timestr = str(timestr)
                print "FILE TO WRITE: %s" % CONF_FILE_wpa_supplicant
                timestr = time.strftime("%Y%m%d-%H%M%S")
                timestr = str(timestr)
                essid = '\n\tssid="%s"' % str(essid)
                psk = '\n\tpsk="%s"' % str(psk)
                key_mgmt='\n\t%s' % str(key_mgmt)

                print toolkits.red("DEBUG:\nessid=%s\npsk=%s\nkey_mgmt=%s" % (str(essid),str(psk),str(key_mgmt)))

                wpa_supplicant_deb_format_OPEN = """
                ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
                update_config=1
                country=GB
                network = {"""

                wpa_supplicant_deb_format_WPA2_MGT
                w.write(wpa_supplicant_deb_format_OPEN)
                w.write(essid)
                w.write(psk)
                w.write(key_mgmt)
                w.write('\n}')
                w.close()

                print toolkits.green("DEBUG: Finished writing file: {0}")
                move_to_wpa_supplicant_folder = "cp -r %s %s" % (str(CONF_FILE_wpa_supplicant),str('/etc/wpa_supplicant'))
                bash_command(move_to_wpa_supplicant_folder)

                append_to_main_wpa_supplicant_file = "cat /tmp/wpa*.conf >> /etc/wpa_supplicant/wpa_supplicant.conf"
                bash_command(append_to_main_wpa_supplicant_file)
                bash_command("file /etc/wpa_supplicant/*")
            except:
                pass

    else:
        WPAX_PSK = True
        #write_string = WPAX_PSK_conf
        write_wpa_config(WPA2_MGT,WPAX_PSK,WEP,OPEN)

        # WEP, WPA/WPA2-PSK, WPA2-MGT/ENT, and OPEN
        wpa_supplicant_deb_format_WPA2_MGT
        w.write(WRITE_STRING_wpa_supplicant_DEBIAN_WPA2PSK)
        w.close()
        debug_str = "DEBUG: Reached end of program. Written file is: %s" % str(CONF_FILE_wpa_supplicant)
        print toolkits.yellow(debug_str)
        move_to_wpa_supplicant_folder = "cp -r %s %s" % (str(CONF_FILE_wpa_supplicant),str('/etc/wpa_supplicant'))
        bash_command(move_to_wpa_supplicant_folder)

        append_to_main_wpa_supplicant_file = "cat /tmp/wpa*.conf >> /etc/wpa_supplicant/wpa_supplicant.conf"
        bash_command(append_to_main_wpa_supplicant_file)
        bash_command("file /etc/wpa_supplicant/*")
        print toolkits.green("You are good to go! The config files have been copied over. Make sure you use the standard Raspbian network manager.")

        print toolkits.red("DEBUG: Contents of wpasupplicant folder")
        bash_command("ls -la /etc/wpa_supplicant/*")

        return potfile, dumped_potfile

def write_wicd_format_conf():
    return

def readlines(potfile,dumped_potfile):
    debug_str = "In function: def readlines(potfile,dumped_potfile):"
    DEFAULT_potfile_organized = '/root/.hashcat/potfile_organized.txt'

    print toolkits.green(debug_str)
    print toolkits.yellow("Dumped potfile is at: %s" % dumped_potfile)

    cmd = "ls -la %s" % str(dumped_potfile)
    bash_command("cp -r %s %s" % (dumped_potfile, DEFAULT_potfile_organized))
    print toolkits.yellow("Cleaned up potfile at: %s" % DEFAULT_potfile_organized)
    time.sleep(3)
    print toolkits.green('Now preparing to copy all of the creds from %s WPA_connection_mode to /etc/wpa_supplicant, 3 seconds...' % str(WPA_connection_mode))
    result = bash_command(cmd)
    print toolkits.cyan(result)
    try:
        r = open(dumped_potfile,'r+')
        with open(dumped_potfile) as r:
            line = r.readline()
            for line in r:
                try:
                    line = line.split("|")
                    print toolkits.yellow("Debug: %s" % str(line))
                    bssid = line[0].strip()
                    print toolkits.yellow("DEBUG bssid = %s" % str(bssid))
                    essid = line[1].strip()
                    print toolkits.yellow("DEBUG essid = %s" % str(essid))

                    psk = line[2].strip()
                    print toolkits.yellow("DEBUG PSK = %s" % str(psk))
                    # wicd = False
                    write_wpa_config(str(bssid), str(essid), str(psk))

                except EOFError:
                    pass
    except EOFError:
        exit(0)

    return potfile, dumped_potfile
def sorter(potfile, dumped_potfile):
    parser = optparse.OptionParser('usage % prog -r <hashcat potfile>')
    parser.add_option('-r', dest='potfile', type='string', help='full absolute path to list of IPs to resolve')
    (options, args) = parser.parse_args()
    if options.potfile == None:
        potfile = '/root/.hashcat/hashcat.potfile'
        convert_hashcat_potfile(potfile,dumped_potfile)
    else:
        potfile = options.potfile
        convert_hashcat_potfile(potfile,dumped_potfile)
    return potfile, dumped_potfile
# sorter(potfile, dumped_potfile)
#
def WPAX_PSK_config_files():
    WPA_connection_mode = 'WPAX_PSK'
    WPA_switch = 0
    potfile = '/root/.hashcat/hashcat.potfile'
    dumped_potfile = '/tmp/dumped_passwords.txt'
    sorter(potfile, dumped_potfile)
    return

def main():

    WPAX_PSK_config_files()
    try:
        if WPA_connection_mode == 'WPAX_PSK':
            WPAX_PSK_config_files()
        elif WPA_connection_mode == 'WPA2_MGT':
            WPA2_MGT_RADIUS_server_config_files()
        elif WPA_connection_mode == "WEP":
            WEP_config_files()
        else:
            WPA_connection_mode == "OPEN"
            OPEN_config_files()
    except WPA_switch > 3 or WPA_switch < 0:
        WPA_switch = 0
        exit(0)


    return
main()
