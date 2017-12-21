from routersploit import (
    exploits,
    mute,
    validators,
    print_error,
    print_success,
    print_status,
    print_info,
    utils,
    threads,

)

import subprocess
import threading

def bash_command(cmd):
    result = subprocess.Popen(cmd,shell=True,executable='/bin/bash')

    return
def autograb_ip_address():
    gateway_list = []
    cmd = """route -n | egrep -v "0.0.0.0|Gateway|routing" | sort | uniq | awk '{{print $2}}'"""
    results = bash_command(cmd)
    for gw in results:
        gateway_list.append(gw)
    return gateway_list
class Exploit(exploits.Exploit):
    """
    Scanner implementation for all vulnerabilities.
    """
    __info__ = {
        'name': 'AutoPwn',
        'description': 'Scanner module for all vulnerabilities.',
        'authors': [
            'Marcin Bury <marcin.bury[at]reverse-shell.com>',  # routersploit module
        ],
        'references': (
            '',
        ),
        'devices': (
            'Multi',
        ),
    }
    modules = ['routers', 'cameras', 'misc']

    # target = exploits.Option('', 'Target IP address e.g. 192.168.1.1')  # target address
    # port = exploits.Option(80, 'Target port')  # default port
    # threads = exploits.Option(8, "Number of threads")

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
    gateway_list = autograb_ip_address()
    for item in gateway_list:
        target = exploits.Option(str(item), 'Target IP address e.g. 192.168.1.1')  # target address
        for item in port_list:
            port = exploits.Option(int(item), 'Target port')  # default port
            threads = exploits.Option(8, "Number of threads")



    def __init__(self):
        self.vulnerabilities = []
        self.not_verified = []
        self._exploits_directories = [path.join(utils.EXPLOITS_DIR, module) for module in self.modules]

    def run(self):
        self.vulnerabilities = []
        self.not_verified = []

        with threads.ThreadPoolExecutor(self.threads) as executor:
            for directory in self._exploits_directories:call
                for exploit in utils.iter_modules(directory):
                    executor.submit(self.target_function, exploit)

        print_info()
        if self.not_verified:
            print_status("Could not verify exploitability:")
            for v in self.not_verified:
                print_info(" - {}".format(v))

        print_info()
        if self.vulnerabilities:
            print_success("Device is vulnerable:")
            for v in self.vulnerabilities:
                print_info(" - {}".format(v))
            print_info()
        else:
            print_error("Could not confirm any vulnerablity\n")

    def check(self):
        raise NotImplementedError("Check method is not available")

    def target_function(self, exploit):
        exploit = exploit()
        exploit.target = self.target
        exploit.port = self.port

        response = exploit.check()

        if response is True:
            print_success("{} is vulnerable".format(exploit))
            self.vulnerabilities.append(exploit)
        elif response is False:
            print_error("{} is not vulnerable".format(exploit))
        else:
            print_status("{} could not be verified".format(exploit))
            self.not_verified.append(exploit)
