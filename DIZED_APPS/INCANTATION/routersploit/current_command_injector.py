#!/usr/bin/env/python
from __future__ import absolute_import
import rsf
import routersploit
from routersploit import *
from routersploit import shell
from os import path
from routersploit import *
### notes

#### because of all of this, you must instqall routersploit intoa  PATH directory, in other words...
### /usr/bin or /usr/local/bin or soemthing like that
### you then have to place your injector right into the path so that its executable and python can find it. SO...

### /usr/local/bin/routersploit/command_injector.py
## nevermind! I made it automated. It'll automatically generate a duplicate copy of the script to do its deeds.


### in return, assuming you wrote a script for it, you can immediately automate post-exploitation as soon as the pi boots up
from routersploit import exploits
from routersploit import payloads
from routersploit import wordlists
from routersploit import validators
from routersploit.shell import shell
###  CUSTOM COMMAND. Discovered new options that enabled me to directly inject python statements into RSF.
import interpreter
from interpreter import * ############ VITAL! Otherwise you cannot access the engine that processes human input into their shell syntax
from shell import *
import importlib
from importlib import *

from routersploit import (exploits,print_error,print_success,print_status,print_info,utils,threads)

import threading
import subprocess

from routersploit.utils import (
print_error,
print_status,
print_success,

print_info,
sanitize_url,
LockedIterator,
random_text,
http_request,
boolify,
mute,
multi,
index_modules,
ssh_interactive,
tokenize,
)

### notes




#### For every one of the modules. you also needed to import this crqazy shit. IT helps in getting the ungraspable modules back. But we just want to reach their custom shel since we can easily learn their syntax.




### at this point you shoudl ahve the ability to directly access your interpreter from the root of the installation directory.
### we need also a logger of our own.


def threads(): # we are planning to add more features into this to allow more penetration testing services to run concurrently.
    rsf = ''
    timer = ''
    dotdotpwn = ''
    othermodules = ''
    metasploit = ''

    return



def crontab_generator():
    return
    # if this one on the bottom works. We can then crontab the script after a successful text
    # it works but I'd rather put it into a installer file instead,

def operate_wait_and_hold_generate_py_script(target,port,threads):

    written_target = "{}".format(str(target))
    written_port = str('{}').format(str(port))
    written_threads = str('8')

    print '\t\t\t\n\n\n' + written_target, '\t\t\t\n\n\n' + written_port, '\t\t\t\n\n\n' + written_threads
    direct_line_feed_injection = """
#!/usr/bin/env/python
from __future__ import absolute_import
import logging
import io

### Create the logger
logger = logging.getLogger('basic_logger')
logger.setLevel(logging.DEBUG)

### Setup the console handler with a StringIO object
log_capture_string = io.StringIO()
ch = logging.StreamHandler(log_capture_string)
ch.setLevel(logging.DEBUG)

### Optionally add a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

### Add the console handler to the logger
logger.addHandler(ch)


### Send log messages.
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


### Pull the contents back into a string and close the stream
log_contents = log_capture_string.getvalue()
log_capture_string.close()

### Output as lower case to prove it worked.
print(log_contents.lower())
import rsf
import routersploit
from routersploit import *
from routersploit import shell
from os import path
from routersploit import *
from routersploit import exploits
from routersploit import payloads
from routersploit import wordlists
from routersploit import validators
from routersploit.shell import shell
###  CUSTOM COMMAND. Discovered new options that enabled me to directly inject python statements into RSF.
import interpreter
from interpreter import * ############ VITAL! Otherwise you cannot access the engine that processes human input into their shell syntax
from shell import *
import importlib
from importlib import *

from routersploit import (exploits,print_error,print_success,print_status,print_info,utils,threads)

import threading
import subprocess

from routersploit.utils import (
print_error,
print_status,
print_success,

print_info,
sanitize_url,
LockedIterator,
random_text,
http_request,
boolify,
mute,
multi,
index_modules,
ssh_interactive,
tokenize,
)
RoutersploitInterpreter.parse_line.__init__
RoutersploitInterpreter.command_use.__name__
self = "routersploit/interpreter"
RoutersploitInterpreter.parse_line.__init__
exploits.__init__
exploits.Exploit.__init__
routersploit.exploits.__name__ = "autopwn"
routersploit.exploits.ExploitOptionsAggregator.__init__
routersploit.exploits.Option(str('{}'),'')
routersploit.exploits.Option({},'')
routersploit.exploits.Option({},'')

exploits.Exploit.run_threads.im_self

RoutersploitInterpreter.command_run.im_self
routersploit.utils.print_status
RoutersploitInterpreter.history_file
RoutersploitInterpreter.history_file.decode
exploits.print_status.func_globals
print sys.stdout
print sys.stdout.encoding
print sys.stdout.errors
print sys.stdout.write
interpreter.RoutersploitInterpreter.command_run.im_self.__init__


""".format(
            str(written_target),
            str(written_port),
            str(written_threads)
        )
    direct_line_feed_injection = str(direct_line_feed_injection)

    w = open('/usr/local/bin/direct_injection_exec.py','w')
    w.write(direct_line_feed_injection)
    w.close()
    # time.sleep(3) # to avoid crashing the program
    chmod = "chmod 777 {}".format(str('/usr/local/bin/direct_injection_exec.py &'))
    rsf_command(str(chmod))
    cmd = "python %s" % str('/usr/local/bin/direct_injection_exec.py &')
    rsf_command(cmd)
    # time.sleep(0.5)
    return

def rsf_command(cmd):
    progress = subprocess.call(cmd,shell=True,executable='/bin/bash')
    print progress
    return progress
def line_feed_queue(results):
    port_list = [
        80,
        443,
        8080,
        81,
        4567,
        9999,
        22,
        23,
        25,
        53
    ]
    for ip in results:
        target = exploits.Option(str(ip))
        for port in list_of_ports:
            port = exploits.Option(str(port))
            threads = exploits.Option(str(8))
            operate_wait_and_hold_generate_py_script(direct_line_feed_injection,target, port, threads)

    return
def extract_gw_ips(results):
    for gw_ip in results:
         target = str(gw_ip)
         port_list = [
             80,
             443,
             8080,
             81,
             4567,
             9999,
             22,
             23,
             25,
             53
         ]

         # for ip in results:
         target = exploits.Option(str(ip))
         for port in list_of_ports:
             port = exploits.Option(int(port))
             threads = exploits.Option(int(8))
             operate_wait_and_hold_generate_py_script(direct_line_feed_injection,target, port, threads)
    return

def rsf_primary_thread(cmd):
    results = subprocess.Popen(cmd,shell=True,executable='/bin/bash')
    results = str(results)
    for ip in results:
        # results = results.append(ip)
        for gw_ip in results:
             target = str(gw_ip)
             port_list = [
                 80,
                 443,
                 8080,
                 81,
                 4567,
                 9999,
                 22,
                 23,
                 25,
                 53
             ]
             # for ip in results:
             for port in port_list:
                 port = exploits.Option(str(port))
                 threads = exploits.Option(str(8))
                 operate_wait_and_hold_generate_py_script(target, port, threads)
    return

def main():
    command = """route -n | egrep -v "0.0.0.0|Gateway|routing" | sort | uniq | awk '{{print $2}}'"""
    rsf_primary_thread(command)
    return
def bash_command(cmd):
    output = subprocess.call(cmd,shell=True,executable='/bin/bash')
    return output

def detect_network():
    # detects the assignment  of a local IP, which guarantees that you have been connected to the LOCAL network, good enough for wireless exploitation
    time.sleep(5) # checks every 5 seconds
    detection_test = "ifconfig | grep inet | awk '{{print $2}}'"
    test_results = bash_command(detection_test)
    if test_results != "" or None or 0:
        if test_results != "0.0.0.0" or '127.0.0.1' or 'ether':
            print "SUCCESSFULLY CONNECTED: Your ip address is \n\t%s" % test_results
            time.sleep(2)
            main()
        else:
            detect_network()
    else:
        detect_network()
    return
print "Raspberry Pi just booted. Scanning for networks to login to."
detect_network()
# Direect feed method. according to this article
# requires perfect path positioning! Might need to makea  launcher script for usr bins
# we still have the display issue to deal with and logging. So we need toa dd that in there too.


# requires me to put it on path chmod +x arbitraryname
# but I may use symbolic links cd ~/bin/
#ln -s ~/some/path/to/myscript/arbitraryname
# double check which interpreter with which commands
# https://dbader.org/blog/how-to-make-command-line-commands-with-python

# or even better write a script. and have python execute it which may be more successful, no spacing isses,
