import os
import sys
import socket
import operator
import __future__
main_routersploit_installation_dir = "/root/Documents/routersploit"
primary_installation_dir = "/root/Documents/routersploit/routersploit"
#!/usr/bin/env python2

#!/usr/bin/env python2

from __future__ import print_function

import argparse
import logging.handlers

from routersploit.interpreter import RoutersploitInterpreter
from routersploit.utils import create_exploit

log_handler = logging.handlers.RotatingFileHandler(filename='routersploit.log', maxBytes=500000)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s       %(message)s')
log_handler.setFormatter(log_formatter)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(log_handler)

parser = argparse.ArgumentParser(description='RouterSploit - Router Exploitation Framework')
parser.add_argument('-a',
                    '--add-exploit',
                    metavar='exploit_path',
                    help='Add exploit using default template.')


def routersploit():
    rsf = RoutersploitInterpreter()
    rsf.start()


if __name__ == "__main__":
    args = parser.parse_args()

    if args.add_exploit:
        create_exploit(args.add_exploit)
    else:
        routersploit()

os.chdir(main_routersploit_installation_dir)
# all routersploit modules
import routersploit
import __future__
from routersploit import *
from routersploit import exploits
from routersploit import payloads
from routersploit import utils
from routersploit import validators
from routersploit import wordlists
from routersploit.interpreter import *
from routersploit.payloads import *
from routersploit.printer import *
from routersploit.shell import *
from routersploit.threads import *
from routersploit.utils import *
from tests.test_case import *

import sys
sys.path.append("/root/Documents/routersploit/routersploit")

os.chdir(primary_installation_dir)

import ABCMeta
import __future__
import ARCH_ELF_HEADERS
import ArchitectureSpecificPayload
import Architectures
import BaseHTTPServer
import BaseInterpreter
import BasePayload
import BindTCPPayloadMixin
import CREDS_DIR
import Communication
import Counter
import DummyFile
import EXPLOITS_DIR
import Exploit
import GLOBAL_OPTS
import GenericPayload
import HttpRequestHandler
import HttpServer
import LockedIterator
import MODULES_DIR
import NonStringIterable
import OptionValidationError
import PayloadHandlers
import PrintResource
import PrinterThread
import Resource
import ReverseTCPPayloadMixin
import RoutersploitException
import RoutersploitInterpreter
import RoutersploitTestCase
import SCANNERS_DIR
import SimpleHTTPServer
import StopThreadPoolExecutor
import ThreadPoolExecutor
import WeakKeyDictionary
import WorkerThread
import __builtin__
import __builtins__
import __doc__
import __name__
import __package__
import absolute_import
import abstractmethod
import architectures
import atexit
import boolify
import collections
import colors
import create_exploit
import create_resource
import data_producing
import data_queue
import errno
import exceptions
import exploits
import http_request
import humanize_path
import import_exploit
import importlib
import index_modules
import inspect
import interpreter
import isfile
import iter_modules
import itertools
import join
import listdir
import logging
import main_routersploit_installation_dir
import mkdir_p
import module_required
import modules
import multi
import mute
import namedtuple
import operator
import os
import pack
import payload_handlers
import payloads
import posix_shell
import pprint_dict_in_order
import print_error
import print_function
import print_info
import print_lock
import print_status
import print_success
import print_table
import printer
import printer_queue
import pythonize_path
import queue
import random
import random_text
import re
import readline
import requests
import routersploit
import routersploit_installation
import rsf_modules
import sanitize_url
import select
import shellimport
import socket
import ssh_interactive
import stop_after
import string
import strtobool
import sys
import telnetlib
import thread_output_stream
import threading
import threads
import time
import tokenize
import traceback
import unittest
import utils
import validators
import windows_shell
import wordlists
import wraps
import Communication

class RoutersploitInterpreter(BaseInterpreter)
 |  Method resolution order:
 |      RoutersploitInterpreter
 |      BaseInterpreter
 |      __builtin__.object
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |
 |  available_modules_completion(self
 text)
 |      Looking for tab completion hints using setup.py entry_points.
 |
 |      May need optimization in the future!
 |
 |      :param text: argument ofimport use command
 |      :return: list of tab completion hints
 |
 |  command_back(self
 *args
 **kwargs)
 |
 |  command_check(self
 *args
 **kwargs)
 |
 |  command_exec(self
 *args
 **kwargs)
:
 |  command_exit(self
 *args
 **kwargs)
 |
 |  command_exploit(self
 *args
 **kwargs)
 |
 |  command_help(self
 *args
 **kwargs)
 |
 |  command_run(self
 *args
 **kwargs)
 |
 |  command_search(self
 *args
 **kwargs)
 |
 |  command_set(self
 *args
 **kwargs)
 |
 |  command_setg(self
 *args
 **kwargs)
 |
:
|  command_run(self
 *args
 **kwargs)
 |
 |  command_search(self
 *args
 **kwargs)
 |
 |  command_set(self
 *args
 **kwargs)
 |
 |  command_setg(self
 *args
 **kwargs)
 |
 |  command_show(self
 *args
 **kwargs)
 |
 |  command_unsetg(self
 *args
 **kwargs)
 |
 |  command_use(self
 module_path
 *args
 **kwargs)
 |
 |  complete_set(self
 *args
 **kwargs)
 |
 |  complete_setg(self
 *args
 **kwargs)
 |
 |  complete_show(self
 *args
 **kwargs)
 |
 |  complete_unsetg(self
 *args
 **kwargs)
 |
 |  complete_use(self
 *args
 **kwargs)
:
|  command_use(self
 module_path
 *args
 **kwargs)
 |
 |  complete_set(self
 *args
 **kwargs)
 |
 |  complete_setg(self
 *args
 **kwargs)
 |
 |  complete_show(self
 *args
 **kwargs)
 |
 |  complete_unsetg(self
 *args
 **kwargs)
 |
 |  complete_use(self
 *args
 **kwargs)
 |
 |  get_opts(self
 *args
 **kwargs)
 |      Generator returning modules Option attributes (option_name
 option_value
 option_description)
 |
 |      :param args: Option names
 |      :return:
:

 |      :param args: Option names
 |      :return:
 |
 |  suggested_commands(self)
 |      Entry point for intelligent tab completion.
 |
 |      Based on state of interpreter this method will return intelligent suggestions.
 |
:
 |      Generator returning modules Option attributes (option_name
 option_value
 option_description)
 |
 |      :param args: Option names
 |      :return:
 | |
 |  setup(self)
 |      Initialization of third-party libraries
 |
 |      Setting interpreter history.
 |      Setting appropriate completer function.
 |
 |      :return:
 |
 |  start(self)
 |      Routersploit main entry point. Starting interpreter loop.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseInterpreter:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from BaseInterpreter:
 |
 |  history_length = 100
(END)

 |  suggested_commands(self)
 |      Entry point for intelligent tab completion.
 |
 |      Based on state of interpreter this method will return intelligent suggestions.
 |
 |      :return: list of most accurate command suggestions
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  module_metadata
 |
 |  prompt
 |      Returns prompt string based on current_module attribute.
 |
 |      Adding module prefix (module.name) if current_module attribute is set.
 |
:
    Generator returning modules Option attributes (option_name
 option_value
 option_description)
 |
 |      :param args: Option names
 |      :return:
 |
 |  suggested_commands(self)
 |      Entry point for intelligent tab completion.
 |
 |      Based on state of interpreter this method will return intelligent suggestions.
 |
 |      :return: list of most accurate command suggestions
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  module_metadata
 |
 |  prompt
 |      Returns prompt string based on current_module attribute.
:
|  module_metadata
 |
 |  prompt
 |      Returns prompt string based on current_module attribute.
 |
 |      Adding module prefix (module.name) if current_module attribute is set.
 |
 |      :return: prompt string with appropriate module prefix.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  global_help =import Global commands:   help                       ...   ...
 |
 |  history_file =import /root/.rsf_history
 |
:
 |
 |  prompt
 |      Returns prompt string based on current_module attribute.
 |
 |      Adding module prefix (module.name) if current_module attribute is set.
 |
 |      :return: prompt string with appropriate module prefix.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  global_help =import Global commands:   help                       ...   ...
 |
 |  history_file =import /root/.rsf_history
 |
 |  module_help = "Module commands:   run                        ...rge...
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseInterpreter:
 |
 |  commands(self
 *ignored)
:
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseInterpreter:
 |
 |  commands(self
 *ignored)
 |      Returns full list of interpreter commands.
 |
 |      :param ignored:
 |      :return: full list of interpreter commands
 |
 |  complete(self
 text
 state)
 |      Return the next possible completion forimport text.
 |
 |      If a command has not been entered
 then complete against command list.
 |      Otherwise try to call complete_<command> to get list of completions.
 |
 |  default_completer(self
 *ignored)
 |
 |  get_command_handler(self
 command)
 |      Parsing command and returning appropriate handler.
:
|      Otherwise try to call complete_<command> to get list of completions.
 |
 |  default_completer(self
 *ignored)
 |
 |  get_command_handler(self
 command)
 |      Parsing command and returning appropriate handler.
 |
 |      :param command: command
 |      :return: command_handler
 |
 |  parse_line(self
 line)
 |      Split line into command and argument.
 |
 |      :param line: line to parse
 |      :return: (command
 argument)
 |
 |  raw_command_completer(self
 text
 line
 start_index
 end_index)
 |      Complete command w/o any argument
 |
 |  setup(self)
 |      Initialization of third-party libraries
|      :param line: line to parse
 |      :return: (command
 argument)
 |
 |  raw_command_completer(self
 text
 line
 start_index
 end_index)
 |      Complete command w/o any argument
 |
 |  setup(self)
 |      Initialization of third-party libraries
 |
 |      Setting interpreter history.
 |      Setting appropriate completer function.
 |
 |      :return:
 |
 |  start(self)
 |      Routersploit main entry point. Starting interpreter loop.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseInterpreter:

routersploit.interpreter.RoutersploitInterpreter().suggested_commands(self)
# Shell and Interpreter startup sequence
BaseInterpreter().__init__
RoutersploitInterpreter(BaseInterpreter).__init__

Help on method parse_line in module routersploit.interpreter:

parse_line(self
 line) unbound routersploit.interpreter.BaseInterpreter method
    Split line into command and argument.

    :param line: line to parse
    :return: (command
 argument)

>>> dir(BaseInterpreter)
[__class__
import __delattr__
import __dict__
import __doc__
import __format__
import __getattribute__
import __hash__
import __init__
import __module__
import __new__
import __reduce__
import __reduce_ex__
import __repr__
import __setattr__
import __sizeof__
import __str__
import __subclasshook__
import __weakref__
import commands
import complete
import default_completer
import get_command_handler
import global_help
import history_file
import history_length
import parse_line
import prompt
import raw_command_completer
import setupCopyright (c) 1991-1995 Stichting Mathematisch Centrum
 Amsterdam.
All Rights Reserved.
import NameError: <typeimport exceptions.NameError>
import BytesWarning: <typeimport exceptions.BytesWarning>
import dict: <typeimport dict>
import input: <built-in function input>
import oct: <built-in function oct>
import bin: <built-in function bin>
import SystemExit: <typeimport exceptions.SystemExit>
import StandardError: <typeimport exceptions.StandardError>
import format: <built-in function format>
import repr: <built-in function repr>
import __cffi_backend_extern_py: {140349544314048: (<ctypeimport int(*)(char *
 int
 int
 void *)>
 <function _pem_password_cb at 0x7fa5abac8398>
import \x00\x00\x00\x00\x00\x00\x00\x00
 None)}
import sorted: <built-in function sorted>
import False: False
import RuntimeWarning: <typeimport exceptions.RuntimeWarning>
import list: <typeimport list>
import iter: <built-in function iter>
import reload: <built-in function reload>
import Warning: <typeimport exceptions.Warning>
import __package__: None
import round: <built-in function round>
import dir: <built-in function dir>
import cmp: <built-in function cmp>
import set: <typeimport set>
import bytes: <typeimport str>
import reduce: <built-in function reduce>
import intern: <built-in function intern>
import issubclass: <built-in function issubclass>
import Ellipsis: Ellipsis
import EOFError: <typeimport exceptions.EOFError>
import locals: <built-in function locals>
import BufferError: <typeimport exceptions.BufferError>
import slice: <typeimport slice>
import FloatingPointError: <typeimport exceptions.FloatingPointError>
import sum: <built-in function sum>
import getattr: <built-in function getattr>
import abs: <built-in function abs>
import exit: Use exit() or Ctrl-D (i.e. EOF) to exit
import print: <built-in function print>
import True: True
import FutureWarning: <typeimport exceptions.FutureWarning>
import ImportWarning: <typeimport exceptions.ImportWarning>
import None: None
import hash: <built-in function hash>
import ReferenceError: <typeimport exceptions.ReferenceError>
import len: <built-in function len>
import credits:     Thanks to CWI
 CNRI
 BeOpen.com
 Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
import frozenset: <typeimport frozenset>
import __name__:import __builtin__
import ord: <built-in function ord>
import super: <typeimport super>
import _: None
import TypeError: <typeimport exceptions.TypeError>
import license: Type license() to see the full license text
import KeyboardInterrupt: <typeimport exceptions.KeyboardInterrupt>
import UserWarning: <typeimport exceptions.UserWarning>
import filter: <built-in function filter>
import range: <built-in function range>
import staticmethod: <typeimport staticmethod>
import SystemError: <typeimport exceptions.SystemError>
import BaseException: <typeimport exceptions.BaseException>
import pow: <built-in function pow>
import RuntimeError: <typeimport exceptions.RuntimeError>
import float: <typeimport float>
import MemoryError: <typeimport exceptions.MemoryError>
import StopIteration: <typeimport exceptions.StopIteration>
import globals: <built-in function globals>
import divmod: <built-in function divmod>
import enumerate: <typeimport enumerate>
import apply: <built-in function apply>
import LookupError: <typeimport exceptions.LookupError>
import open: <built-in function open>
import quit: Use quit() or Ctrl-D (i.e. EOF) to exit
import basestring: <typeimport basestring>
import UnicodeError: <typeimport exceptions.UnicodeError>
import zip: <built-in function zip>
import hex: <built-in function hex>
import long: <typeimport long>
import next: <built-in function next>
import ImportError: <typeimport exceptions.ImportError>
import chr: <built-in function chr>
import xrange: <typeimport xrange>
import type: <typeimport type>
import __doc__: "Built-in functions
 exceptions
 and other objects.\n\nNoteworthy: None is the `nil object; Ellipsis represents `... in slices."
import Exception: <typeimport exceptions.Exception>
import tuple: <typeimport tuple>
import UnicodeTranslateError: <typeimport exceptions.UnicodeTranslateError>
import reversed: <typeimport reversed>
import UnicodeEncodeError: <typeimport exceptions.UnicodeEncodeError>
import IOError: <typeimport exceptions.IOError>
import hasattr: <built-in function hasattr>
import delattr: <built-in function delattr>
import setattr: <built-in function setattr>
import raw_input: <built-in function raw_input>
import SyntaxWarning: <typeimport exceptions.SyntaxWarning>
import compile: <built-in function compile>
import ArithmeticError: <typeimport exceptions.ArithmeticError>
import str: <typeimport str>
import property: <typeimport property>
import GeneratorExit: <typeimport exceptions.GeneratorExit>
import int: <typeimport int>
import __import__: <built-in function __import__>
import KeyError: <typeimport exceptions.KeyError>
import coerce: <built-in function coerce>
import PendingDeprecationWarning: <typeimport exceptions.PendingDeprecationWarning>
import file: <typeimport file>
import EnvironmentError: <typeimport exceptions.EnvironmentError>
import unichr: <built-in function unichr>
import id: <built-in function id>
import OSError: <typeimport exceptions.OSError>
import DeprecationWarning: <typeimport exceptions.DeprecationWarning>
import min: <built-in function min>
import UnicodeWarning: <typeimport exceptions.UnicodeWarning>
import execfile: <built-in function execfile>
import any: <built-in function any>
import complex: <typeimport complex>
import bool: <typeimport bool>
import ValueError: <typeimport exceptions.ValueError>
import NotImplemented: NotImplemented
import map: <built-in function map>
import buffer: <typeimport buffer>
import max: <built-in function max>
import object: <typeimport object>
import TabError: <typeimport exceptions.TabError>
import callable: <built-in function callable>
import ZeroDivisionError: <typeimport exceptions.ZeroDivisionError>
import eval: <built-in function eval>
import __debug__: True
import IndentationError: <typeimport exceptions.IndentationError>
import AssertionError: <typeimport exceptions.AssertionError>
import classmethod: <typeimport classmethod>
import UnboundLocalError: <typeimport exceptions.UnboundLocalError>
import NotImplementedError: <typeimport exceptions.NotImplementedError>
import AttributeError: <typeimport exceptions.AttributeError>
import OverflowError: <typeimport exceptions.OverflowError>}
import __file__:import routersploit/modules/__init__.pyc
import __package__: None
import __path__: [routersploit/modules]
import __name__:import routersploit.modules
import __author__:import fwkz
import __doc__: None}



# NEW DIRECTORY
 routersploit/routersploit

Copyright (c) 1991-1995 Stichting Mathematisch Centrum
 Amsterdam.
All Rights Reserved.
import NameError: <typeimport exceptions.NameError>
import BytesWarning: <typeimport exceptions.BytesWarning>
import dict: <typeimport dict>
import input: <built-in function input>
import oct: <built-in function oct>
import bin: <built-in function bin>
import SystemExit: <typeimport exceptions.SystemExit>
import StandardError: <typeimport exceptions.StandardError>
import format: <built-in function format>
import repr: <built-in function repr>
import __cffi_backend_extern_py: {140349544314048: (<ctypeimport int(*)(char *
 int
 int
 void *)>
 <function _pem_password_cb at 0x7fa5abac8398>
import \x00\x00\x00\x00\x00\x00\x00\x00
 None)}
import sorted: <built-in function sorted>
import False: False
import RuntimeWarning: <typeimport exceptions.RuntimeWarning>
import list: <typeimport list>
import iter: <built-in function iter>
import reload: <built-in function reload>
import Warning: <typeimport exceptions.Warning>
import __package__: None
import round: <built-in function round>
import dir: <built-in function dir>
import cmp: <built-in function cmp>
import set: <typeimport set>
import bytes: <typeimport str>
import reduce: <built-in function reduce>
import intern: <built-in function intern>
import issubclass: <built-in function issubclass>
import Ellipsis: Ellipsis
import EOFError: <typeimport exceptions.EOFError>
import locals: <built-in function locals>
import BufferError: <typeimport exceptions.BufferError>
import slice: <typeimport slice>
import FloatingPointError: <typeimport exceptions.FloatingPointError>
import sum: <built-in function sum>
import getattr: <built-in function getattr>
import abs: <built-in function abs>
import exit: Use exit() or Ctrl-D (i.e. EOF) to exit
import print: <built-in function print>
import True: True
import FutureWarning: <typeimport exceptions.FutureWarning>
import ImportWarning: <typeimport exceptions.ImportWarning>
import None: None
import hash: <built-in function hash>
import ReferenceError: <typeimport exceptions.ReferenceError>
import len: <built-in function len>
import credits:     Thanks to CWI
 CNRI
 BeOpen.com
 Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
import frozenset: <typeimport frozenset>
import __name__:import __builtin__
import ord: <built-in function ord>
import super: <typeimport super>
import _: None
import TypeError: <typeimport exceptions.TypeError>
import license: Type license() to see the full license text
import KeyboardInterrupt: <typeimport exceptions.KeyboardInterrupt>
import UserWarning: <typeimport exceptions.UserWarning>
import filter: <built-in function filter>
import range: <built-in function range>
import staticmethod: <typeimport staticmethod>
import SystemError: <typeimport exceptions.SystemError>
import BaseException: <typeimport exceptions.BaseException>
import pow: <built-in function pow>
import RuntimeError: <typeimport exceptions.RuntimeError>
import float: <typeimport float>
import MemoryError: <typeimport exceptions.MemoryError>
import StopIteration: <typeimport exceptions.StopIteration>
import globals: <built-in function globals>
import divmod: <built-in function divmod>
import enumerate: <typeimport enumerate>
import apply: <built-in function apply>
import LookupError: <typeimport exceptions.LookupError>
import open: <built-in function open>
import quit: Use quit() or Ctrl-D (i.e. EOF) to exit
import basestring: <typeimport basestring>
import UnicodeError: <typeimport exceptions.UnicodeError>
import zip: <built-in function zip>
import hex: <built-in function hex>
import long: <typeimport long>
import next: <built-in function next>
import ImportError: <typeimport exceptions.ImportError>
import chr: <built-in function chr>
import xrange: <typeimport xrange>
import type: <typeimport type>
import __doc__: "Built-in functions

 >> globals()
{exploits: <moduleimport routersploit.exploits fromimport routersploit/exploits.pyc>
import mute: <function mute at 0x7fa5ab7b7230>
import random: <moduleimport random fromimport /usr/lib/python2.7/random.pyc>
import BasePayload: <classimport routersploit.payloads.BasePayload>
import ArchitectureSpecificPayload: <classimport routersploit.payloads.ArchitectureSpecificPayload>
import HttpRequestHandler: <class shell.HttpRequestHandler at 0x7fa5ab6c6050>
import colors: {blue: 34
import green: 32
import yellow: 33
import cyan: 36
import magenta: 35
import white: 37
import grey: 30
import red: 31}
import validators: <moduleimport routersploit.validators fromimport routersploit/validators.pyc>

 # so its true
 it does not work until you get to here
 the second directory.
import interpreter: <moduleimport routersploit.interpreter fromimport routersploit/interpreter.pyc>
import BindTCPPayloadMixin: <classimport routersploit.payloads.BindTCPPayloadMixin>
import wraps: <function wraps at 0x7fa5af7650c8>
import importlib: <moduleimport importlib fromimport /usr/lib/python2.7/importlib/__init__.pyc>
import re: <moduleimport re fromimport /usr/lib/python2.7/re.pyc>
import routersploit_installation:import /root/Documents/routersploit
import collections: <moduleimport collections fromimport /usr/lib/python2.7/collections.pyc>
import ARCH_ELF_HEADERS: {armle:import \x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00(\x00\x01\x00\x00\x00T\x80\x00\x004\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004\x00 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x80\x00\x00\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00\x00\x10\x00\x00
import mipsbe:import \x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00\x00\x00\x01\x00@\x00T\x00\x00\x004\x00\x00\x00\x00\x00\x00\x00\x00\x004\x00 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00@\x00\x00\x00@\x00\x00\xde\xad\xbe\xef\xde\xad\xbe\xef\x00\x00\x00\x07\x00\x00\x10\x00
import mipsle:import \x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00\x01\x00\x00\x00T\x00@\x004\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004\x00 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00@\x00\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00\x00\x10\x00\x00}
import RoutersploitException: <classimport routersploit.exceptions.RoutersploitException>
import namedtuple: <function namedtuple at 0x7fa5ad7e92a8>
import PayloadHandlers: PayloadHandlers(BIND_TCP=bind_tcp
 REVERSE_TCP=reverse_tcp)
import string: <moduleimport string fromimport /usr/lib/python2.7/string.pyc>
import absolute_import: _Feature((2
 5
 0
import alpha
 1)
 (3
 0
 0
import alpha
 0)
 16384)
import payload_handlers: <classimport routersploit.payloads.PayloadHandlers>
import stop_after: <function stop_after at 0x7fa5ab7b71b8>
import LockedIterator: <classimport routersploit.utils.LockedIterator>
import ThreadPoolExecutor: <classimport routersploit.threads.ThreadPoolExecutor>
import iter_modules: <function iter_modules at 0x7fa5ab79bf50>
import import_exploit: <function import_exploit at 0x7fa5ab79bed8>
import humanize_path: <function humanize_path at 0x7fa5ab7b70c8>
import index_modules: <function index_modules at 0x7fa5ab79bb18>
import threading: <moduleimport threading fromimport /usr/lib/python2.7/threading.pyc>
import MODULES_DIR:import routersploit/modules
import SimpleHTTPServer: <moduleimport SimpleHTTPServer fromimport /usr/lib/python2.7/SimpleHTTPServer.pyc>
import atexit: <moduleimport atexit fromimport /usr/lib/python2.7/atexit.pyc>
import BaseHTTPServer: <moduleimport BaseHTTPServer fromimport /usr/lib/python2.7/BaseHTTPServer.pyc>
import Resource: <classimport routersploit.utils.Resource>
import print_lock: <thread.lock object at 0x7fa5acc55530>
import isfile: <function isfile at 0x7fa5af7e3050>
import sanitize_url: <function sanitize_url at 0x7fa5ab7b7a28>
import BaseInterpreter: <classimport routersploit.interpreter.BaseInterpreter>
import HttpServer: <class shell.HttpServer at 0x7fa5ab6c60b8>
import WeakKeyDictionary: <class weakref.WeakKeyDictionary at 0x7fa5ad562bb0>
import GenericPayload: <classimport routersploit.payloads.GenericPayload>
import Architectures: ArchitectureType(ARMLE=armle
 MIPSBE=mipsbe
 MIPSLE=mipsle)
import http_request: <function http_request at 0x7fa5ab7b7b90>
import inspect: <moduleimport inspect fromimport /usr/lib/python2.7/inspect.pyc>
import ReverseTCPPayloadMixin: <classimport routersploit.payloads.ReverseTCPPayloadMixin>
import Counter: <classimport collections.Counter>
import data_queue: <Queue.Queue instance at 0x7fa5ab769ab8>
import create_exploit: <function create_exploit at 0x7fa5ab7b7e60>
import threads: <moduleimport routersploit.threads fromimport routersploit/threads.pyc>
import __name__:import __main__
import mkdir_p: <function mkdir_p at 0x7fa5ab7b7f50>
import PrintResource: <classimport routersploit.utils.PrintResource>
import print_function: _Feature((2
 6
 0
import alpha
 2)
 (3
 0
 0
import alpha
 0)
 65536)
import create_resource: <function create_resource at 0x7fa5ab7b7ed8>
import socket: <moduleimport socket fromimport /usr/lib/python2.7/socket.pyc>
import Communication: <classimport shell.Communication>
import traceback: <moduleimport traceback fromimport /usr/lib/python2.7/traceback.pyc>
import routersploit: <moduleimport routersploit fromimport routersploit/__init__.pyc>
import queue: <moduleimport queue fromimport /usr/lib/python2.7/dist-packages/queue/__init__.pyc>
import itertools: <moduleimport itertools (built-in)>
import telnetlib: <moduleimport telnetlib fromimport /usr/lib/python2.7/telnetlib.pyc>
import requests: <moduleimport requests fromimport /usr/lib/python2.7/dist-packages/requests/__init__.pyc>
import os: <moduleimport os fromimport /usr/lib/python2.7/os.pyc>
import unittest: <moduleimport unittest fromimport /usr/lib/python2.7/unittest/__init__.pyc>
import rsf_modules: <moduleimport routersploit.modules fromimport routersploit/modules/__init__.pyc>
import __builtin__: <moduleimport __builtin__ (built-in)>
import print_error: <function print_error at 0x7fa5ab7b7410>
import operator: <moduleimport operator (built-in)>
import select: <moduleimport select (built-in)>
import NonStringIterable: <classimport routersploit.utils.NonStringIterable>
import wordlists: <moduleimport routersploit.wordlists fromimport routersploit/wordlists/__init__.pyc>
import StopThreadPoolExecutor: <classimport routersploit.exceptions.StopThreadPoolExecutor>
import errno: <moduleimport errno (built-in)>
import thread_output_stream: <WeakKeyDictionary at 140349523642560>
import ABCMeta: <classimport abc.ABCMeta>
import windows_shell: <function windows_shell at 0x7fa5ab7b7d70>
import tokenize: <function tokenize at 0x7fa5ab7b7de8>
import posix_shell: <function posix_shell at 0x7fa5ab7b7cf8>
import __doc__: None
import module_required: <function module_required at 0x7fa5ab7b7140>
import print_status: <function print_status at 0x7fa5ab7b7488>
import shell: <function shell at 0x7fa5ab751230>
import OptionValidationError: <classimport routersploit.exceptions.OptionValidationError>
import printer_queue: <Queue.Queue instance at 0x7fa5ab6a3440>
import logging: <moduleimport logging fromimport /usr/lib/python2.7/logging/__init__.pyc>
import multi: <function multi at 0x7fa5ab7b7320>
import join: <function join at 0x7fa5af7eb050>
import main_routersploit_installation_dir:import /root/Documents/routersploit
import print_info: <function print_info at 0x7fa5ab7b7578>
import GLOBAL_OPTS: {}
import exceptions: <moduleimport routersploit.exceptions fromimport routersploit/exceptions.pyc>
import random_text: <function random_text at 0x7fa5ab7b7b18>
import pack: <built-in function pack>
import pythonize_path: <function pythonize_path at 0x7fa5ab7b7050>
import PrinterThread: <classimport routersploit.printer.PrinterThread>
import RoutersploitTestCase: <classimport tests.test_case.RoutersploitTestCase>
import utils: <moduleimport routersploit.utils fromimport routersploit/utils/__init__.pyc>
import WorkerThread: <classimport routersploit.threads.WorkerThread>
import RoutersploitInterpreter: <classimport routersploit.interpreter.RoutersploitInterpreter>
import CREDS_DIR:import routersploit/modules/creds
import __package__: None
import payloads: <moduleimport routersploit.payloads fromimport routersploit/payloads.pyc>
import print_success: <function print_success at 0x7fa5ab7b7500>
import listdir: <built-in function listdir>
import printer: <moduleimport routersploit.printer fromimport routersploit/printer.pyc>
import ssh_interactive: <function ssh_interactive at 0x7fa5ab7b7c80>
import abstractmethod: <function abstractmethod at 0x7fa5af7f9500>
import DummyFile: <classimport routersploit.utils.DummyFile>
import __builtins__: <moduleimport __builtin__ (built-in)>
import sys: <moduleimport sys (built-in)>
import pprint_dict_in_order: <function pprint_dict_in_order at 0x7fa5ab7b7aa0>
import architectures: <classimport routersploit.payloads.ArchitectureType>
import data_producing: <threading._Event object at 0x7fa5ab76ced0>
import boolify: <function boolify at 0x7fa5ab7b7c08>
import readline: <moduleimport readline fromimport /usr/lib/python2.7/lib-dynload/readline.x86_64-linux-gnu.so>
import strtobool: <function strtobool at 0x7fa5ad545410>
import EXPLOITS_DIR:import routersploit/modules/exploits
import SCANNERS_DIR:import routersploit/modules/scanners
import modules: <moduleimport routersploit.modules fromimport routersploit/modules/__init__.pyc>
import print_table: <function print_table at 0x7fa5ab7b79b0>
import Exploit: <classimport routersploit.exploits.Exploit>
import time: <moduleimport time (built-in)>}
>>>

 exceptions
 and other objects.\n\nNoteworthy: None is the `nil object; Ellipsis represents `... in slices."
import Exception: <typeimport exceptions.Exception>
import tuple: <typeimport tuple>
import UnicodeTranslateError: <typeimport exceptions.UnicodeTranslateError>
import reversed: <typeimport reversed>
import UnicodeEncodeError: <typeimport exceptions.UnicodeEncodeError>
import IOError: <typeimport exceptions.IOError>
import hasattr: <built-in function hasattr>
import delattr: <built-in function delattr>
import setattr: <built-in function setattr>
import raw_input: <built-in function raw_input>
import SyntaxWarning: <typeimport exceptions.SyntaxWarning>
import compile: <built-in function compile>
import ArithmeticError: <typeimport exceptions.ArithmeticError>
import str: <typeimport str>
import property: <typeimport property>
import GeneratorExit: <typeimport exceptions.GeneratorExit>
import int: <typeimport int>
import __import__: <built-in function __import__>
import KeyError: <typeimport exceptions.KeyError>
import coerce: <built-in function coerce>
import PendingDeprecationWarning: <typeimport exceptions.PendingDeprecationWarning>
import file: <typeimport file>
import EnvironmentError: <typeimport exceptions.EnvironmentError>
import unichr: <built-in function unichr>
import id: <built-in function id>
import OSError: <typeimport exceptions.OSError>
import DeprecationWarning: <typeimport exceptions.DeprecationWarning>
import min: <built-in function min>
import UnicodeWarning: <typeimport exceptions.UnicodeWarning>
import execfile: <built-in function execfile>
import any: <built-in function any>
import complex: <typeimport complex>
import bool: <typeimport bool>
import ValueError: <typeimport exceptions.ValueError>
import NotImplemented: NotImplemented
import map: <built-in function map>
import buffer: <typeimport buffer>
import max: <built-in function max>
import object: <typeimport object>
import TabError: <typeimport exceptions.TabError>
import callable: <built-in function callable>
import ZeroDivisionError: <typeimport exceptions.ZeroDivisionError>
import eval: <built-in function eval>
import __debug__: True
import IndentationError: <typeimport exceptions.IndentationError>
import AssertionError: <typeimport exceptions.AssertionError>
import classmethod: <typeimport classmethod>
import UnboundLocalError: <typeimport exceptions.UnboundLocalError>
import NotImplementedError: <typeimport exceptions.NotImplementedError>
import AttributeError: <typeimport exceptions.AttributeError>
import OverflowError: <typeimport exceptions.OverflowError>}
import __file__:import routersploit/modules/__init__.pyc
import __package__: None
import __path__: [routersploit/modules]
import __name__:import routersploit.modules
import __author__:import fwkz
import __doc__: None}

import start
import suggested_commands]
>>>

[(__add__
 <method-wrapperimport __add__ of str object at 0x7fa5ad3ffcc0>)
 (__class__
 <typeimport str>)
 (__contains__
 <method-wrapperimport __contains__ of str object at 0x7fa5ad3ffcc0>)
 (__delattr__
 <method-wrapperimport __delattr__ of str object at 0x7fa5ad3ffcc0>)
 (__doc__
 "str(object=) -> string\n\nReturn a nice string representation of the object.\nIf the argument is a string
 the return value is the same object.")
 (__eq__
 <method-wrapperimport __eq__ of str object at 0x7fa5ad3ffcc0>)
 (__format__
 <built-in method __format__ of str object at 0x7fa5ad3ffcc0>)
 (__ge__
 <method-wrapperimport __ge__ of str object at 0x7fa5ad3ffcc0>)
 (__getattribute__
 <method-wrapperimport __getattribute__ of str object at 0x7fa5ad3ffcc0>)
 (__getitem__
 <method-wrapperimport __getitem__ of str object at 0x7fa5ad3ffcc0>)
 (__getnewargs__
 <built-in method __getnewargs__ of str object at 0x7fa5ad3ffcc0>)
 (__getslice__
 <method-wrapperimport __getslice__ of str object at 0x7fa5ad3ffcc0>)
 (__gt__
 <method-wrapperimport __gt__ of str object at 0x7fa5ad3ffcc0>)
 (__hash__
 <method-wrapperimport __hash__ of str object at 0x7fa5ad3ffcc0>)
 (__init__
 <method-wrapperimport __init__ of str object at 0x7fa5ad3ffcc0>)
 (__le__
 <method-wrapperimport __le__ of str object at 0x7fa5ad3ffcc0>)
 (__len__
 <method-wrapperimport __len__ of str object at 0x7fa5ad3ffcc0>)
 (__lt__
 <method-wrapperimport __lt__ of str object at 0x7fa5ad3ffcc0>)
 (__mod__
 <method-wrapperimport __mod__ of str object at 0x7fa5ad3ffcc0>)
 (__mul__
 <method-wrapperimport __mul__ of str object at 0x7fa5ad3ffcc0>)
 (__ne__
 <method-wrapperimport __ne__ of str object at 0x7fa5ad3ffcc0>)
 (__new__
 <built-in method __new__ of type object at 0x562255a3e7e0>)
 (__reduce__
 <built-in method __reduce__ of str object at 0x7fa5ad3ffcc0>)
 (__reduce_ex__
 <built-in method __reduce_ex__ of str object at 0x7fa5ad3ffcc0>)
 (__repr__
 <method-wrapperimport __repr__ of str object at 0x7fa5ad3ffcc0>)
 (__rmod__
 <method-wrapperimport __rmod__ of str object at 0x7fa5ad3ffcc0>)
 (__rmul__
 <method-wrapperimport __rmul__ of str object at 0x7fa5ad3ffcc0>)
 (__setattr__
 <method-wrapperimport __setattr__ of str object at 0x7fa5ad3ffcc0>)
 (__sizeof__
 <built-in method __sizeof__ of str object at 0x7fa5ad3ffcc0>)
 (__str__
 <method-wrapperimport __str__ of str object at 0x7fa5ad3ffcc0>)
 (__subclasshook__
 <built-in method __subclasshook__ of type object at 0x562255a3e7e0>)
 (_formatter_field_name_split
 <built-in method _formatter_field_name_split of str object at 0x7fa5ad3ffcc0>)
 (_formatter_parser
 <built-in method _formatter_parser of str object at 0x7fa5ad3ffcc0>)
 (capitalize
 <built-in method capitalize of str object at 0x7fa5ad3ffcc0>)
 (center
 <built-in method center of str object at 0x7fa5ad3ffcc0>)
 (count
 <built-in method count of str object at 0x7fa5ad3ffcc0>)
 (decode
 <built-in method decode of str object at 0x7fa5ad3ffcc0>)
 (encode
 <built-in method encode of str object at 0x7fa5ad3ffcc0>)
 (endswith
 <built-in method endswith of str object at 0x7fa5ad3ffcc0>)
 (expandtabs
 <built-in method expandtabs of str object at 0x7fa5ad3ffcc0>)
 (find
 <built-in method find of str object at 0x7fa5ad3ffcc0>)
 (format
 <built-in method format of str object at 0x7fa5ad3ffcc0>)
 (index
 <built-in method index of str object at 0x7fa5ad3ffcc0>)
 (isalnum
 <built-in method isalnum of str object at 0x7fa5ad3ffcc0>)
 (isalpha
 <built-in method isalpha of str object at 0x7fa5ad3ffcc0>)
 (isdigit
 <built-in method isdigit of str object at 0x7fa5ad3ffcc0>)
 (islower
 <built-in method islower of str object at 0x7fa5ad3ffcc0>)
 (isspace
 <built-in method isspace of str object at 0x7fa5ad3ffcc0>)
 (istitle
 <built-in method istitle of str object at 0x7fa5ad3ffcc0>)
 (isupper
 <built-in method isupper of str object at 0x7fa5ad3ffcc0>)
 (join
 <built-in method join of str object at 0x7fa5ad3ffcc0>)
 (ljust
 <built-in method ljust of str object at 0x7fa5ad3ffcc0>)
 (lower
 <built-in method lower of str object at 0x7fa5ad3ffcc0>)
 (lstrip
 <built-in method lstrip of str object at 0x7fa5ad3ffcc0>)
 (partition
 <built-in method partition of str object at 0x7fa5ad3ffcc0>)
 (replace
 <built-in method replace of str object at 0x7fa5ad3ffcc0>)
 (rfind
 <built-in method rfind of str object at 0x7fa5ad3ffcc0>)
 (rindex
 <built-in method rindex of str object at 0x7fa5ad3ffcc0>)
 (rjust
 <built-in method rjust of str object at 0x7fa5ad3ffcc0>)
 (rpartition
 <built-in method rpartition of str object at 0x7fa5ad3ffcc0>)
 (rsplit
 <built-in method rsplit of str object at 0x7fa5ad3ffcc0>)
 (rstrip
 <built-in method rstrip of str object at 0x7fa5ad3ffcc0>)
 (split
 <built-in method split of str object at 0x7fa5ad3ffcc0>)
 (splitlines
 <built-in method splitlines of str object at 0x7fa5ad3ffcc0>)
 (startswith
 <built-in method startswith of str object at 0x7fa5ad3ffcc0>)
 (strip
 <built-in method strip of str object at 0x7fa5ad3ffcc0>)
 (swapcase
 <built-in method swapcase of str object at 0x7fa5ad3ffcc0>)
 (title
 <built-in method title of str object at 0x7fa5ad3ffcc0>)
 (translate
 <built-in method translate of str object at 0x7fa5ad3ffcc0>)
 (upper
 <built-in method upper of str object at 0x7fa5ad3ffcc0>)
 (zfill
 <built-in method zfill of str object at 0x7fa5ad3ffcc0>)]

opyright (c) 1991-1995 Stichting Mathematisch Centrum
 Amsterdam.
All Rights Reserved.
import NameError: <typeimport exceptions.NameError>
import BytesWarning: <typeimport exceptions.BytesWarning>
import dict: <typeimport dict>
import input: <built-in function input>
import oct: <built-in function oct>
import bin: <built-in function bin>
import SystemExit: <typeimport exceptions.SystemExit>
import StandardError: <typeimport exceptions.StandardError>
import format: <built-in function format>
import repr: <built-in function repr>
import __cffi_backend_extern_py: {140349544314048: (<ctypeimport int(*)(char *
 int
 int
 void *)>
 <function _pem_password_cb at 0x7fa5abac8398>
import \x00\x00\x00\x00\x00\x00\x00\x00
 None)}
import sorted: <built-in function sorted>
import False: False
import RuntimeWarning: <typeimport exceptions.RuntimeWarning>
import list: <typeimport list>
import iter: <built-in function iter>
import reload: <built-in function reload>
import Warning: <typeimport exceptions.Warning>
import __package__: None
import round: <built-in function round>
import dir: <built-in function dir>
import cmp: <built-in function cmp>
import set: <typeimport set>
import bytes: <typeimport str>
import reduce: <built-in function reduce>
import intern: <built-in function intern>
import issubclass: <built-in function issubclass>
import Ellipsis: Ellipsis
import EOFError: <typeimport exceptions.EOFError>
import locals: <built-in function locals>
import BufferError: <typeimport exceptions.BufferError>
import slice: <typeimport slice>
import FloatingPointError: <typeimport exceptions.FloatingPointError>
import sum: <built-in function sum>
import getattr: <built-in function getattr>
import abs: <built-in function abs>
import exit: Use exit() or Ctrl-D (i.e. EOF) to exit
import print: <built-in function print>
import True: True
import FutureWarning: <typeimport exceptions.FutureWarning>
import ImportWarning: <typeimport exceptions.ImportWarning>
import None: None
import hash: <built-in function hash>
import ReferenceError: <typeimport exceptions.ReferenceError>
import len: <built-in function len>
import credits:     Thanks to CWI
 CNRI
 BeOpen.com
 Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
import frozenset: <typeimport frozenset>
import __name__:import __builtin__
import ord: <built-in function ord>
import super: <typeimport super>
import _: None
import TypeError: <typeimport exceptions.TypeError>
import license: Type license() to see the full license text
import KeyboardInterrupt: <typeimport exceptions.KeyboardInterrupt>
import UserWarning: <typeimport exceptions.UserWarning>
import filter: <built-in function filter>
import range: <built-in function range>
import staticmethod: <typeimport staticmethod>
import SystemError: <typeimport exceptions.SystemError>
import BaseException: <typeimport exceptions.BaseException>
import pow: <built-in function pow>
import RuntimeError: <typeimport exceptions.RuntimeError>
import float: <typeimport float>
import MemoryError: <typeimport exceptions.MemoryError>
import StopIteration: <typeimport exceptions.StopIteration>
import globals: <built-in function globals>
import divmod: <built-in function divmod>
import enumerate: <typeimport enumerate>
import apply: <built-in function apply>
import LookupError: <typeimport exceptions.LookupError>
import open: <built-in function open>
import quit: Use quit() or Ctrl-D (i.e. EOF) to exit
import basestring: <typeimport basestring>
import UnicodeError: <typeimport exceptions.UnicodeError>
import zip: <built-in function zip>
import hex: <built-in function hex>
import long: <typeimport long>
import next: <built-in function next>
import ImportError: <typeimport exceptions.ImportError>
import chr: <built-in function chr>
import xrange: <typeimport xrange>
import type: <typeimport type>
import __doc__: "Built-in functions
 exceptions
 and other objects.\n\nNoteworthy: None is the `nil object; Ellipsis represents `... in slices."
import Exception: <typeimport exceptions.Exception>
import tuple: <typeimport tuple>
import UnicodeTranslateError: <typeimport exceptions.UnicodeTranslateError>
import reversed: <typeimport reversed>
import UnicodeEncodeError: <typeimport exceptions.UnicodeEncodeError>
import IOError: <typeimport exceptions.IOError>
import hasattr: <built-in function hasattr>
import delattr: <built-in function delattr>
import setattr: <built-in function setattr>
import raw_input: <built-in function raw_input>
import SyntaxWarning: <typeimport exceptions.SyntaxWarning>
import compile: <built-in function compile>
import ArithmeticError: <typeimport exceptions.ArithmeticError>
import str: <typeimport str>
import property: <typeimport property>
import GeneratorExit: <typeimport exceptions.GeneratorExit>
import int: <typeimport int>
import __import__: <built-in function __import__>
import KeyError: <typeimport exceptions.KeyError>
import coerce: <built-in function coerce>
import PendingDeprecationWarning: <typeimport exceptions.PendingDeprecationWarning>
import file: <typeimport file>
import EnvironmentError: <typeimport exceptions.EnvironmentError>
import unichr: <built-in function unichr>
import id: <built-in function id>
import OSError: <typeimport exceptions.OSError>
import DeprecationWarning: <typeimport exceptions.DeprecationWarning>
import min: <built-in function min>
import UnicodeWarning: <typeimport exceptions.UnicodeWarning>
import execfile: <built-in function execfile>
import any: <built-in function any>
import complex: <typeimport complex>
import bool: <typeimport bool>
import ValueError: <typeimport exceptions.ValueError>
import NotImplemented: NotImplemented
import map: <built-in function map>
import buffer: <typeimport buffer>
import max: <built-in function max>
import object: <typeimport object>
import TabError: <typeimport exceptions.TabError>
import callable: <built-in function callable>
import ZeroDivisionError: <typeimport exceptions.ZeroDivisionError>
import eval: <built-in function eval>
import __debug__: True
import IndentationError: <typeimport exceptions.IndentationError>
import AssertionError: <typeimport exceptions.AssertionError>
import classmethod: <typeimport classmethod>
import UnboundLocalError: <typeimport exceptions.UnboundLocalError>
import NotImplementedError: <typeimport exceptions.NotImplementedError>
import AttributeError: <typeimport exceptions.AttributeError>
import OverflowError: <typeimport exceptions.OverflowError>}
import Traceback: <classimport inspect.Traceback>
import findsource: <function findsource at 0x7fa5ac668aa0>
import _searchbases: <function _searchbases at 0x7fa5ac668230>
import ModuleInfo: <classimport inspect.ModuleInfo>
import __name__:import inspect
import joinseq: <function joinseq at 0x7fa5ac614aa0>
import getsourcefile: <function getsourcefile at 0x7fa5ac668938>
import os: <moduleimport os fromimport /usr/lib/python2.7/os.pyc>
import getinnerframes: <function getinnerframes at 0x7fa5ac6245f0>
import ismemberdescriptor: <function ismemberdescriptor at 0x7fa5ac66d848>
import getabsfile: <function getabsfile at 0x7fa5ac6689b0>
import isabstract: <function isabstract at 0x7fa5ac66dcf8>
import isbuiltin: <function isbuiltin at 0x7fa5ac66dc08>
import tokenize: <moduleimport tokenize fromimport /usr/lib/python2.7/tokenize.pyc>
import isfunction: <function isfunction at 0x7fa5ac66d938>
import __doc__: "Get useful information from live Python objects.\n\nThis module encapsulates the interface provided by the internal special\nattributes (func_*
 co_*
 im_*
 tb_*
 etc.) in a friendlier fashion.\nIt also provides some help for examining source code and class layout.\n\nHere are some of the useful functions provided by this module:\n   ismodule()
 isclass()
 ismethod()
 isfunction()
 isgeneratorfunction()
       isgenerator()
 istraceback()
 isframe()
 iscode()
 isbuiltin()
       isroutine() - check object types   getmembers() - get members of an object that satisfy a given condition\n   getfile()
 getsourcefile()
 getsource() - find an objects source code   getdoc()
 getcomments() - get documentation on an object   getmodule() - determine the module that an object came from   getclasstree() - arrange classes so as to represent their hierarchy\n   getargspec()
 getargvalues()
 getcallargs() - get info about function arguments   formatargspec()
 formatargvalues() - format an argument spec   getouterframes()
 getinnerframes() - get info about frames   currentframe() - get the current stack frame   stack()
 trace() - get info about frames on the stack or in a traceback\n"
import istraceback: <function istraceback at 0x7fa5ac66daa0>
import getmoduleinfo: <function getmoduleinfo at 0x7fa5ac668500>
import __author__:import Ka-Ping Yee <ping@lfw.org>
import isgeneratorfunction: <function isgeneratorfunction at 0x7fa5ac66d9b0>
import getargs: <function getargs at 0x7fa5ac668ed8>
import CO_GENERATOR: 32
import cleandoc: <function cleandoc at 0x7fa5ac668410>
import classify_class_attrs: <function classify_class_attrs at 0x7fa5ac66dde8>
import Attribute: <classimport inspect.Attribute>
import walktree: <function walktree at 0x7fa5ac668de8>
import getmodule: <function getmodule at 0x7fa5ac668a28>
import ismethod: <function ismethod at 0x7fa5ac66d6e0>
import formatargvalues: <function formatargvalues at 0x7fa5ac614ed8>
import indentsize: <function indentsize at 0x7fa5ac668320>
import getmodulename: <function getmodulename at 0x7fa5ac6688c0>
import Arguments: <classimport inspect.Arguments>
import CO_NEWLOCALS: 2
import iscode: <function iscode at 0x7fa5ac66db90>
import formatargspec: <function formatargspec at 0x7fa5ac614cf8>
import getlineno: <function getlineno at 0x7fa5ac624500>
import CO_VARKEYWORDS: 8
import __package__: None
import CO_VARARGS: 4
import ArgSpec: <classimport inspect.ArgSpec>
import getargvalues: <function getargvalues at 0x7fa5ac6146e0>
import trace: <function trace at 0x7fa5ac6246e0>
import isclass: <function isclass at 0x7fa5ac66d668>
import ismethoddescriptor: <function ismethoddescriptor at 0x7fa5ac66d758>
import sys: <moduleimport sys (built-in)>
import isroutine: <function isroutine at 0x7fa5ac66dc80>
import stack: <function stack at 0x7fa5ac624668>
import types: <moduleimport types fromimport /usr/lib/python2.7/types.pyc>
import getdoc: <function getdoc at 0x7fa5ac668398>
import ismodule: <function ismodule at 0x7fa5ac66d5f0>
import linecache: <moduleimport linecache fromimport /usr/lib/python2.7/linecache.pyc>
import isgetsetdescriptor: <function isgetsetdescriptor at 0x7fa5ac66d8c0>
import getblock: <function getblock at 0x7fa5ac668b90>}

RoutersploitInterpreter.__dict__
dict_proxy({command_search
: <function command_search at 0x7f81bf9807d0>
RoutersploitInterpreter.__module__:RoutersploitInterpreter.routersploit.interpreter
RoutersploitInterpreter.prompt
: <property object at 0x7f81bf9d5e10>
RoutersploitInterpreter._show_creds
: <function _show_creds at 0x7f81bf980410>
RoutersploitInterpreter.command_exit
: <function command_exit at 0x7f81bf980848>
RoutersploitInterpreter.command_show
: <function command_show at 0x7f81bf980488>
RoutersploitInterpreter.complete_setg
: <function complete_setg at 0x7f81bf97ec08>
RoutersploitInterpreter.suggested_commands
: <function suggested_commands at 0x7f81bf97e488>
RoutersploitInterpreter.command_setg
: <function command_setg at 0x7f81bf97eaa0>
RoutersploitInterpreter.command_run
: <function command_run at 0x7f81bf97e758>
RoutersploitInterpreter.command_unsetg
: <function command_unsetg at 0x7f81bf97ec80>
RoutersploitInterpreter._RoutersploitInterpreter__parse_prompt
: <function __parse_prompt at 0x7f81bf97e230>
RoutersploitInterpreter.complete_set
: <function complete_set at 0x7f81bf97ea28>
RoutersploitInterpreter._extend_with_global_commands
: <function _extend_with_global_commands at 0x7f81bf97e2a8>
RoutersploitInterpreter._RoutersploitInterpreter__show_modules
: <function __show_modules at 0x7f81bf980230>
RoutersploitInterpreter.command_set
: <function command_set at 0x7f81bf97e8c0>
RoutersploitInterpreter.module_help: "Module commands:   run                                 Run the selected module with the given options   back                                De-select the current module   set <option name> <option value>    Set an option for the selected module   setg <option name> <option value>   Set an option for all of the modules   unsetg <option name>                Unset option that was set globally   show [info|options|devices]         Print information
 options
 or target devices for a module   check                               Check if a given target is vulnerable to a selected modules exploit"
RoutersploitInterpreter.complete_show
: <function complete_show at 0x7f81bf9805f0>
RoutersploitInterpreter.command_back
: <function command_back at 0x7f81bf97e500>
RoutersploitInterpreter._show_info
: <function _show_info at 0x7f81bf97ef50>
RoutersploitInterpreter.command_check
: <function command_check at 0x7f81bf980668>
RoutersploitInterpreter.command_use
: <function command_use at 0x7f81bf97e578>
RoutersploitInterpreter.__doc__: None
RoutersploitInterpreter.complete_use
: <function complete_use at 0x7f81bf97e6e0>
RoutersploitInterpreter.history_file:RoutersploitInterpreter./root/.rsf_history
RoutersploitInterpreter._show_options
: <function _show_options at 0x7f81bf9800c8>
RoutersploitInterpreter._show_devices
: <function _show_devices at 0x7f81bf9801b8>
RoutersploitInterpreter.command_exec
: <function command_exec at 0x7f81bf980758>
RoutersploitInterpreter.command_help
: <function command_help at 0x7f81bf9806e0>
RoutersploitInterpreter.get_opts
: <function get_opts at 0x7f81bf97ee60>
RoutersploitInterpreter._show_all
: <function _show_all at 0x7f81bf9802a8>
RoutersploitInterpreter._show_scanners
: <function _show_scanners at 0x7f81bf980320>
RoutersploitInterpreter.complete_unsetg
: <function complete_unsetg at 0x7f81bf97ede8>
RoutersploitInterpreter.global_help:RoutersploitInterpreter.Global commands:   help                        Print this help menu   use <module>                Select a module for usage   exec <shell command> <args> Execute a command in a shell   search <search term>        Search for appropriate module   exit                        Exit RouterSploit
RoutersploitInterpreter.command_exploit
: <function command_exploit at 0x7f81bf97e7d0>
RoutersploitInterpreter.__init__
: <function __init__ at 0x7f81bf97e1b8>
RoutersploitInterpreter.available_modules_completion
: <function available_modules_completion at 0x7f81bf97e410>
RoutersploitInterpreter._show_exploits
: <function _show_exploits at 0x7f81bf980398>
RoutersploitInterpreter.module_metadata
: <property object at 0x7f81bf9d5db8>})
>>>


# The shell
shell(var)

Copyright (c) 1991-1995 Stichting Mathematisch Centrum
 Amsterdam.
All Rights Reserved.
import NameError: <typeimport exceptions.NameError>
import BytesWarning: <typeimport exceptions.BytesWarning>
import dict: <typeimport dict>
import input: <built-in function input>
import oct: <built-in function oct>
import bin: <built-in function bin>
import SystemExit: <typeimport exceptions.SystemExit>
import StandardError: <typeimport exceptions.StandardError>
import format: <built-in function format>
import repr: <built-in function repr>
import __cffi_backend_extern_py: {139870661244096: (<ctypeimport int(*)(char *
 int
 int
 void *)>
 <function _pem_password_cb at 0x7f362c04c398>
import \x00\x00\x00\x00\x00\x00\x00\x00
 None)}
import sorted: <built-in function sorted>
import False: False
import RuntimeWarning: <typeimport exceptions.RuntimeWarning>
import list: <typeimport list>
import iter: <built-in function iter>
import reload: <built-in function reload>
import Warning: <typeimport exceptions.Warning>
import __package__: None
import round: <built-in function round>
import dir: <built-in function dir>
import cmp: <built-in function cmp>
import set: <typeimport set>
import bytes: <typeimport str>
import reduce: <built-in function reduce>
import intern: <built-in function intern>
import issubclass: <built-in function issubclass>
import Ellipsis: Ellipsis
import EOFError: <typeimport exceptions.EOFError>
import locals: <built-in function locals>
import BufferError: <typeimport exceptions.BufferError>
import slice: <typeimport slice>
import FloatingPointError: <typeimport exceptions.FloatingPointError>
import sum: <built-in function sum>
import getattr: <built-in function getattr>
import abs: <built-in function abs>
import exit: Use exit() or Ctrl-D (i.e. EOF) to exit
import print: <built-in function print>
import True: True
import FutureWarning: <typeimport exceptions.FutureWarning>
import ImportWarning: <typeimport exceptions.ImportWarning>
import None: None
import hash: <built-in function hash>
import ReferenceError: <typeimport exceptions.ReferenceError>
import len: <built-in function len>
import credits:     Thanks to CWI
 CNRI
 BeOpen.com
 Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
import frozenset: <typeimport frozenset>
import __name__:import __builtin__
import ord: <built-in function ord>
import super: <typeimport super>
import _: None
import TypeError: <typeimport exceptions.TypeError>
import license: Type license() to see the full license text
import KeyboardInterrupt: <typeimport exceptions.KeyboardInterrupt>
import UserWarning: <typeimport exceptions.UserWarning>
import filter: <built-in function filter>
import range: <built-in function range>
import staticmethod: <typeimport staticmethod>
import SystemError: <typeimport exceptions.SystemError>
import BaseException: <typeimport exceptions.BaseException>
import pow: <built-in function pow>
import RuntimeError: <typeimport exceptions.RuntimeError>
import float: <typeimport float>
import MemoryError: <typeimport exceptions.MemoryError>
import StopIteration: <typeimport exceptions.StopIteration>
import globals: <built-in function globals>
import divmod: <built-in function divmod>
import enumerate: <typeimport enumerate>
import apply: <built-in function apply>
import LookupError: <typeimport exceptions.LookupError>
import open: <built-in function open>
import quit: Use quit() or Ctrl-D (i.e. EOF) to exit
import basestring: <typeimport basestring>
import UnicodeError: <typeimport exceptions.UnicodeError>
import zip: <built-in function zip>
import hex: <built-in function hex>
import long: <typeimport long>
import next: <built-in function next>
import ImportError: <typeimport exceptions.ImportError>
import chr: <built-in function chr>
import xrange: <typeimport xrange>
import type: <typeimport type>
import __doc__: "Built-in functions
 exceptions
 and other objects.\n\nNoteworthy: None is the `nil object; Ellipsis represents `... in slices."
import Exception: <typeimport exceptions.Exception>
import tuple: <typeimport tuple>
import UnicodeTranslateError: <typeimport exceptions.UnicodeTranslateError>
import reversed: <typeimport reversed>
import UnicodeEncodeError: <typeimport exceptions.UnicodeEncodeError>
import IOError: <typeimport exceptions.IOError>
import hasattr: <built-in function hasattr>
import delattr: <built-in function delattr>
import setattr: <built-in function setattr>
import raw_input: <built-in function raw_input>
import SyntaxWarning: <typeimport exceptions.SyntaxWarning>
import compile: <built-in function compile>
import ArithmeticError: <typeimport exceptions.ArithmeticError>
import str: <typeimport str>
import property: <typeimport property>
import GeneratorExit: <typeimport exceptions.GeneratorExit>
import int: <typeimport int>
import __import__: <built-in function __import__>
import KeyError: <typeimport exceptions.KeyError>
import coerce: <built-in function coerce>
import PendingDeprecationWarning: <typeimport exceptions.PendingDeprecationWarning>
import file: <typeimport file>
import EnvironmentError: <typeimport exceptions.EnvironmentError>
import unichr: <built-in function unichr>
import id: <built-in function id>
import OSError: <typeimport exceptions.OSError>
import DeprecationWarning: <typeimport exceptions.DeprecationWarning>
import min: <built-in function min>
import UnicodeWarning: <typeimport exceptions.UnicodeWarning>
import execfile: <built-in function execfile>
import any: <built-in function any>
import complex: <typeimport complex>
import bool: <typeimport bool>
import ValueError: <typeimport exceptions.ValueError>
import NotImplemented: NotImplemented
import map: <built-in function map>
import buffer: <typeimport buffer>
import max: <built-in function max>
import object: <typeimport object>
import TabError: <typeimport exceptions.TabError>
import callable: <built-in function callable>
import ZeroDivisionError: <typeimport exceptions.ZeroDivisionError>
import eval: <built-in function eval>
import __debug__: True
import IndentationError: <typeimport exceptions.IndentationError>
import AssertionError: <typeimport exceptions.AssertionError>
import classmethod: <typeimport classmethod>
import UnboundLocalError: <typeimport exceptions.UnboundLocalError>
import NotImplementedError: <typeimport exceptions.NotImplementedError>
import AttributeError: <typeimport exceptions.AttributeError>
import OverflowError: <typeimport exceptions.OverflowError>}
import __file__:import routersploit/shell.pyc
import sys: <moduleimport sys (built-in)>
import printer_queue: <Queue.Queue instance at 0x7f362bd88878>
import __name__:import routersploit.shell
import LockedIterator: <classimport routersploit.utils.LockedIterator>
import print_status: <function print_status at 0x7f362bd3b488>
import multi: <function multi at 0x7f362bd3b320>
import join: <function join at 0x7f362fd6f050>
import socket: <moduleimport socket fromimport /usr/lib/python2.7/socket.pyc>
import Communication: <classimport routersploit.shell.Communication>
import modules: <moduleimport routersploit.modules fromimport routersploit/modules/__init__.pyc>
import boolify: <function boolify at 0x7f362bd3bc08>
import index_modules: <function index_modules at 0x7f362bd1fb18>
import threading: <moduleimport threading fromimport /usr/lib/python2.7/threading.pyc>
import telnetlib: <moduleimport telnetlib fromimport /usr/lib/python2.7/telnetlib.pyc>
import print_info: <function print_info at 0x7f362bd3b578>
import time: <moduleimport time (built-in)>
import exceptions: <moduleimport routersploit.exceptions fromimport routersploit/exceptions.pyc>
import random_text: <function random_text at 0x7f362bd3bb18>}
>>>
Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

utils.modules
import NameError: <typeimport exceptions.NameError>
import BytesWarning: <typeimport exceptions.BytesWarning>
import dict: <typeimport dict>
import input: <built-in function input>
import oct: <built-in function oct>
import bin: <built-in function bin>
import SystemExit: <typeimport exceptions.SystemExit>
import StandardError: <typeimport exceptions.StandardError>
import format: <built-in function format>
import repr: <built-in function repr>
import __cffi_backend_extern_py: {140405567485120: (<ctypeimport int(*)(char *
 int
 int
 void *)>
 <function _pem_password_cb at 0x7fb2b6ea4398>
import \x00\x00\x00\x00\x00\x00\x00\x00
 None)}
import sorted: <built-in function sorted>
import False: False
import RuntimeWarning: <typeimport exceptions.RuntimeWarning>
import list: <typeimport list>
import iter: <built-in function iter>
import reload: <built-in function reload>
import Warning: <typeimport exceptions.Warning>
import __package__: None
import round: <built-in function round>
import dir: <built-in function dir>
import cmp: <built-in function cmp>
import set: <typeimport set>
import bytes: <typeimport str>
import reduce: <built-in function reduce>
import intern: <built-in function intern>
import issubclass: <built-in function issubclass>
import Ellipsis: Ellipsis
import EOFError: <typeimport exceptions.EOFError>
import locals: <built-in function locals>
import BufferError: <typeimport exceptions.BufferError>
import slice: <typeimport slice>
import FloatingPointError: <typeimport exceptions.FloatingPointError>
import sum: <built-in function sum>
import getattr: <built-in function getattr>
import abs: <built-in function abs>
import exit: Use exit() or Ctrl-D (i.e. EOF) to exit
import print: <built-in function print>
import True: True
import FutureWarning: <typeimport exceptions.FutureWarning>
import ImportWarning: <typeimport exceptions.ImportWarning>
import None: None
import hash: <built-in function hash>
import ReferenceError: <typeimport exceptions.ReferenceError>
import len: <built-in function len>
import credits:     Thanks to CWI
 CNRI
 BeOpen.com
 Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
import frozenset: <typeimport frozenset>
import __name__:import __builtin__
import ord: <built-in function ord>
import super: <typeimport super>
import _: None
import TypeError: <typeimport exceptions.TypeError>
import license: Type license() to see the full license text
import KeyboardInterrupt: <typeimport exceptions.KeyboardInterrupt>
import UserWarning: <typeimport exceptions.UserWarning>
import filter: <built-in function filter>
import range: <built-in function range>
import staticmethod: <typeimport staticmethod>
import SystemError: <typeimport exceptions.SystemError>
import BaseException: <typeimport exceptions.BaseException>
import pow: <built-in function pow>
import RuntimeError: <typeimport exceptions.RuntimeError>
import float: <typeimport float>
import MemoryError: <typeimport exceptions.MemoryError>
import StopIteration: <typeimport exceptions.StopIteration>
import globals: <built-in function globals>
import divmod: <built-in function divmod>
import enumerate: <typeimport enumerate>
import apply: <built-in function apply>
import LookupError: <typeimport exceptions.LookupError>
import open: <built-in function open>
import quit: Use quit() or Ctrl-D (i.e. EOF) to exit
import basestring: <typeimport basestring>
import UnicodeError: <typeimport exceptions.UnicodeError>
import zip: <built-in function zip>
import hex: <built-in function hex>
import long: <typeimport long>
import next: <built-in function next>
import ImportError: <typeimport exceptions.ImportError>
import chr: <built-in function chr>
import xrange: <typeimport xrange>
import type: <typeimport type>
import __doc__: "Built-in functions
 exceptions
 and other objects.\n\nNoteworthy: None is the `nil object; Ellipsis represents `... in slices."
import Exception: <typeimport exceptions.Exception>
import tuple: <typeimport tuple>
import UnicodeTranslateError: <typeimport exceptions.UnicodeTranslateError>
import reversed: <typeimport reversed>
import UnicodeEncodeError: <typeimport exceptions.UnicodeEncodeError>
import IOError: <typeimport exceptions.IOError>
import hasattr: <built-in function hasattr>
import delattr: <built-in function delattr>
import setattr: <built-in function setattr>
import raw_input: <built-in function raw_input>
import SyntaxWarning: <typeimport exceptions.SyntaxWarning>
import compile: <built-in function compile>
import ArithmeticError: <typeimport exceptions.ArithmeticError>
import str: <typeimport str>
import property: <typeimport property>
import GeneratorExit: <typeimport exceptions.GeneratorExit>
import int: <typeimport int>
import __import__: <built-in function __import__>
import KeyError: <typeimport exceptions.KeyError>
import coerce: <built-in function coerce>
import PendingDeprecationWarning: <typeimport exceptions.PendingDeprecationWarning>
import file: <typeimport file>
import EnvironmentError: <typeimport exceptions.EnvironmentError>
import unichr: <built-in function unichr>
import id: <built-in function id>
import OSError: <typeimport exceptions.OSError>
import DeprecationWarning: <typeimport exceptions.DeprecationWarning>
import min: <built-in function min>
import UnicodeWarning: <typeimport exceptions.UnicodeWarning>
import execfile: <built-in function execfile>
import any: <built-in function any>
import complex: <typeimport complex>
import bool: <typeimport bool>
import ValueError: <typeimport exceptions.ValueError>
import NotImplemented: NotImplemented
import map: <built-in function map>
import buffer: <typeimport buffer>
import max: <built-in function max>
import object: <typeimport object>
import TabError: <typeimport exceptions.TabError>
import callable: <built-in function callable>
import ZeroDivisionError: <typeimport exceptions.ZeroDivisionError>
import eval: <built-in function eval>
import __debug__: True
import IndentationError: <typeimport exceptions.IndentationError>
import AssertionError: <typeimport exceptions.AssertionError>
import classmethod: <typeimport classmethod>
import UnboundLocalError: <typeimport exceptions.UnboundLocalError>
import NotImplementedError: <typeimport exceptions.NotImplementedError>
import AttributeError: <typeimport exceptions.AttributeError>
import OverflowError: <typeimport exceptions.OverflowError>}
import __file__:import routersploit/utils/__init__.pyc
import create_exploit: <function create_exploit at 0x7fb2b6b93e60>
import sys: <moduleimport sys (built-in)>
import printer_queue: <Queue.Queue instance at 0x7fb2b6be0878>
import PrintResource: <classimport routersploit.utils.PrintResource>
import posix_shell: <function posix_shell at 0x7fb2b6b93cf8>
import __name__:import routersploit.utils
import LockedIterator: <classimport routersploit.utils.LockedIterator>
import strtobool: <function strtobool at 0x7fb2b8921410>
import EXPLOITS_DIR:import routersploit/modules/exploits
import print_function: _Feature((2
 6
 0
import alpha
 2)
 (3
 0
 0
import alpha
 0)
 65536)
import iter_modules: <function iter_modules at 0x7fb2b6b77f50>
import import_exploit: <function import_exploit at 0x7fb2b6b77ed8>
import multi: <function multi at 0x7fb2b6b93320>
import create_resource: <function create_resource at 0x7fb2b6b93ed8>
import socket: <moduleimport socket fromimport /usr/lib/python2.7/socket.pyc>
import SCANNERS_DIR:import routersploit/modules/scanners
import index_modules: <function index_modules at 0x7fb2b6b77b18>
import print_error: <function print_error at 0x7fb2b6b93410>
import humanize_path: <function humanize_path at 0x7fb2b6b930c8>
import print_lock: <thread.lock object at 0x7fb2b8031530>
import threading: <moduleimport threading fromimport /usr/lib/python2.7/threading.pyc>
import CREDS_DIR:import routersploit/modules/creds
import print_success: <function print_success at 0x7fb2b6b93500>
import print_info: <function print_info at 0x7fb2b6b93578>
import DummyFile: <classimport routersploit.utils.DummyFile>
import requests: <moduleimport requests fromimport /usr/lib/python2.7/dist-packages/requests/__init__.pyc>
import os: <moduleimport os fromimport /usr/lib/python2.7/os.pyc>
import random_text: <function random_text at 0x7fb2b6b93b18>}

###
#ssh_interactive shell


Copyright (c) 1991-1995 Stichting Mathematisch Centrum
 Amsterdam.
All Rights Reserved.
import NameError: <typeimport exceptions.NameError>
import BytesWarning: <typeimport exceptions.BytesWarning>
import dict: <typeimport dict>
import input: <built-in function input>
import oct: <built-in function oct>
import bin: <built-in function bin>
import SystemExit: <typeimport exceptions.SystemExit>
import StandardError: <typeimport exceptions.StandardError>
import format: <built-in function format>
import repr: <built-in function repr>
import __cffi_backend_extern_py: {140405567485120: (<ctypeimport int(*)(char *
 int
 int
 void *)>
 <function _pem_password_cb at 0x7fb2b6ea4398>
import \x00\x00\x00\x00\x00\x00\x00\x00
 None)}
import sorted: <built-in function sorted>
import False: False
import RuntimeWarning: <typeimport exceptions.RuntimeWarning>
import list: <typeimport list>
import iter: <built-in function iter>
import reload: <built-in function reload>
import Warning: <typeimport exceptions.Warning>
import __package__: None
import round: <built-in function round>
import dir: <built-in function dir>
import cmp: <built-in function cmp>
import set: <typeimport set>
import bytes: <typeimport str>
import reduce: <built-in function reduce>
import intern: <built-in function intern>
import issubclass: <built-in function issubclass>
import Ellipsis: Ellipsis
import EOFError: <typeimport exceptions.EOFError>
import locals: <built-in function locals>
import BufferError: <typeimport exceptions.BufferError>
import slice: <typeimport slice>
import FloatingPointError: <typeimport exceptions.FloatingPointError>
import sum: <built-in function sum>
import getattr: <built-in function getattr>
import abs: <built-in function abs>
import exit: Use exit() or Ctrl-D (i.e. EOF) to exit
import print: <built-in function print>
import True: True
import FutureWarning: <typeimport exceptions.FutureWarning>
import ImportWarning: <typeimport exceptions.ImportWarning>
import None: None
import hash: <built-in function hash>
import ReferenceError: <typeimport exceptions.ReferenceError>
import len: <built-in function len>
import credits:     Thanks to CWI
 CNRI
 BeOpen.com
 Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
import frozenset: <typeimport frozenset>
import __name__:import __builtin__
import ord: <built-in function ord>
import super: <typeimport super>
import _: None
import TypeError: <typeimport exceptions.TypeError>
import license: Type license() to see the full license text
import KeyboardInterrupt: <typeimport exceptions.KeyboardInterrupt>
import UserWarning: <typeimport exceptions.UserWarning>
import filter: <built-in function filter>
import range: <built-in function range>
import staticmethod: <typeimport staticmethod>
import SystemError: <typeimport exceptions.SystemError>
import BaseException: <typeimport exceptions.BaseException>
import pow: <built-in function pow>
import RuntimeError: <typeimport exceptions.RuntimeError>
import float: <typeimport float>
import MemoryError: <typeimport exceptions.MemoryError>
import StopIteration: <typeimport exceptions.StopIteration>
import globals: <built-in function globals>
import divmod: <built-in function divmod>
import enumerate: <typeimport enumerate>
import apply: <built-in function apply>
import LookupError: <typeimport exceptions.LookupError>
import open: <built-in function open>
import quit: Use quit() or Ctrl-D (i.e. EOF) to exit
import basestring: <typeimport basestring>
import UnicodeError: <typeimport exceptions.UnicodeError>
import zip: <built-in function zip>
import hex: <built-in function hex>
import long: <typeimport long>
import next: <built-in function next>
import ImportError: <typeimport exceptions.ImportError>
import chr: <built-in function chr>
import xrange: <typeimport xrange>
import type: <typeimport type>
import __doc__: "Built-in functions
 exceptions
 and other objects.\n\nNoteworthy: None is the `nil object; Ellipsis represents `... in slices."
import Exception: <typeimport exceptions.Exception>
import tuple: <typeimport tuple>
import UnicodeTranslateError: <typeimport exceptions.UnicodeTranslateError>
import reversed: <typeimport reversed>
import UnicodeEncodeError: <typeimport exceptions.UnicodeEncodeError>
import IOError: <typeimport exceptions.IOError>
import hasattr: <built-in function hasattr>
import delattr: <built-in function delattr>
import setattr: <built-in function setattr>
import raw_input: <built-in function raw_input>
import SyntaxWarning: <typeimport exceptions.SyntaxWarning>
import compile: <built-in function compile>
import ArithmeticError: <typeimport exceptions.ArithmeticError>
import str: <typeimport str>
import property: <typeimport property>
import GeneratorExit: <typeimport exceptions.GeneratorExit>
import int: <typeimport int>
import __import__: <built-in function __import__>
import KeyError: <typeimport exceptions.KeyError>
import coerce: <built-in function coerce>
import PendingDeprecationWarning: <typeimport exceptions.PendingDeprecationWarning>
import file: <typeimport file>
import EnvironmentError: <typeimport exceptions.EnvironmentError>
import unichr: <built-in function unichr>
import id: <built-in function id>
import OSError: <typeimport exceptions.OSError>
import DeprecationWarning: <typeimport exceptions.DeprecationWarning>
import min: <built-in function min>
import UnicodeWarning: <typeimport exceptions.UnicodeWarning>
import execfile: <built-in function execfile>
import any: <built-in function any>
import complex: <typeimport complex>
import bool: <typeimport bool>
import ValueError: <typeimport exceptions.ValueError>
import NotImplemented: NotImplemented
import map: <built-in function map>
import buffer: <typeimport buffer>
import max: <built-in function max>
import object: <typeimport object>
import TabError: <typeimport exceptions.TabError>
import callable: <built-in function callable>
import ZeroDivisionError: <typeimport exceptions.ZeroDivisionError>
import eval: <built-in function eval>
import __debug__: True
import IndentationError: <typeimport exceptions.IndentationError>
import AssertionError: <typeimport exceptions.AssertionError>
import classmethod: <typeimport classmethod>
import UnboundLocalError: <typeimport exceptions.UnboundLocalError>
import NotImplementedError: <typeimport exceptions.NotImplementedError>
import AttributeError: <typeimport exceptions.AttributeError>
import OverflowError: <typeimport exceptions.OverflowError>}
import __file__:import routersploit/utils/__init__.pyc
import create_exploit: <function create_exploit at 0x7fb2b6b93e60>
import sys: <moduleimport sys (built-in)>
import printer_queue: <Queue.Queue instance at 0x7fb2b6be0878>
import PrintResource: <classimport routersploit.utils.PrintResource>
import posix_shell: <function posix_shell at 0x7fb2b6b93cf8>
import __name__:import routersploit.utils
import LockedIterator: <classimport routersploit.utils.LockedIterator>
import strtobool: <function strtobool at 0x7fb2b8921410>
import EXPLOITS_DIR:import routersploit/modules/exploits
import print_function: _Feature((2
 6
 0
import alpha
 2)
 (3
 0
 0
import alpha
 0)
 65536)
import iter_modules: <function iter_modules at 0x7fb2b6b77f50>
import import_exploit: <function import_exploit at 0x7fb2b6b77ed8>
import multi: <function multi at 0x7fb2b6b93320>
import create_resource: <function create_resource at 0x7fb2b6b93ed8>
import socket: <moduleimport socket fromimport /usr/lib/python2.7/socket.pyc>
import SCANNERS_DIR:import routersploit/modules/scanners
import index_modules: <function index_modules at 0x7fb2b6b77b18>
import print_error: <function print_error at 0x7fb2b6b93410>
import humanize_path: <function humanize_path at 0x7fb2b6b930c8>
import print_lock: <thread.lock object at 0x7fb2b8031530>
import threading: <moduleimport threading fromimport /usr/lib/python2.7/threading.pyc>
import CREDS_DIR:import routersploit/modules/creds
import print_success: <function print_success at 0x7fb2b6b93500>
import print_info: <function print_info at 0x7fb2b6b93578>
import DummyFile: <classimport routersploit.utils.DummyFile>
import requests: <moduleimport requests fromimport /usr/lib/python2.7/dist-packages/requests/__init__.pyc>
import os: <moduleimport os fromimport /usr/lib/python2.7/os.pyc>
import random_text: <function random_text at 0x7fb2b6b93b18>}
>>>

# this is the primary "interaction engine" designed for external manipulation of the hacking toolkit called routersploit
# # this directly interfaces with the API to allow the user to run and pass certain commands to the routersploit shell in the background.
# # that routersploit shell
#  will be sent on its own task
#  working asynchronously
#  so that the attacker now remains unburdened and can focus on other things
