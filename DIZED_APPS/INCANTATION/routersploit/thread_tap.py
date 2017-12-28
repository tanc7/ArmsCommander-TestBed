import os, sys, operator, socket,subprocess
# import direct_injection_exec
# from direct_injection_exec import *
import printer
from printer import *

def write_temp_py_file(write_str):

    # generates a file named printer thread tap in the same TL directory of RSF as the injector
    rsf_PATH_local = '/usr/local/bin'
    py_filename = "{}/thread_tap.py".format(str(rsf_PATH_local))

    # blank_file = "echo '' > %s" % str(py_filename)
    # os.system(blank_file)
    w = open(py_filename,'w')
    w.write(write_str)
    w.close()

    # orders bash to chmod and execute the temporary file
    run_cmd = """chmod 777 {0}
    python {0}""".format(
        str(py_filename)
    )

    bash_command(run_cmd)
    return
def bash_command(cmd):
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash')
    # executes the commands and then returns the process back to us as a separate thread.
    return p

# every time the main injector runs, it will open a instance of this.
# it'll be a def function
#
# # got this errors
#
# ile "/usr/lib/python2.7/dist-packages/chardet/escprober.py", line 31, in <module>
#     from .escsm import (HZ_SM_MODEL, ISO2022CN_SM_MODEL, ISO2022JP_SM_MODEL,
#   File "/usr/lib/python2.7/dist-packages/chardet/escsm.py", line 28, in <module>
#     from .escsm import (HZ_SM_MODEL, ISO2022CN_SM_MODEL, ISO2022JP_SM_MODEL,
#   File "/usr/lib/python2.7/dist-packages/chardet/escsm.py", line 28, in <module>
#     from .escsm import (HZ_SM_MODEL, ISO2022CN_SM_MODEL, ISO2022JP_SM_MODEL,
#   File "/usr/lib/python2.7/dist-packages/chardet/escsm.py", line 28, in <module>
#     from .escsm import (HZ_SM_MODEL, ISO2022CN_SM_MODEL, ISO2022JP_SM_MODEL,
#   File "/usr/lib/python2.7/dist-packages/chardet/escsm.py", line 28, in <module>
#     from .escsm import (HZ_SM_MODEL, ISO2022CN_SM_MODEL, ISO2022JP_SM_MODEL,
#   File "/usr/lib/python2.7/dist-packages/chardet/escsm.py", line 28, in <module>
#     from .enums import MachineState
#     from .enums import MachineState
# KeyboardInterrupt
# KeyboardInterrupt
#     from .enums import MachineState
# KeyboardInterrupt
#     from .enums import MachineState
# KeyboardInterrupt
#     from .enums import MachineState
# that means it only RAN AFTER I managed to CANCEL The main module.

# EIther we just go integrate this into the main injector, or we create a master process. to run both.
def p_generate():

    write_str = """
from __future__ import print_function
from __future__ import absolute_import


########### this may not be needed, but just to be sure.

import os
import threading
import time
import rsf
import routersploit

from itertools import chain
from weakref import WeakKeyDictionary

from routersploit.utils import print_status, NonStringIterable




######## required decoder

import threading
from weakref import WeakKeyDictionary
try:
    import queue
except ImportError:
    import Queue as queue


printer_queue = queue.Queue()
thread_output_stream = WeakKeyDictionary()


class PrinterThread(threading.Thread):
    def __init__(self):
        super(PrinterThread, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            content, sep, end, file_, thread = printer_queue.get()
            print(*content, sep=sep, end=end, file=file_)
            printer_queue.task_done()

PrinterThread().run()
    """

    p = threading.Thread(target=write_temp_py_file(write_str))

    ### p = the output from threading
    return p

p_generate()


### ??? Bug?
### Executing this file before the injector caused the injector to start up. But still same output


# <routersploit.exploits.Option object at 0x7f71a1f6d350>
#
#
# 8
# 0
#   File "/usr/local/bin/direct_injection_exec.py", line 87
#     routersploit.exploits.Option(<routersploit.exploits.Option object at 0x7f71a1f6d350>,'')
#                                  ^
# SyntaxError: invalid syntax
# 0
#
#
#
# a
#
#
# <routersploit.exploits.Option object at 0x7f71a1f6d350>
#
#
# 8
#   File "/usr/local/bin/direct_injection_exec.py", line 87
#     routersploit.exploits.Option(<routersploit.exploits.Option object at 0x7f71a1f6d350>,'')
#                                  ^
# SyntaxError: invalid syntax
# 0
# 0
#
#
#
# a
#
#
# <routersploit.exploits.Option object at 0x7f71a1f6d350>
#
#
# 8
#




# this is intended to be run as a subprocess
    # withe threading
# import threading
# from common import IP_LIST, do_ping
#
# def run_do_ping(addr):
#    p = do_ping(addr)
#    p.wait()
#
# ###
#
# # start all threads
# z = []
# for i in range(0, len(IP_LIST)):
#    t = threading.Thread(target=run_do_ping, args=(IP_LIST[i],))
#    t.start()
#    z.append(t)
#
# # wait for all threads to finish
# for t in z:
#    t.join()

    # No threading
    # from subprocess import Popen
    #
    # commands = [
    #     'date; ls -l; sleep 1; date',
    #     'date; sleep 5; date',
    #     'date; df -h; sleep 3; date',
    #     'date; hostname; sleep 2; date',
    #     'date; uname -a; date',
    # ]
    # # run in parallel
    # processes = [Popen(cmd, shell=True) for cmd in commands]
    # # do other things here..
    # # wait for completion
    # for p in processes: p.wait()
