#!/usr/bin/env/python
import os
import sys
import subprocess
import socket
import subprocess
import threading

def bash_command(cmd):
    result = subprocess.call(cmd,shell=True,executable='/bin/bash')
    print result
    return result

cmd = str(raw_input("Enter a command for the standard /bin/bash or sh: "))
bash_command(cmd)
