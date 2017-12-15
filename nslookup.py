import os
import socket
import sys
import operator
import socket
import subprocess
import re
import optparse
from sys import argv

# input_file = "/root/Documents/shell_script_output.log"

def nslookup(input_file):

    output_log = "nslookup_output.log"
    script_dir = "/var/log"
    default_dns = "8.8.8.8"

    r = open(input_file,'a+')
    with open(input_file) as r:
        lines = r.read().splitlines()
        print lines
        try:
            for line in lines:
                target_host = str(line)
                cmd_str = "nslookup {0} {1} >> {2}/{3};cat {2}/{3}".format(str(target_host), str(default_dns), str(script_dir), str(output_log))
                os.system(cmd_str)
                subprocess.call(cmd_str, shell=True)
        except EOFError:
            print "Done, exiting!"
            exit(0)

def main():
    parser = optparse.OptionParser('usage % prog -r <list_of_targets>')
    parser.add_option('-r', dest='input_file', type='string', help='full absolute path to list of IPs to resolve')
    (options, args) = parser.parse_args()
    if options.input_file == None:
        print parser.usage
        exit(0)
    else:
        input_file = options.input_file
        nslookup(input_file)
    return
main()
#
