import os, sys, operator, socket,subprocess
# import direct_injection_exec
# from direct_injection_exec import *
import printer
from printer import *

def check_and_inject(inject_logger_printer_str):
# sed -i -e 's/few/asd/g' hello.txt
# replaces "few" with "asd"
    ### check the printer file###
    target_str = "from __future__ import absolute_import"
    replacement_str = str(inject_logger_printer_str)
    printer_file = "/usr/local/bin/routersploit/printer.py"

    sed_cmd = "sed -i -e 's/{0}/{1}/g' {2}".format(
        str(target_str),
        str(replacement_str),
        str(printer_file)
    )
    r = open("/usr/local/bin/routersploit/printer.py".'a+')
    read_file = r.readlines()

    if 'logger' or 'log' not in read_file:
        #inject the string at a point with sed.
        bash_command(sed_cmd)
        r.close()
    else:
        # just run the printer
        r.close()
        pass
    r.close() # make sure file is closed!
    # orders bash to chmod and execute the temporary file
    run_cmd = """python /usr/local/bin/routersploit/printer.py &"""
    bash_command(run_cmd)
    return
def bash_command(cmd):
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash')
    # executes the commands and then returns the process back to us as a separate thread.
    return p



inject_logger_printer_str = """
from __future__ import absolute_import
### Create the logger
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


check_and_inject(inject_logger_printer_str)
