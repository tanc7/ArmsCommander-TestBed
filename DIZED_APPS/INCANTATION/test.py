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
interpreter.RoutersploitInterpreter.command_run.im_self.test.py
