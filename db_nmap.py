#!/usr/bin/env python
# coding=UTF-8


import subprocess
import time
import operator
import os
import socket
import sys
from termcolor import colored
sys.path.append('/root/ArmsCommander')
import toolkits

default_target_list = "/tmp/default_target_list.txt"
MSF_init_str = """
service postgresql start
service metasploit start
msfdb init
msfdb start
"""
os.system(MSF_init_str)

def bash_command(cmd): # runs commands through the more featureful bash shell instead of regular
    #subprocess.Popen(['/bin/bash', '-c'. cmd])
    print cmd
    subprocess.call(cmd, shell=True, executable='/bin/bash')
    return

def MSF_cmd_exec(cmd):
    MSF_cmd = """tsocks msfconsole -x {0}""".format(str(cmd))

    bash_command(MSF_cmd)
    return MSF_cmd

def MSF_resource_script(cmd):
    return

def sh_command(cmd):
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, executable='/bin/bash')
    return
def installer(default_target_list):
    PIP_packages = """
    adns-python==1.2.1
    AdvancedHTTPServer==2.0.10
    alembic==0.9.3.dev0
    anyjson==0.3.3
    argcomplete==1.8.1
    argh==0.26.2
    attrs==17.2.0
    backdoor-factory==0.0.0
    backports-abc==0.5
    backports.shutil-get-terminal-size==1.0.0
    backports.ssl-match-hostname==3.5.0.1
    basemap==1.0.7
    BBQSQL==1.0
    BeautifulSoup==3.2.1
    beautifulsoup4==4.6.0
    binwalk===2.1.2-8330f7e
    blessings==1.6
    BlindElephant==1.0
    blinker==1.3
    boltons==17.1.0
    brotlipy==0.6.0
    capstone==3.0.4
    certifi==2017.7.27.1
    chardet==3.0.4
    Cheetah==2.4.4
    clamd==1.0.1
    click==6.7
    cluster==1.3.3
    colorama==0.3.7
    ConfigArgParse==0.11.0
    configobj==5.0.6
    configparser==3.5.0
    constantly==15.1.0
    construct==2.8.16
    couchdbkit==0.6.5
    cryptography==1.7.1
    cssutils==1.0.2
    cycler==0.10.0
    d2to1==0.2.12
    dap==2.2.6.7
    darts.util.lru==0.5
    dbus-python==1.2.4
    decorator==4.1.2
    defusedxml==0.5.0
    dicttoxml==1.7.4
    dissy==9
    distorm3==3.3.4
    Django==1.11.7
    dnspython==1.15.0
    docutils==0.14
    easygui==0.96
    EditorConfig==0.12.1
    Elixir==0.7.1
    enum34==1.1.6
    esmre==0.3.1
    feedparser==5.1.3
    Flask==0.12.2
    FormEncode==1.3.0
    functools32==3.2.3.post2
    fuse-python==0.2.1
    future==0.15.2
    futures==3.1.1
    GDAL==2.1.2
    GeoIP==1.3.2
    geoip2==2.6.0
    geojson==2.3.0
    gevent==1.2.2
    gitdb2==2.0.2
    GitPython==2.1.7
    greenlet==0.4.12
    guess-language-spirit==0.5.2
    h2==2.5.2
    halberd==0.2.4
    hpack==3.0.0
    html2text==2016.9.19
    html5lib==0.999999999
    http-parser==0.8.3
    httplib2==0.9.2
    httpretty==0.8.14
    hyperframe==4.0.1
    icalendar==3.8
    idna==2.5
    impacket==0.9.15
    incremental==16.10.1
    ipaddr==2.1.11
    ipaddress==1.0.17
    IPy==0.83
    ipython==5.5.0
    ipython-genutils==0.2.0
    itsdangerous==0.24
    jdcal==1.0
    Jinja2==2.9.6
    jsbeautifier==1.6.4
    jsonpickle==0.9.5
    jsonrpclib==0.1.3
    keepnote==0.7.8
    keyring==10.4.0
    keyrings.alt==2.2
    killerbee==1.0
    lxml==4.1.0
    M2Crypto==0.27.0
    Mako==1.0.7
    Markdown==2.6.9
    MarkupSafe==1.0
    matplotlib==2.0.0
    maxminddb==1.3.0
    mechanize==0.2.5
    mercurial==4.3.1
    metaconfig==0.1.4a1
    mitmproxy==0.18.2
    mockito==0.5.2
    msgpack-python==0.4.8
    mysqlclient==1.3.10
    nassl==0.12
    ndg-httpsclient==0.4.3
    netaddr==0.7.19
    NfSpy==1.0
    nltk==3.2.5
    numpy==1.13.3
    olefile==0.44
    openpyxl==2.3.0
    PAM==0.4.2
    paramiko==2.0.0
    passlib==1.7.1
    Paste==2.0.3
    PasteDeploy==1.5.2
    PasteScript==1.7.5
    pathlib2==2.1.0
    pathtools==0.1.2
    pbkdf2==1.3
    pcapy==0.10.8
    pdfminer==20140328
    pefile==2017.11.5
    pexpect==4.2.1
    phply==1.2.1
    pickleshare==0.7.4
    Pillow==4.3.0
    ply==3.9
    prettytable==0.7.2
    prompt-toolkit==1.0.14
    psutil==5.4.1
    psycopg2==2.7.3
    py==1.4.34
    pyasn1==0.1.9
    pyasn1-modules==0.0.7
    pybloomfiltermmap==0.3.15
    PyBOMBS==2.3.2
    pycairo==1.15.4
    pycrypto==2.6.1
    pycryptodomex==3.4.7
    pycryptopp==0.7.1
    pycurl==7.43.0
    pydns==2.3.6
    pyenchant==1.6.11
    PyGithub==1.23.0
    Pygments==2.2.0
    pygobject==3.26.1
    pyinotify==0.9.6
    PyInstaller==3.1.1+4529aa2
    pylibemu==0.3.3
    pyliblzma==0.5.3
    pymetasploit==1.1
    pymongo==3.5.1
    pymssql==2.1.3
    pyOpenSSL==16.2.0
    pyotp==2.2.6
    pyparsing==2.1.10
    pyPdf==1.13
    PyPDF2==1.26.0
    pyperclip==1.5.32
    PyRIC==0.1.6.3
    pyrit==0.5.1
    pyscard==1.9.6
    pyserial==3.4
    pysmi==0.1.3
    pysnmp==4.3.2
    pysnmp-apps==0.3.2
    pysnmp-mibs==0.1.3
    PySocks==1.6.5
    pyspatialite==3.0.1
    pysqlite==2.7.0
    pytest==3.2.1
    python-apt==1.4.0b3+b1
    python-dateutil==2.6.1
    python-debian==0.1.31
    python-debianbts==2.7.1
    python-editor==0.4
    python-Levenshtein==0.12.0
    python-ntlm==1.1.0
    python-openid==2.2.5
    python-pam==1.8.2
    pytz==2017.2
    pyusb==1.0.0b2
    PyX==0.12.1
    pyxdg==0.25
    PyYAML==3.12
    qrcode==5.3
    reportbug==6.6.6
    requests==2.18.1
    restkit==4.2.2
    rfidiot==1.0
    roguehostapd==1.1.6
    roman==2.0.0
    ruamel.ordereddict==0.4.13
    ruamel.yaml==0.15.34
    scapy==2.3.3
    scgi==1.13
    SecretStorage==2.3.1
    service-identity==16.0.0
    Shapely==1.6.2
    simplegeneric==0.8.1
    simplejson==3.12.0
    singledispatch==3.4.0.3
    six==1.11.0
    slowaes==0.1a1
    smmap2==2.0.3
    smoke-zephyr==1.0.2
    SOAPpy==0.12.22
    socketpool==0.5.3
    SQLAlchemy==1.1.11
    sqlparse==0.2.2
    stopit==1.1.0
    subprocess32==3.2.7
    tblib==1.3.2
    tcpwatch==1.3.1
    Tempita==0.5.2
    termcolor==1.1.0
    tornado==4.5.2
    traitlets==4.3.2
    Twisted==16.6.0
    typing==3.6.2
    tzlocal==1.4
    unicodecsv==0.14.1
    unpyclib==0.8.1
    urllib3==1.21.1
    urwid==1.3.1
    uTidylib==0.3
    vinetto==0.7b0
    volatility==2.6
    vulndb==0.0.19
    wafw00f==0.9.3
    wapiti==2.3.0
    watchdog==0.8.3
    wcwidth==0.1.7
    webencodings==0.5
    webunit==1.3.10
    Werkzeug==0.12.2.dev0
    wfuzz==2.2.3
    Whoosh==2.7.4
    wicd==1.7.4
    wifiphisher==1.3
    wstools==0.4.3
    wxPython==3.0.2.0
    wxPython-common==3.0.2.0
    xdot==0.5
    XlsxWriter==0.9.6
    xmlbuilder==1.0
    yara-python==3.7.0
    zenmap==7.60
    zim==0.67
    zope.interface==4.3.2"""
    git_repo = """""" # the official location of this package
    APT_packages = "tor db_metasploit-framework nmap zenmap"

    # generates a list of required python modules physically as a temporary file
    requirements_file = "/tmp/pip_requirements_file.txt"
    w = open(requirements_file,'w')
    w.write(PIP_packages)
    w.close()
    PIP_REQUIREMENTS_FILE_install_from_cmd = "pip install -r {0}".format(str(requirements_file))


    GIT_CLONE_cmd = "cd /tmp;git clone{0}".format(str(git_repo))

    # installs from a list of required APT packages commonly found on linux
    APT_install_cmd = "sudo apt-get update && apt-get install -y {0}".format(str(APT_packages))
    os.system(GIT_CLONE_cmd)
    os.system(APT_install_cmd)
    os.system(PIP_REQUIREMENTS_FILE_install_from_cmd)

    GIT_local_folder_name = ""

    COPY_CHANGE_PERM_cmd = """
    cd /tmp
    chmod 777 {0}
    chmod 777 {0}/*
    mkdir /root/ArmsCommander/
    mkdir /root/ArmsCommander/recon/
    cp -r {0} /root/ArmsCommander/recon/initial_recon/
    # echo '' > default_target_list.txt
    """.format(str(GIT_local_folder_name))
    return

def target_list_edit(default_target_list):
    NANO_target_list = "nano {0}".format(str(default_target_list))
    os.system(NANO_target_list)
    return

# parses both the fail2ban.log and alert.logs and then creates a wordlist and adds it to the default target list
def parse_fail2ban_snort_logs(default_target_list):
    debug_str = "DEBUG: The default target list is {0}".format(str(default_target_list))
    print debug_str
    # clears out the default target list
    # WIPE_DEFAULT_target_list_cmd = "echo '' > {0}".format(str(default_target_list))
    # os.system(WIPE_DEFAULT_target_list_cmd)
    # output = ''
# bug solution. Python will not allow me to pass SHELL PIPE ARGUMENTS but I can still run the variables as arugments, and then store the output as a variable, and then write it to a document.

    # starts off by parsing banned IPs in fail2ban logs
# https://stackoverflow.com/questions/20291543/cant-execute-shell-script-from-python-subprocess-permission-denied
# this link basically states that python is inadequate for nrunning shell commands
# next solution is a generate-a-script code which woulod be better because we can take advantage of specifying the command until bash for the better features.
    INTERNAL_ip_addr = "*.*.*.*"
    default_target_list = "/tmp/default_target_list.txt"

    # generate exclude file generally assuming that everything in your /etc/hosts directory is something you want to exclude from the pentest
    default_exclude_list = "/tmp/exclude_file.txt"
    bash_command("""cat /etc/hosts | awk '{{print $1}}' > {0}""".format(str(default_exclude_list)))
    script_1_name = "./bash_parse_fail2ban.sh"
    script_2_name = "./bash_parse_snort_logs.sh"
    # bash_script = ''
    # CMD_execute_bash = "/bin/bash {0}".format(str(bash_script))
    #
    # bash_script = script_1_name
    # os.system(CMD_execute_bash)
    # initial_scan(default_target_list)

    bash_command("""cd /var/log;egrep -irh "Ban" fail2ban* --color | awk -F "NOTICE" '{ print $2 }' | uniq -c > banned-ips.txt && cat banned-ips.txt | awk '{ print $4 }' | strings > /tmp/default_target_list.txt""")
    bash_command("""cd /var/log/snort;egrep -irh " -> *.*.*.*" * --color | sort -k 2 | awk -F "->" '{ print $1 $2 }'| awk -F " " '{ print $2 "|" $3 }' | awk -F ":" '{ print $1 }' >> /tmp/default_target_list.txt""")
    bash_command("""cat /tmp/default_target_list.txt""")
    print toolkits.red("DEBUG: Checking if the default target list is enumerated")

    time.sleep(3)
    initial_scan(default_target_list)

    return default_target_list
def initial_scan(target_list):
    resource_file_default = '/tmp/resource_file_default.rc'
    print toolkits.cyan("Your selected target list file is {0}".format(str(target_list)))
    workspace = str(raw_input("Enter your Metasploit WORKSPACE: "))

    if workspace == "" or None:
        workspace = "default"
    else:
        pass
    # restarts tor

    TOR_restart_cmd = "service tor restart"
    os.system(TOR_restart_cmd)
    save_file_location = "/root/Documents" # default nmap xml saved files location

    # asks user for a list of targets he wants to scan as a simple text file with one IP address or hostname per line

    # these are all of the enumeration scripts
    enum_scripts = """ajp-headers.nse,http-headers.nse,http-security-headers.nse,http-server-header.nse,cics-enum.nse,cics-user-enum.nse,citrix-enum-apps.nse,citrix-enum-apps-xml.nse,citrix-enum-servers.nse,citrix-enum-servers-xml.nse,dns-nsec3-enum.nse,dns-nsec-enum.nse,dns-srv-enum.nse,domino-enum-users.nse,eppc-enum-processes.nse,http-domino-enum-passwords.nse,http-drupal-enum.nse,http-drupal-enum-users.nse,http-enum.nse,http-gitweb-projects-enum.nse,http-svn-enum.nse,http-userdir-enum.nse,http-wordpress-enum.nse,krb5-enum-users.nse,msrpc-enum.nse,mysql-enum.nse,ncp-enum-users.nse,nrpe-enum.nse,omp2-enum-targets.nse,oracle-enum-users.nse,rdp-enum-encryption.nse,sip-enum-users.nse,smb-enum-domains.nse,smb-enum-groups.nse,smb-enum-processes.nse,smb-enum-sessions.nse,smb-enum-shares.nse,smb-enum-users.nse,smb-mbenum.nse,smtp-enum-users.nse,ssh2-enum-algos.nse,ssl-enum-ciphers.nse,tftp-enum.nse,tso-enum.nse,vtam-enum.nse"""

    # generates random time str to make the .xml file unique
    timestr = timestr = time.strftime("%Y%m%d-%H%M%S")

    # runs scans in this order, FIN, XMAS, and COMPREHENSIVE


# the problem is that


# we cannot multiplex additional commands into msf console with the -x option
# the resource file option is slow as fuck. 
    FIN_scan_cmd = """db_nmap -v -O -sF -Pn -T4 -O -F -oX {2}/FIN_initial_scan_{3}.xml --script={0} nmap --min-hostgroup 50 --max-hostgroup 1024 --min-parallelism 10 --max-parallelism 20 --host-timeout 30s -iL {1}""".format(str(enum_scripts),str(target_list),str(save_file_location),str(timestr))

    #timestr = timestr = time.strftime("%Y%m%d-%H%M%S")

    XMAS_scan_cmd = """db_nmap -v -O -sX -Pn -T4 -O -F -oX {2}/XMAS_initial_scan_{3}.xml --script={0} nmap --min-hostgroup 50 --max-hostgroup 1024 --min-parallelism 10 --max-parallelism 20 --host-timeout 30s -iL {1}""".format(str(enum_scripts),str(target_list),str(save_file_location),str(timestr))

    #timestr = timestr = time.strftime("%Y%m%d-%H%M%S")

    COMPRE_scan_cmd = """db_nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 -oX {2}/COMPRE_initial_scan_{3}.xml --script={0} nmap --min-hostgroup 50 --max-hostgroup 1024 --min-parallelism 10 --max-parallelism 20 --host-timeout 30s -iL {1}""".format(str(enum_scripts),str(target_list),str(save_file_location),str(timestr))

    # runs all of these commands immediately after metasploit starts up.
    MSF_cmd = "workspace -a {0};setg WORKSPACE {0};{2};resource {1}".format(
    str(workspace),
    str(resource_file_default),
    str(FIN_scan_cmd)
    )

    print toolkits.yellow("""
        DEBUG: db_nmap lines
        {0}

    """).format(str(MSF_cmd))

    time.sleep(3)
    db_nmap_resource_file = """
    use auxiliary/server/socks4a
    run -j
    {0}
    {1}
    {2}
    """.format(
        str(FIN_scan_cmd),
        str(XMAS_scan_cmd),
        str(COMPRE_scan_cmd)
    )
    print toolkits.yellow("""
    DEBUG: Resource file content
    {0}
    """).format(
        str(db_nmap_resource_file)
    )
    w = open(resource_file_default,'w')
    w.write(db_nmap_resource_file)
    w.close()
    print toolkits.yellow("""
    DEBUG: Location of resource files

    {0}
    """).format(str(resource_file_default))

    debug_str = """ls -la {0}""".format(str(resource_file_default))
    bash_command(debug_str)

    host_cidr_range = ''
    darkoperator_resource_file = """
    workspace {0}
    load pentest
    network_discovery -d -v -r {1}
    """.format(
        str(workspace),
        str(host_cidr_range)
    )



    MSF_cmd_exec(MSF_cmd)

    return MSF_cmd, resource_file_default
def main(default_target_list):

    target_list = str(raw_input("Enter a FULL PATH to a wordlist of HOSTS/TARGETS or NOTHING to use whats in the DEFAULT target list: "))

    if target_list == "" or None:
        parse_fail2ban_snort_logs(default_target_list)
    else:
        initial_scan(target_list)
    return
main(default_target_list)
