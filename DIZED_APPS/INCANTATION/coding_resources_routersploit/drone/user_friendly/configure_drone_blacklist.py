import os
import sys
import socket
import operator
import subprocess
import time
import re
os.chdir('/root/Cylon-Raider-Lite/logs/wardriver_xpress')
parrot_drone_ESSID = str(raw_input("Enter the ESSID (name) of your drone as it appears on Wi-Fi: "))
parrot_drone_BSSID = str(raw_input("Enter the BSSID (MAC address) of your drone as it appears on Wi-Fi: "))
drone_controller_ESSID = str(raw_input("Enter the ESSID (name) of your smartphone/tablet as it appears on Wi-Fi: "))
drone_controller_BSSID = str(raw_input("Enter the BSSID (MAC address) of your smartphone/tablet as it appears on Wi-Fi: "))

# set ignore to drone network ID
ignore_essid = parrot_drone_ESSID
ignore_bssid = parrot_drone_BSSID
str_ignore_line_for_besside = "{0}           \| Got WPA handshake                      \| {1} \|".format(str(ignore_essid),str(ignore_bssid))

# add to blacklist
add_ignore_cmd = """echo {0} >> blacklist.txt""".format(str(str_ignore_line_for_besside))
os.system(add_ignore_cmd)

confirmation_str = "DEVICE: {0} with MAC: {1} has been added to the blacklist".format(str(ignore_essid),str(ignore_bssid))
print confirmation_str
# set ignore to drone controller network ID
ignore_essid = drone_controller_ESSID
ignore_bssid = drone_controller_BSSID
str_ignore_line_for_besside = "{0}           \| Got WPA handshake                      \| {1} \|".format(str(ignore_essid),str(ignore_bssid))

# add to blacklist
add_ignore_cmd = """echo {0} >> blacklist.txt""".format(str(str_ignore_line_for_besside))
confirmation_str = "DEVICE: {0} with MAC: {1} has been added to the blacklist".format(str(ignore_essid),str(ignore_bssid))
print confirmation_str
os.system(add_ignore_cmd)
