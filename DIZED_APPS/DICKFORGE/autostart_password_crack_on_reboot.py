#!/usr/bin/env python
# coding=UTF-8

# add @reboot python /root/ArmsCommander/passwordattacks/autostart_password_crack_on_reboot.py
# to your crontab by typing crontab -e
#import modules
import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
# sys.path.append("/root/ArmsCommander/passwordattacks")
import password_toolkits
import time
import subprocess
import threading


##################### CHANGE THIS TO YOUR OWN WORDLIST #####################################################
password_wordlist = '/mnt/Data1/WordlistCollection/AWESOME_LIST_2'
installation_dir = "/root/ArmsCommander/logs/HashCat"
queue_folder = "{0}/queue_folder".format(str(installation_dir)) # for the discovered.cap files queue.
##################### LEAVE EVERYTHING ELSE ALONE ##############################################################















### fallback password list, if the user didn't change the above value to his own ###
if password_wordlist == "" or 0 or None:
    password_wordlist = "/usr/share/wordlists/metasploit/password.lst"
    # its the largest pw list I could find in a stock Kali Linux installation :/

#### REMINDERS
# 1. add a copy of the cap2hccapx binary with this copy online, so we can fix it for them
# 2. Finish the threading module and see if it is capable of hunting my entire hard disk for hashes to crack.
# 3. Then shut down teh threading as a alternative option.


################ COLORED DISPLAYS

def red(string):
    string = colored(string,'red',attrs=['bold'])
    return string
def green(string):
    string = colored(string,'green',attrs=['bold'])

    return string
def yellow(string):
    string = colored(string,'yellow',attrs=['bold'])

    return string
def cyan(string):
    string = colored(string,'cyan',attrs=['bold'])

    return string


################# VITAL FILES FOR FUNCTIONING ######################

pw_cracker_wordlist = '/root/ArmsCommander/passwordattacks/CocaineFactory/wordlist'
converter_wordlist_cap_to_hccapx = "/root/ArmsCommander/passwordattacks/MeowMix/wordlist"
converter = "/root/ArmsCommander/passwordattacks/MeowMix/convert.py"
hccapx_dir = "/root/ArmsCommander/logs/HashCat"

print yellow("\n\n\n\t\t\tNOTE TO NEW USERS: Please configure your password wordlists! It will be the first variable \n\n\t\t\tpassword_wordlist='some path to list'")
print colored('CRACK COCAINE FACTORY, \nthe automated password-hasher for Hashcat GPU cracking rigs\nBy Chang Tan Lister\nwww.github.com/tanc7','white',attrs=['bold'])


def debug(comment):
    comment = password_toolkits.debug_text(comment)
    print comment
    return comment


############ allows it to permit different modes of operation beyond POSIX shells
def bash_command(command):

    subprocess.call(command,shell=True,executable="/bin/bash")
    return

def bash_background(command):
    process = subprocess.Popen(command,shell=True,executable="/bin/bash")
    return

def process_threads(cmd_1, cmd_2, cmd_3):
    # time right after start
    # the import-convert-load new WPA hashes function
    thread_x = bash_background(command)
    # right after start
    # the countdown timer function
    thread_y = bash_background(another_command)
    # right after start
    # the password cracker function
    thread_z = bash_background(one_more_command)
    # one hour after start
    # greps your entire hard disk for hashes to crack. Not sure if I will implement it. Could be invasion of privacy.
    thread_xyz = search_for_more_cap_files()
    return

# ######################################################greps your entire hard disk for hashes to crack. Not sure if I will implement it. Could be invasion of privacy.

def search_for_more_cap_files():
    dir_specified = "/"

    file_formats = [
        '.cap',
        '.hccapx'
    ]
    find_command = "find %s -iname '*.%s'" % (dir_specified, file_format)
    write_down_to_do_list()
    return

def write_down_to_do_list():
    discovered_files_list = "./discovered_cap_files"
    w = open(discovered_files_list,'w')
    w.write(lines)
    w.close
    #import_command = "ls $PWD/*.cap > %s" % str(converter_wordlist_cap_to_hccapx)
    import_command = "cat %s > %s" % (str(discovered_files_list), str(converter_wordlist_cap_to_hccapx))

    bash_command(import_command)

    convert_cap_to_hccapx(hccapx_dir)
    return

def copy_over_files(discovered_files_list,queue_folder):

    filelist = str(discovered_files_list)
    queue_folder = ""
    sh_format_file = './temp_file.sh'


    shell_commands = """filelist="{0}"
folder_name="{1}"
for file in $(cat ${0}); do cp -r "$file" ${1};echo "copied: $file";done""".format(str(filelist),str(queue_folder))


    w = open(sh_format_file,'w')
    w.write(shell_commands)
    w.close()

    bash_command("/bin/sh %s" % sh_format_file)

    return
################ ALLOWS IT TO EDIT AND CONTINUALLY QUEUE THE WORDLIST FOR CRACKING PASSWORDS
def import_cap_files():
    debug("in import more .cap files function")
    os.chdir("/root/ArmsCommander/logs/HashCat")
    # search_command = "ls *.cap"

    import_command = "ls $PWD/*.cap > %s" % str(converter_wordlist_cap_to_hccapx)
    bash_command(import_command)

    convert_cap_to_hccapx(hccapx_dir)

    return

def convert_cap_to_hccapx(hccapx_dir):
    os.chdir(hccapx_dir)

    debug("in convert function")
    convert_command = "python /root/ArmsCommander/passwordattacks/MeowMix/convert.py"
    bash_command(convert_command)
    os.chdir(hccapx_dir)
    import_hccapx_command = "ls $PWD/*.hccapx >> %s" % pw_cracker_wordlist
    bash_command(import_hccapx_command)
    os.chdir(hccapx_dir)
    clear_out_old_files = "rm -rf ./*.cap"
    check_hashes_to_crack()

    return
################## PREVENTS CRASHES by double checking if its looping repeatedly. And then stops program if we are all out. #########################

def check_hashes_to_crack(pw_cracker_wordlist):
    results = bash_command("cat %s" % str(pw_cracker_wordlist))
    if str(results) == '' or None or 0:
        print "OUT OF HASHES"
        exit(0)
    else:
        pw_cracker(pw_cracker_wordlist, converter_wordlist_cap_to_hccapx, converter, hccapx_dir, password_wordlist)

    return
###########################################################################################



# def timer_add_new_hashes():
#
#     # pip shows this
#     #     countdown-slackbot (0.0.2)   - A slackbot that plays countdown
#     # countdown (1.0.0)            - A simple countdown recursive function
#     # easy-countdown (v0.1.0)      - A simple yet flexible countdown timer
#     # fluentcms-countdown (1.1.1)  - A countdown timer for django-fluent-contents
#     # CountDownApp (0.0.1)         - Count Down Timer Application
#     # countdowner (0.3.1)          - A Python 3.5+ package to check for sales at
#     #                                Countdowngrocery stores throughout New Zealand
#     # leonardo-counters (0.0.1)    - CounterWidget Up/Down CountdownWidget for
#     #                                Datetime
#     # csci.countdown (1.0dev)      - provides a countdown to an event
#     # easy-timer (0.0.4)           - Super Simple Command-line Countdown Timer
#     # pyCountdownTimer (1.0)       - A count-down timer that periodically checks a
#     #                                flag (to terminate the timer) using a supplied
#     #                                callable.
#     # termdown (1.12.1)            - Countdown timer for your terminal
#     # urtimer (0.6.1)              - Simple countdown timer and stopwatch using
#     #                                urwid
#     # wpd.countdown (2.0)          - Countdown portlet for the World Plone Days
#     # wpd.mmxi.countdown (1.0)     - Countdown portlet for the World Plone Day 2011
#
# #     starttime=time.time()
# #     interval = 21600
# #     while True:
# #
# # # import time
# # # starttime=time.time()
# # # while True:
# # #   print "tick"
# # #   time.sleep(60.0 - ((time.time() - starttime) % 60.0))
#
#     # if time == 00000
#     #     import_cap_files()
#     # return

######################### the actual PW cracking machine ##################################

def pw_cracker(pw_cracker_wordlist, converter_wordlist_cap_to_hccapx, converter, hccapx_dir, password_wordlist):
    # os.chdir("/root/ArmsCommander/passwordattacks/CocaineFactory")
    crack_mode = 2

# if crack_mode is NOT ZERO, you must provide additional parameters!
# and uncomment this bottom line

    # crack_mode = 1
    ruleset = '/usr/share/hashcat/rules/dive.rule' # find your rulesets at...

    # crack_mode = 2 # pp_binary
    pp_binary = "/usr/local/bin/pp64.bin"
    hash_type = 'slow' # hash type for WPA hashes
    # hash_type = 'fast' # for something easier to crack like NTLM
    if hash_type == 'fast':
        ruleset = '/usr/share/hashcat/rules/dive.rule' # find your rulesets at...
    debug("All modules loaded")


    debug("loading %s" % str(pw_cracker_wordlist))
    w = open(pw_cracker_wordlist,'r+b')
    read_w = w.read()
    buf = StringIO.StringIO(read_w)
    debug("Reading user input file")
    pw_attack_type = 'STRAIGHT DICTIONARY ATTACK'

    while True:
        try:
            # debug("Entered pw cracking loop")
            timestr = time.strftime("%Y%m%d-%H%M%S")
            # open progress log, write COMPLETED for anything already done

            line = buf.readline().strip()

            if line != '': # line with uncracked hash
                file_to_mark = line
                line = line.replace('(','\(')
                line = line.replace(')','\)')
                hash_file = line
                debug("Cracking file: %s" % str(hash_file))

                print colored('[+] Now cracking the hashes of file: %s','yellow',attrs=['bold']) % hash_file

                if crack_mode == 0:
                    # Stanard, unamplified, non-piped password cracking. Straight-attack.
                    cmd_String = "hashcat -a 0 -w 4 -m 2500 %s %s --session=test --force" % (str(hash_file), str(password_wordlist))
                elif crack_mode == 1: # ruleset enhanced password cracking mode
                    cmd_String = "hashcat -a 0 -w 4 -m 2500 %s %s --session=ruleset --force -r %s" % (str(hash_file), str(password_wordlist), str(ruleset))
                elif crack_mode == 2: # prince processor attacks
                    if hash_type == 'slow':
                        cmd_String = "{0} < {1} | hashcat -a 0 -w 4 -m 2500 --session=ruleset_pp --runtime=600 {2}".format(
                            str(pp_binary),
                            str(password_wordlist),
                            str(hash_file)
                        )
                    elif hash_type == 'fast':
                        cmd_String = "{0} < {1} | hashcat -a 0 -w 4 -m 2500 --session=pp --runtime=600 {2} -r {3}".format(
                            str(pp_binary),
                            str(password_wordlist),
                            str(hash_file),
                            str(ruleset)
                        )
                else:
                    print ""
                    exit(0)


                os.system(cmd_String)


            else: # empty line
                pass
        except EOFError: # end of file

            print colored('[-] Hashcat has finished going through the wordlists you provided against your password dictionary\nPlease Check the console output for results','red',attrs=['bold'])
            import_cap_files()
    return

pw_cracker(pw_cracker_wordlist, converter_wordlist_cap_to_hccapx, converter, hccapx_dir, password_wordlist)
