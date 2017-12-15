"""
if not os.path.exists(self.history_file):
    open(self.history_file, 'a+').close()

readline.read_history_file(self.history_file)
readline.set_history_length(self.history_length)
atexit.register(readline.write_history_file, self.history_file)

readline.parse_and_bind('set enable-keypad on')

readline.set_completer(self.complete)
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")

'description': 'Exploits ZTE F460 and F660 backdoor vulnerability that allows executing commands on operating system level.',
routersploit/modules/exploits/routers/zte/f460_f660_backdoor.py:55:            print_info(self.execute(cmd))
routersploit/modules/exploits/routers/zte/f460_f660_backdoor.py:57:    def execute(self, cmd):
routersploit/modules/exploits/routers/zte/f460_f660_backdoor.py:85:        response = self.execute(cmd)
routersploit/modules/exploits/cameras/multi/P2P_wificam_rce.py:22:        'name': 'P2P wificam remote code execution',
routersploit/modules/exploits/cameras/multi/P2P_wificam_rce.py:25:        unauthenticated remote code execution.""",
routersploit/modules/exploits/cameras/multi/P2P_wificam_rce.py:1303:    def execute(self, cmd):
routersploit/modules/exploits/misc/asus/b1m_projector_rce.py:15:    Exploit implementation for Asus B1M Projector Remote Code Execution vulnerability.
routersploit/modules/exploits/misc/asus/b1m_projector_rce.py:16:    If the target is vulnerable, command loop is invoked that allows executing commands with root privileges.
routersploit/modules/exploits/misc/asus/b1m_projector_rce.py:20:        'description': 'Module exploits Asus B1M Projector Remote Code Execution vulnerability which '
routersploit/modules/exploits/misc/asus/b1m_projector_rce.py:21:                       'allows executing command on operating system level with root privileges.',
routersploit/modules/exploits/misc/asus/b1m_projector_rce.py:45:    def execute(self, cmd):
routersploit/modules/exploits/misc/asus/b1m_projector_rce.py:58:        response_text = self.execute(cmd)
routersploit/modules/exploits/misc/wepresent/wipg1000_rce.py:16:    If the target is vulnerable, it is possible to execute commands on operating system level.
routersploit/modules/exploits/misc/wepresent/wipg1000_rce.py:21:                       'executing commands on operating system level.',
routersploit/modules/exploits/misc/wepresent/wipg1000_rce.py:48:    def execute(self, cmd):
routersploit/modules/payloads/mipsbe/bind_tcp.py:82:            # execve("//bin/sh", ["//bin/sh"], [/* 0 vars */]) = 0
routersploit/modules/payloads/mipsbe/bind_tcp.py:95:            "\x24\x02\x0f\xab" +        # li v0,4011 ( __NR_execve )
routersploit/modules/payloads/mipsle/bind_tcp.py:87:            "\xab\x0f\x02\x24" +  # li v0,4011 ( __NR_execve )
routersploit/modules/scanners/autopwn.py:142:        with threads.ThreadPoolExecutor(self.threads) as executor:
routersploit/modules/scanners/autopwn.py:145:                    executor.submit(self.target_function, exploit)
Binary file routersploit/modules/scanners/autopwn.pyc matches
routersploit/modules/creds/http_basic_bruteforce.py:17:from routersploit.exceptions import StopThreadPoolExecutor
routersploit/modules/creds/http_basic_bruteforce.py:78:        with threads.ThreadPoolExecutor(self.threads) as executor:
routersploit/modules/creds/http_basic_bruteforce.py:80:                executor.submit(self.target_function, url, record)
routersploit/modules/creds/http_basic_bruteforce.py:101:                raise StopThreadPoolExecutor
routersploit/modules/creds/http_digest_default.py:15:from routersploit.exceptions import StopThreadPoolExecutor
routersploit/modules/creds/http_digest_default.py:16:from routersploit.threads import ThreadPoolExecutor
routersploit/modules/creds/http_digest_default.py:72:        with ThreadPoolExecutor(self.threads) as executor:
routersploit/modules/creds/http_digest_default.py:75:                executor.submit(self.target_function, url, username, password)
routersploit/modules/creds/http_digest_default.py:98:                raise StopThreadPoolExecutor
routersploit/modules/creds/http_digest_bruteforce.py:17:from routersploit.exceptions import StopThreadPoolExecutor
routersploit/modules/creds/http_digest_bruteforce.py:80:        with threads.ThreadPoolExecutor(self.threads) as executor:
routersploit/modules/creds/http_digest_bruteforce.py:82:                executor.submit(self.target_function, url, record)
routersploit/modules/creds/http_digest_bruteforce.py:103:                raise StopThreadPoolExecutor
routersploit/modules/creds/http_basic_default.py:15:from routersploit.exceptions import StopThreadPoolExecutor
routersploit/modules/creds/http_basic_default.py:16:from routersploit.threads import ThreadPoolExecutor
routersploit/modules/creds/http_basic_default.py:70:        with ThreadPoolExecutor(self.threads) as executor:
routersploit/modules/creds/http_basic_default.py:73:                executor.submit(self.target_function, url, username, password)
routersploit/modules/creds/http_basic_default.py:96:                raise StopThreadPoolExecutor
routersploit/threads.py:12:from .exceptions import StopThreadPoolExecutor
routersploit/threads.py:34:            except StopThreadPoolExecutor:
routersploit/threads.py:42:class ThreadPoolExecutor(object):
Binary file routersploit/exceptions.pyc matches
Binary file routersploit/shell.pyc matches
routersploit/utils/__init__.py:113:    before executing command specific to modules (ex. 'run').
routersploit/utils/__init__.py:179:    multiple targets definition. Decorated function will be executed
Binary file routersploit/utils/__init__.pyc matches
routersploit/shell.py:33:    print_success("Welcome to cmd. Commands are sent to the target via the execute method.")
routersploit/shell.py:117:                    params['exec_binary'] = data
routersploit/shell.py:129:            print_status("Executing '{}' on the device...".format(cmd))
routersploit/shell.py:130:            print_info(exploit.execute(cmd))
routersploit/shell.py:155:    def __init__(self, exploit, payload, options, location="", wget_options={}, echo_options={}, exec_binary=None):
routersploit/shell.py:167:        # process of executing payload
routersploit/shell.py:168:        self.exec_binary = exec_binary
routersploit/shell.py:221:        self.exploit.execute(cmd)
routersploit/shell.py:260:            self.exploit.execute(cmd)
routersploit/shell.py:280:        # set of instructions to execute payload on the device
routersploit/shell.py:281:        if isinstance(self.exec_binary, list) or isinstance(self.exec_binary, tuple):
routersploit/shell.py:282:            for item_exec_binary in self.exec_binary:
routersploit/shell.py:283:                if isinstance(item_exec_binary, str):
routersploit/shell.py:285:                        commands.append(item_exec_binary.format(path))
routersploit/shell.py:287:                        commands.append(item_exec_binary)
routersploit/shell.py:288:                elif callable(item_exec_binary):
routersploit/shell.py:289:                    commands.append(item_exec_binary(path))
routersploit/shell.py:291:        # instruction to execute generic payload e.g. netcat / awk
routersploit/shell.py:292:        elif isinstance(self.exec_binary, str):
routersploit/shell.py:294:                commands.append(self.exec_binary.format(path))
routersploit/shell.py:296:                commands.append(self.exec_binary)
routersploit/shell.py:298:        # default way of executing payload
routersploit/shell.py:300:            exec_binary_str = "chmod 777 {0}; {0}; rm {0}".format(path)
routersploit/shell.py:301:            commands.append(exec_binary_str)
routersploit/shell.py:311:        # execute binary
routersploit/shell.py:314:        print_status("Executing payload on the device")
routersploit/shell.py:318:            self.exploit.execute(command)
routersploit/shell.py:320:        # asynchronous last command to execute binary & rm binary
routersploit/shell.py:321:        thread = threading.Thread(target=self.exploit.execute, args=(commands[-1],))
routersploit/shell.py:336:        # execute binary
routersploit/shell.py:341:            self.exploit.execute(command)
routersploit/shell.py:343:        # asynchronous last command to execute binary & rm binary
routersploit/shell.py:344:        thread = threading.Thread(target=self.exploit.execute, args=(commands[-1],))
tests/test_completer.py:38:            'exec     exit     help     search   show     use      \r\n',
tests/test_completer.py:97:            'back     exec     help     search   setg     use      \r\n'
tests/test_completer.py:201:            "back     exec     help     search   setg     use      \r\n"
tests/test_completer.py:214:            'back     exec     help     search   setg     unsetg   \r\n'
tests/test_interpreter.py:215:    def test_command_run_exception_during_exploit_execution(self,
tests/test_interpreter.py:298:            ['back', 'check', 'exec ', 'exit', 'help', 'run', 'search ',
tests/test_interpreter.py:307:            ['back', 'check', 'exec ', 'exit', 'help', 'run', 'search ',
tests/test_interpreter.py:317:            ['exec ', 'exit', 'help', 'search ', 'show ', 'use ']
tests/test_interpreter.py:677:    def test_command_exec(self, mock_system):
tests/test_interpreter.py:678:        self.interpreter.command_exec("foo -bar")
root@CRACK_COCAINE:~/Documents/routersploit# egrep -ix "show" * --color
grep: routersploit: Is a directory
grep: tests: Is a directory
root@CRACK_COCAINE:~/Documents/routersploit# egrep -irx "show" * --color
root@CRACK_COCAINE:~/Documents/routersploit# egrep -irx "show" * --color
root@CRACK_COCAINE:~/Documents/routersploit# egrep -irn "show" * --color
CONTRIBUTING.md:23:3. If exploit does not work but it should, check "show info" for more information. References should provide you with links to proof of concept exploits.
README.md:103:	rsf (D-LINK DIR-300 & DIR-600 RCE) > show options
README.md:137:	rsf (D-LINK DIR-300 & DIR-600 RCE) > show info
README.md:189:    rsf (SSH Default Creds) > show options
README.md:250:    rsf (D-Link Scanner) > show options
routersploit/interpreter.py:174:    show [info|options|devices]         Print information, options, or target devices for a module
routersploit/interpreter.py:185:        self.show_sub_commands = (
routersploit/interpreter.py:191:            ['use ', 'exec ', 'help', 'exit', 'show ', 'search ']
routersploit/interpreter.py:394:    def _show_info(self, *args, **kwargs):
routersploit/interpreter.py:402:    def _show_options(self, *args, **kwargs):
routersploit/interpreter.py:417:    def _show_devices(self, *args, **kwargs):  # TODO: cover with tests
routersploit/interpreter.py:433:    def __show_modules(self, root=''):
routersploit/interpreter.py:437:    def _show_all(self, *args, **kwargs):
routersploit/interpreter.py:438:        self.__show_modules()
routersploit/interpreter.py:440:    def _show_scanners(self, *args, **kwargs):
routersploit/interpreter.py:441:        self.__show_modules('scanners')
routersploit/interpreter.py:443:    def _show_exploits(self, *args, **kwargs):
routersploit/interpreter.py:444:        self.__show_modules('exploits')
routersploit/interpreter.py:446:    def _show_creds(self, *args, **kwargs):
routersploit/interpreter.py:447:        self.__show_modules('creds')
routersploit/interpreter.py:449:    def command_show(self, *args, **kwargs):
routersploit/interpreter.py:452:            getattr(self, "_show_{}".format(sub_command))(*args, **kwargs)
routersploit/interpreter.py:454:            utils.print_error("Unknown 'show' sub-command '{}'. "
routersploit/interpreter.py:455:                              "What do you want to show?\n"
routersploit/interpreter.py:456:                              "Possible choices are: {}".format(sub_command, self.show_sub_commands))
routersploit/interpreter.py:459:    def complete_show(self, text, *args, **kwargs):
routersploit/interpreter.py:461:            return [command for command in self.show_sub_commands if command.startswith(text)]
routersploit/interpreter.py:463:            return self.show_sub_commands
Binary file routersploit/interpreter.pyc matches
routersploit/modules/exploits/routers/cisco/ios_http_authorization_bypass.py:19:    Example: http://10.0.0.1/level/99/exec/show/startup/config
routersploit/modules/exploits/routers/cisco/ios_http_authorization_bypass.py:39:    show_command = exploits.Option('show startup-config', 'Command to be executed e.g show startup-config')
routersploit/modules/exploits/routers/cisco/ios_http_authorization_bypass.py:45:            url = "{}:{}/level/{}/exec/-/{}".format(self.target, self.port, self.access_level, self.show_command)
routersploit/modules/exploits/routers/cisco/ios_http_authorization_bypass.py:59:            url = "{}:{}/level/{}/exec/-/{}".format(self.target, self.port, num, self.show_command)
routersploit/modules/exploits/routers/cisco/ios_http_authorization_bypass.py:64:            if response.status_code == 200 and "Command was:  {}".format(self.show_command) in response.text:
routersploit/modules/exploits/routers/cisco/catalyst_2960_rocem.py:44:    device = exploits.Option(-1, 'Target device - use "show devices"', validators=validators.integer)
routersploit/modules/exploits/routers/cisco/catalyst_2960_rocem.py:55:                # next bytes are shown as offsets from r1
routersploit/modules/exploits/routers/cisco/catalyst_2960_rocem.py:118:                # next bytes are shown as offsets from r1
routersploit/modules/exploits/routers/cisco/catalyst_2960_rocem.py:176:            print_error("Set target device - use \"show devices\" and \"set device <id>\"")
routersploit/modules/exploits/routers/multi/misfortune_cookie.py:129:    device = exploits.Option('', 'Target device (show devices)')  # target firmware
routersploit/modules/exploits/routers/multi/rom0.py:30:            'http://www.osvdb.org/show/osvdb/102668',
routersploit/modules/exploits/routers/2wire/4011g_5012nv_path_traversal.py:48:            data = {"__ENH_SHOW_REDIRECT_PATH__": "/pages/C_4_0.asp/../../..{}".format(self.filename),
routersploit/modules/exploits/routers/2wire/4011g_5012nv_path_traversal.py:49:                    "__ENH_SUBMIT_VALUE_SHOW__": "Acceder",
routersploit/modules/exploits/routers/2wire/4011g_5012nv_path_traversal.py:68:        data = {"__ENH_SHOW_REDIRECT_PATH__": "/pages/C_4_0.asp/../../../etc/passwd",
routersploit/modules/exploits/routers/2wire/4011g_5012nv_path_traversal.py:69:                "__ENH_SUBMIT_VALUE_SHOW__": "Acceder",
routersploit/modules/exploits/routers/dlink/dir_300_320_600_615_info_disclosure.py:43:        url = "{}:{}/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd".format(self.target, self.port)
routersploit/modules/exploits/routers/dlink/dir_300_320_600_615_info_disclosure.py:60:        url = "{}:{}/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd".format(self.target, self.port)
Binary file routersploit/shell.pyc matches
routersploit/utils/__init__.py:369:    Pretty printing dictionary in specific order. (as in 'show info' command)
Binary file routersploit/utils/__init__.pyc matches
routersploit/shell.py:35:    print_status("For further exploitation use 'show payloads' and 'set payload <payload>' commands.")
routersploit/shell.py:52:        elif cmd == "show payloads":
routersploit/shell.py:79:            if cmd == "show options":
tests/test_completer.py:38:            'exec     exit     help     search   show     use      \r\n',
tests/test_completer.py:98:            'check    exit     run      set      show     \r\n',
tests/test_completer.py:138:            'search   set      setg     show     \r\n',
tests/test_completer.py:202:            "check    exit     run      set      show     \r\n",
tests/test_completer.py:215:            'check    exit     run      set      show     use      \r\n',
tests/test_completer.py:244:    def test_complete_show_raw(self):
tests/test_completer.py:249:            'show ',
tests/test_completer.py:252:    def test_complete_show(self):
tests/test_completer.py:254:        self.rsf.send("show \t\t")
tests/test_completer.py:261:    def test_complete_show_info(self):
tests/test_completer.py:263:        self.rsf.send("show i\t\t")
tests/test_completer.py:266:            'show info'
tests/test_completer.py:269:    def test_complete_show_options(self):
tests/test_completer.py:271:        self.rsf.send("show o\t\t")
tests/test_completer.py:274:            'show options'
tests/test_interpreter.py:299:             'set ', 'setg ', 'show ', 'use ']
tests/test_interpreter.py:308:             'set ', 'setg ', 'show ', 'unsetg ', 'use ']
tests/test_interpreter.py:317:            ['exec ', 'exit', 'help', 'search ', 'show ', 'use ']
tests/test_interpreter.py:418:    def test_show_info(self, mock_print):
tests/test_interpreter.py:430:        self.interpreter._show_info()
tests/test_interpreter.py:449:    def test_command_show_info_module_with_no_metadata(self, mock_print):
tests/test_interpreter.py:455:        self.interpreter._show_info()
tests/test_interpreter.py:462:    def test_show_options(self, mock_print):
tests/test_interpreter.py:481:        self.interpreter._show_options()
tests/test_interpreter.py:509:    def test_command_show_options_when_there_is_no_module_opts(self,
tests/test_interpreter.py:522:        self.interpreter._show_options()
tests/test_interpreter.py:541:    def test_command_show(self):
tests/test_interpreter.py:543:                               "_show_options") as mock_show_options:
tests/test_interpreter.py:544:            self.interpreter.command_show("options")
tests/test_interpreter.py:545:            mock_show_options.assert_called_once_with("options")
tests/test_interpreter.py:548:    def test_command_show_unknown_sub_command(self, mock_print_error):
tests/test_interpreter.py:549:        self.interpreter.command_show('unknown_sub_command')
tests/test_interpreter.py:551:            "Unknown 'show' sub-command 'unknown_sub_command'. "
tests/test_interpreter.py:552:            "What do you want to show?\n"
tests/test_interpreter.py:554:                self.interpreter.show_sub_commands))
tests/test_interpreter.py:557:    def test_show_all(self, mock_print):
tests/test_interpreter.py:567:        self.interpreter._show_all()
tests/test_interpreter.py:581:    def test_show_scanners(self, mock_print):
tests/test_interpreter.py:591:        self.interpreter._show_scanners()
tests/test_interpreter.py:598:    def test_show_exploits(self, mock_print):
tests/test_interpreter.py:608:        self.interpreter._show_exploits()
tests/test_interpreter.py:615:    def test_show_creds(self, mock_print):
tests/test_interpreter.py:625:        self.interpreter._show_creds()
tests/test_interpreter.py:643:    def test_if_command_show_info_has_module_required_decorator(self):
tests/test_interpreter.py:645:            self.interpreter._show_info,
tests/test_interpreter.py:649:    def test_if_command_show_options_has_module_required_decorator(self):
tests/test_interpreter.py:651:            self.interpreter._show_options,
tests/test_interpreter.py:655:    def test_if_command_show_devices_has_module_required_decorator(self):
tests/test_interpreter.py:657:            self.interpreter._show_devices,
tests/test_interpreter.py:672:        cmd, args = self.interpreter.parse_line("show options")
tests/test_interpreter.py:673:        self.assertEqual(cmd, "show")
root@CRACK_COCAINE:~/Documents/routersploit# egrep -irn "cmd ==" * --color
routersploit/interpreter.py:117:                if cmd == '':
routersploit/shell.py:52:        elif cmd == "show payloads":
routersploit/shell.py:79:            if cmd == "show options":
routersploit/shell.py:102:            elif cmd == "run":
routersploit/shell.py:125:            elif cmd == "back":
root@CRACK_COCAINE:~/Documents/routersploit# ls
CONTRIBUTING.md  LICENSE   README.md		 requirements.txt  routersploit.log  tests
Dockerfile	 Makefile  requirements-dev.txt  routersploit	   rsf.py
root@CRACK_COCAINE:~/Documents/routersploit# ls */*.log
ls: cannot access '*/*.log': No such file or directory
root@CRACK_COCAINE:~/Documents/routersploit# ls */*.log
ls: cannot access '*/*.log': No such file or directory
root@CRACK_COCAINE:~/Documents/routersploit# ls *.log/*.log
ls: cannot access '*.log/*.log': No such file or directory
root@CRACK_COCAINE:~/Documents/routersploit# ls
CONTRIBUTING.md  LICENSE   README.md		 requirements.txt  routersploit.log  tests
Dockerfile	 Makefile  requirements-dev.txt  routersploit	   rsf.py
root@CRACK_COCAINE:~/Documents/routersploit# cd routersploit
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# ls
exceptions.py	exploits.pyc  interpreter.py   payloads.py   printer.pyc  templates    utils	       wordlists
exceptions.pyc	__init__.py   interpreter.pyc  payloads.pyc  shell.py	  threads.py   validators.py
exploits.py	__init__.pyc  modules	       printer.py    shell.pyc	  threads.pyc  validators.pyc
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# ls *.log
ls: cannot access '*.log': No such file or directory
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# ls -la
total 164
drwxr-xr-x 6 root root  4096 Dec 13 10:58 .
drwxr-xr-x 6 root root  4096 Dec 13 10:58 ..
-rw-r--r-- 1 root root   343 Dec 13 10:15 exceptions.py
-rw-r--r-- 1 root root   945 Dec 13 10:31 exceptions.pyc
-rw-r--r-- 1 root root  4078 Dec 13 10:15 exploits.py
-rw-r--r-- 1 root root  5152 Dec 13 10:31 exploits.pyc
-rw-r--r-- 1 root root   460 Dec 13 10:15 __init__.py
-rw-r--r-- 1 root root   797 Dec 13 10:31 __init__.pyc
-rw-r--r-- 1 root root 18793 Dec 13 10:15 interpreter.py
-rw-r--r-- 1 root root 21898 Dec 13 10:58 interpreter.pyc
drwxr-xr-x 6 root root  4096 Dec 13 10:31 modules
-rw-r--r-- 1 root root  5804 Dec 13 10:15 payloads.py
-rw-r--r-- 1 root root  5797 Dec 13 10:31 payloads.pyc
-rw-r--r-- 1 root root   618 Dec 13 10:15 printer.py
-rw-r--r-- 1 root root  1172 Dec 13 10:31 printer.pyc
-rw-r--r-- 1 root root 12397 Dec 13 10:15 shell.py
-rw-r--r-- 1 root root 10669 Dec 13 10:31 shell.pyc
drwxr-xr-x 2 root root  4096 Dec 13 10:15 templates
-rw-r--r-- 1 root root  2457 Dec 13 10:15 threads.py
-rw-r--r-- 1 root root  3417 Dec 13 10:58 threads.pyc
drwxr-xr-x 2 root root  4096 Dec 13 10:31 utils
-rw-r--r-- 1 root root  2725 Dec 13 10:15 validators.py
-rw-r--r-- 1 root root  3328 Dec 13 10:31 validators.pyc
drwxr-xr-x 2 root root  4096 Dec 13 10:31 wordlists
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# atom shell.py
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# ls
exceptions.py	exploits.pyc  interpreter.py   payloads.py   printer.pyc  templates    utils	       wordlists
exceptions.pyc	__init__.py   interpreter.pyc  payloads.pyc  shell.py	  threads.py   validators.py
exploits.py	__init__.pyc  modules	       printer.py    shell.pyc	  threads.pyc  validators.pyc
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# python shell.py
Traceback (most recent call last):
File "shell.py", line 12, in <module>
 from routersploit import validators
ImportError: No module named routersploit
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# python shell.py
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 220016  8588 ?        Ss   05:49   0:04 /sbin/init
root         2  0.0  0.0      0     0 ?        S    05:49   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    05:49   0:00 [ksoftirqd/0]
root         5  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    05:49   0:02 [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    05:49   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        S    05:49   0:00 [migration/0]
root        10  0.0  0.0      0     0 ?        S<   05:49   0:00 [lru-add-drain]
root        11  0.0  0.0      0     0 ?        S    05:49   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    05:49   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    05:49   0:00 [cpuhp/1]
root        14  0.0  0.0      0     0 ?        S    05:49   0:00 [watchdog/1]
root        15  0.0  0.0      0     0 ?        S    05:49   0:00 [migration/1]
root        16  0.0  0.0      0     0 ?        S    05:49   0:00 [ksoftirqd/1]
root        18  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/1:0H]
root        19  0.0  0.0      0     0 ?        S    05:49   0:00 [cpuhp/2]
root        20  0.0  0.0      0     0 ?        S    05:49   0:00 [watchdog/2]
root        21  0.0  0.0      0     0 ?        S    05:49   0:00 [migration/2]
root        22  0.0  0.0      0     0 ?        S    05:49   0:00 [ksoftirqd/2]
root        24  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/2:0H]
root        25  0.0  0.0      0     0 ?        S    05:49   0:00 [cpuhp/3]
root        26  0.0  0.0      0     0 ?        S    05:49   0:00 [watchdog/3]
root        27  0.0  0.0      0     0 ?        S    05:49   0:00 [migration/3]
root        28  0.0  0.0      0     0 ?        S    05:49   0:00 [ksoftirqd/3]
root        30  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/3:0H]
root        31  0.0  0.0      0     0 ?        S    05:49   0:00 [kdevtmpfs]
root        32  0.0  0.0      0     0 ?        S<   05:49   0:00 [netns]
root        33  0.0  0.0      0     0 ?        S    05:49   0:00 [khungtaskd]
root        34  0.0  0.0      0     0 ?        S    05:49   0:00 [oom_reaper]
root        35  0.0  0.0      0     0 ?        S<   05:49   0:00 [writeback]
root        36  0.0  0.0      0     0 ?        S    05:49   0:00 [kcompactd0]
root        38  0.0  0.0      0     0 ?        SN   05:49   0:00 [ksmd]
root        39  0.0  0.0      0     0 ?        SN   05:49   0:00 [khugepaged]
root        40  0.0  0.0      0     0 ?        S<   05:49   0:00 [crypto]
root        41  0.0  0.0      0     0 ?        S<   05:49   0:00 [kintegrityd]
root        42  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root        43  0.0  0.0      0     0 ?        S<   05:49   0:00 [kblockd]
root        47  0.0  0.0      0     0 ?        S<   05:49   0:00 [devfreq_wq]
root        48  0.0  0.0      0     0 ?        S<   05:49   0:00 [watchdogd]
root        49  0.0  0.0      0     0 ?        S    05:49   0:00 [kswapd0]
root        50  0.0  0.0      0     0 ?        S<   05:49   0:00 [vmstat]
root        62  0.0  0.0      0     0 ?        S<   05:49   0:00 [kthrotld]
root        63  0.0  0.0      0     0 ?        S<   05:49   0:00 [ipv6_addrconf]
root       109  0.0  0.0      0     0 ?        S<   05:49   0:00 [acpi_thermal_pm]
root       111  0.0  0.0      0     0 ?        S<   05:49   0:00 [ata_sff]
root       152  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_0]
root       153  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_0]
root       154  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_1]
root       155  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_1]
root       156  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_2]
root       157  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_2]
root       158  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_3]
root       159  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_3]
root       160  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_4]
root       161  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_4]
root       162  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_5]
root       163  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_5]
root       171  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root       172  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root       173  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root       174  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root       176  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/0:1H]
root       180  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/2:1H]
root       181  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/3:1H]
root       182  0.0  0.0      0     0 ?        S<   05:49   0:00 [kworker/1:1H]
root       187  0.0  0.0      0     0 ?        S<   05:49   0:00 [md]
root       209  0.0  0.0      0     0 ?        S<   05:49   0:00 [raid5wq]
root       226  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root       265  0.0  0.0      0     0 ?        S<   05:49   0:00 [ext4-rsv-conver]
root       312  0.0  0.0  81684 10600 ?        Ss   05:49   0:00 /lib/systemd/systemd-journald
root       317  0.0  0.0      0     0 ?        S    05:49   0:00 [kauditd]
root       357  0.0  0.0      0     0 ?        S    05:49   0:00 [nvidia-modeset]
root       360  0.0  0.0  46012  5316 ?        Ss   05:49   0:00 /lib/systemd/systemd-udevd
root       394  0.0  0.0      0     0 ?        S<   05:49   0:00 [edac-poller]
root       401  0.0  0.0      0     0 ?        S    05:49   0:00 [irq/31-mei_me]
systemd+   444  0.0  0.0 147096  5156 ?        Ssl  05:49   0:00 /lib/systemd/systemd-timesyncd
root       578  0.0  0.0      0     0 ?        S    05:49   0:00 [scsi_eh_6]
root       579  0.0  0.0      0     0 ?        S<   05:49   0:00 [scsi_tmf_6]
root       580  0.0  0.0      0     0 ?        S    05:49   0:00 [usb-storage]
root       599  0.0  0.0      0     0 ?        S<   05:49   0:00 [bioset]
root       645  0.0  0.0  29624  2928 ?        Ss   05:49   0:00 /usr/sbin/cron -f
root       646  0.0  0.0 427140  9064 ?        Ssl  05:49   0:00 /usr/sbin/ModemManager
root       649  0.0  0.0  25336  4608 ?        Ss   05:49   0:00 /usr/sbin/smartd -n
root       654  0.0  0.0 116156  3388 ?        Ssl  05:49   0:00 /usr/sbin/irqbalance --foreground
root       655  0.0  0.0 275496  4004 ?        Ssl  05:49   0:00 /usr/sbin/rsyslogd -n
message+   656  0.0  0.0  48772  5356 ?        Ss   05:49   0:03 /usr/bin/dbus-daemon --system --address=systemd: --nofork --no
root       662  0.0  0.0  50912  2976 ?        S    05:49   0:00 /usr/sbin/CRON -f
root       667  0.0  0.0  50912  2960 ?        S    05:49   0:00 /usr/sbin/CRON -f
root       679  0.0  0.1 454332 15496 ?        Ssl  05:49   0:00 /usr/sbin/NetworkManager --no-daemon
root       681  0.0  0.0  65236  5724 ?        Ss   05:49   0:00 /lib/systemd/systemd-logind
root       682  0.0  0.0 285712  6608 ?        Ssl  05:49   0:00 /usr/lib/accountsservice/accounts-daemon
rtkit      684  0.0  0.0 187832  3024 ?        SNsl 05:49   0:00 /usr/lib/rtkit/rtkit-daemon
root       699  0.0  0.0 290228  8484 ?        Ssl  05:49   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       712  0.0  0.0   4312   760 ?        Ss   05:49   0:00 /bin/sh -c python /root/ArmsCommander/passwordattacks/autostar
root       725  0.0  0.0   4312   740 ?        Ss   05:49   0:00 /bin/sh -c /bin/sh /usr/local/bin/IDS.sh
root       726  0.0  0.0  32088  9892 ?        S    05:49   0:00 python /root/ArmsCommander/passwordattacks/autostart_password_
root       732  0.0  0.0   4312   772 ?        S    05:49   0:00 /bin/sh /usr/local/bin/IDS.sh
root       775  0.0  0.0   8500  1564 ?        Ss   05:49   0:00 nvidia-persistenced --persistence-mode
root       778  0.7  0.0      0     0 ?        S    05:49   3:16 [irq/33-nvidia]
root       779  0.0  0.0      0     0 ?        S    05:49   0:00 [nvidia]
pulse      825  0.0  0.0 357068 11264 ?        S<l  05:49   0:00 pulseaudio -D --system
root       836  0.0  0.0  19872  9060 ?        Ss   05:49   0:00 /sbin/mount.ntfs /dev/sda2 /mnt/Data2 -o rw
root       840  0.0  0.1 190896 14508 ?        S    05:49   0:06 /usr/bin/python -O /usr/share/wicd/daemon/wicd-daemon.py --kee
root       842  0.0  0.0  13300  2648 ?        Ss   05:49   0:00 /sbin/mount.ntfs /dev/sdb2 /mnt/Data3 -o rw
root       858  0.0  0.1 111348 17848 ?        S    05:49   0:02 /usr/bin/python -O /usr/share/wicd/daemon/monitor.py
root       900  0.0  0.0  13052  2388 ?        Ss   05:49   0:00 /sbin/mount.ntfs /dev/sdc1 /mnt/Data4 -o rw
root       909  0.0  0.0      0     0 ?        S<   05:49   0:00 [iprt-VBoxWQueue]
root       921  0.0  0.0      0     0 ?        S    05:49   0:00 [iprt-VBoxTscThr]
root       942  0.0  0.0  20484  1040 ?        Ss   05:49   0:00 dhclient eth0
root       951  0.0  0.0  71996  5564 ?        Ss   05:49   0:00 /usr/sbin/sshd -D
root       962  0.0  0.0 371556  7600 ?        Ssl  05:49   0:00 /usr/sbin/gdm3
root       984  0.0  0.0 243928  7564 ?        Sl   05:49   0:00 gdm-session-worker [pam/gdm-launch-environment]
Debian-+  1019  0.0  0.0  80020  7988 ?        Ss   05:49   0:00 /lib/systemd/systemd --user
Debian-+  1020  0.0  0.0 102172  2384 ?        S    05:49   0:00 (sd-pam)
root      1039  0.0  0.0      0     0 ?        S    05:49   0:00 [UVM global queu]
root      1041  0.0  0.0      0     0 ?        S    05:49   0:00 [UVM Tools Event]
Debian-+  1062  0.0  0.0 203236  5324 tty1     Ssl+ 05:49   0:00 /usr/lib/gdm3/gdm-x-session gnome-session --autostart /usr/sha
root      1073  0.0  0.4 267228 49324 tty1     Sl+  05:49   0:01 /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth /run/user/132/gdm/Xa
Debian-+  1175  0.0  0.0  47336  4032 ?        Ss   05:49   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --n
Debian-+  1177  0.0  0.1 553208 12440 tty1     Sl+  05:49   0:00 /usr/lib/gnome-session/gnome-session-binary --autostart /usr/s
Debian-+  1183  0.0  0.0 355200  6228 ?        Ssl  05:49   0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
Debian-+  1188  0.0  0.0  47116  3488 ?        S    05:49   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2
Debian-+  1191  0.0  0.0 222348  5312 ?        Sl   05:49   0:00 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
Debian-+  1200  0.0  1.3 2274720 159764 tty1   Sl+  05:49   0:03 /usr/bin/gnome-shell
root      1204  0.0  0.0 313532  8516 ?        Ssl  05:49   0:00 /usr/lib/upower/upowerd
Debian-+  1236  0.0  0.0 1229632 11912 ?       Ssl  05:49   0:00 /usr/bin/pulseaudio --daemonize=no
root      1248  0.0  0.2 444476 31020 ?        Ssl  05:50   0:02 /usr/lib/packagekit/packagekitd
Debian-+  1249  0.0  0.2 1025836 29760 tty1    Sl+  05:50   0:00 /usr/lib/gnome-settings-daemon/gnome-settings-daemon
root      1263  0.0  0.0  48328  5132 ?        Ss   05:50   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
colord    1269  0.0  0.1 317520 13508 ?        Ssl  05:50   0:00 /usr/lib/colord/colord
root      1400  0.0  0.0   4312  1648 ?        S    05:54   0:00 /bin/sh /root/Desktop/external_scans_njp_dnac/edit_2__bash_scr
root      1401  0.0  0.0   4312  1632 ?        S    05:54   0:00 /bin/sh /root/Desktop/external_scans_njp_dnac/nmap_ssl_detecti
root      1434  0.0  1.4 594104 179572 ?       Sl   05:54   0:03 snort -q -A full -c /etc/snort/snort.conf
postgres  1508  0.0  0.1 276848 24164 ?        S    05:54   0:00 /usr/lib/postgresql/9.5/bin/postgres -D /var/lib/postgresql/9.
postgres  1511  0.0  0.2 293676 25356 ?        S    05:54   0:00 /usr/lib/postgresql/9.6/bin/postgres -D /var/lib/postgresql/9.
postgres  1523  0.0  0.0 293676  3976 ?        Ss   05:54   0:00 postgres: 9.6/main: checkpointer process
postgres  1524  0.0  0.0 293676  3976 ?        Ss   05:54   0:00 postgres: 9.6/main: writer process
postgres  1525  0.0  0.0 293676  3976 ?        Ss   05:54   0:00 postgres: 9.6/main: wal writer process
postgres  1526  0.0  0.0 294104  6396 ?        Ss   05:54   0:00 postgres: 9.6/main: autovacuum launcher process
postgres  1527  0.0  0.0 148676  3172 ?        Ss   05:54   0:00 postgres: 9.6/main: stats collector process
postgres  1534  0.0  0.0 276948 10940 ?        Ss   05:54   0:00 postgres: 9.5/main: checkpointer process
postgres  1535  0.0  0.0 276848  6196 ?        Ss   05:54   0:00 postgres: 9.5/main: writer process
postgres  1536  0.0  0.0 276848  9544 ?        Ss   05:54   0:00 postgres: 9.5/main: wal writer process
postgres  1537  0.0  0.0 277280  6780 ?        Ss   05:54   0:00 postgres: 9.5/main: autovacuum launcher process
postgres  1538  0.0  0.0 132004  4860 ?        Ss   05:54   0:00 postgres: 9.5/main: stats collector process
root      4164  0.0  0.0 248052  7768 ?        Sl   05:59   0:00 gdm-session-worker [pam/gdm-password]
root      4169  0.0  0.0  71576  7748 ?        Ss   05:59   0:00 /lib/systemd/systemd --user
root      4170  0.0  0.0 249636  2424 ?        S    05:59   0:00 (sd-pam)
root      4177  0.0  0.0 287764  7876 ?        Sl   05:59   0:00 /usr/bin/gnome-keyring-daemon --daemonize --login
root      4181  0.0  0.0 203236  5464 tty2     Ssl+ 05:59   0:00 /usr/lib/gdm3/gdm-x-session --run-script default
root      4183  0.6  0.6 315908 73964 tty2     Sl+  05:59   2:49 /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/0/gdm/Xaut
root      4187  0.0  0.0  48112  5004 ?        Ss   05:59   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --n
root      4189  0.0  0.1 774704 13264 tty2     Sl+  05:59   0:00 /usr/lib/gnome-session/gnome-session-binary
root      4244  0.0  0.0  11100   332 ?        Ss   05:59   0:00 /usr/bin/ssh-agent x-session-manager
root      4251  0.0  0.0 355208  6404 ?        Ssl  05:59   0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
root      4256  0.0  0.0  47240  3908 ?        S    05:59   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2
root      4259  0.0  0.0 222348  6844 ?        Sl   05:59   0:02 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
root      4276  1.2  4.2 3012136 523172 tty2   Sl+  05:59   5:04 /usr/bin/gnome-shell
root      4279  0.0  0.0 285212  6796 ?        Ssl  05:59   0:00 /usr/lib/gvfs/gvfsd
root      4284  0.0  0.0 417780  5472 ?        Sl   05:59   0:00 /usr/lib/gvfs/gvfsd-fuse /run/user/0/gvfs -f -o big_writes
root      4294  0.0  0.1 2284756 13428 ?       S<sl 05:59   0:01 /usr/bin/pulseaudio --daemonize=no
root      4301  0.0  0.1 615016 15260 ?        Sl   05:59   0:00 /usr/lib/gnome-shell/gnome-shell-calendar-server
root      4312  0.0  0.1 1229040 21172 ?       Ssl  05:59   0:00 /usr/lib/evolution/evolution-source-registry
root      4317  0.0  0.0 468280 11700 ?        Ssl  05:59   0:00 /usr/lib/telepathy/mission-control-5
root      4322  0.0  0.2 769136 33164 ?        Sl   05:59   0:00 /usr/lib/gnome-online-accounts/goa-daemon
root      4324  0.0  0.0 359628 11140 ?        Ssl  05:59   0:00 /usr/lib/gvfs/gvfs-udisks2-volume-monitor
root      4328  0.0  0.0 380244  8420 ?        Ssl  05:59   0:06 /usr/lib/udisks2/udisksd --no-debug
root      4335  0.0  0.0 269568  5936 ?        Ssl  05:59   0:00 /usr/lib/gvfs/gvfs-goa-volume-monitor
root      4348  0.0  0.0 370416  7452 ?        Sl   05:59   0:00 /usr/lib/gnome-online-accounts/goa-identity-service
root      4357  0.0  0.0 271368  5204 ?        Ssl  05:59   0:00 /usr/lib/gvfs/gvfs-mtp-volume-monitor
root      4361  0.0  0.0 374324  7344 ?        Ssl  05:59   0:00 /usr/lib/gvfs/gvfs-afc-volume-monitor
root      4366  0.0  0.0 283740  6240 ?        Ssl  05:59   0:00 /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
root      4372  0.0  0.3 1501824 40612 tty2    Sl+  05:59   0:01 /usr/lib/gnome-settings-daemon/gnome-settings-daemon
root      4383  0.0  0.0 187504  4868 ?        Sl   05:59   0:00 /usr/lib/dconf/dconf-service
root      4402  0.0  0.0 442468 11988 tty2     SNl+ 05:59   0:00 /usr/lib/tracker/tracker-miner-apps
root      4406  0.0  0.0 503548 11800 tty2     Sl+  05:59   0:00 /usr/lib/gnome-settings-daemon/gsd-printer
root      4407  0.0  0.2 896700 25800 tty2     SNl+ 05:59   0:01 /usr/lib/tracker/tracker-extract
root      4413  0.0  0.2 697632 34676 tty2     Sl+  05:59   0:08 psensor
root      4420  0.0  0.0 426144  8036 ?        Ssl  05:59   0:00 /usr/bin/zeitgeist-daemon
root      4428  0.0  0.1 441384 18492 ?        Sl   05:59   0:00 zeitgeist-datahub
root      4432  0.0  0.0 341280 12172 tty2     SNl+ 05:59   0:00 /usr/lib/tracker/tracker-miner-user-guides
root      4433  0.0  0.8 936708 109568 tty2    Sl+  05:59   0:02 /usr/bin/gnome-software --gapplication-service
root      4434  0.0  0.3 398160 38368 tty2     Sl+  05:59   0:00 /usr/bin/python -O /usr/share/wicd/gtk/wicd-client.py --tray
root      4435  0.0  0.1 329128 16240 ?        Ssl  05:59   0:00 /usr/lib/zeitgeist/zeitgeist/zeitgeist-fts
root      4448  0.0  0.3 1252228 41124 tty2    Sl+  05:59   0:01 nautilus-desktop
root      4455  0.0  0.2 838396 32404 ?        Ssl  05:59   0:00 /usr/lib/evolution/evolution-calendar-factory
root      4469  0.0  0.5 472696 62988 ?        Ssl  05:59   0:00 /usr/lib/tracker/tracker-store
root      4490  0.0  0.0 361372  6760 ?        Sl   06:00   0:00 /usr/lib/gvfs/gvfsd-trash --spawner :1.17 /org/gtk/gvfs/exec_s
root      4528  0.0  0.1 874164 24140 ?        Sl   06:00   0:00 /usr/lib/evolution/evolution-calendar-factory-subprocess --fac
root      4538  0.0  0.1 711224 20136 ?        Sl   06:00   0:00 /usr/lib/evolution/evolution-calendar-factory-subprocess --fac
root      4543  0.0  0.1 707516 22508 ?        Ssl  06:00   0:00 /usr/lib/evolution/evolution-addressbook-factory
root      4556  0.0  0.1 847816 22520 ?        Sl   06:00   0:00 /usr/lib/evolution/evolution-addressbook-factory-subprocess --
root      4592  0.0  0.0 195860  5904 ?        Ssl  06:00   0:00 /usr/lib/gvfs/gvfsd-metadata
root      4706  0.0  0.0  73248  5680 ?        S    06:00   0:00 /usr/lib/x86_64-linux-gnu/gconf/gconfd-2
root     12661  0.0  0.4  97744 50384 ?        S    09:21   0:03 nmap -sV --version-all -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA
root     14894  0.0  0.0   4312   756 ?        S    10:05   0:00 /bin/sh /root/Desktop/external_scans_njp_dnac/edit_2__bash_scr
root     14895  0.0  0.0   4312   760 ?        S    10:05   0:00 /bin/sh /root/Desktop/external_scans_njp_dnac/nmap_ssl_detecti
root     14925  0.0  0.0      0     0 ?        S    10:05   0:00 [kworker/0:1]
debian-+ 16497  0.0  0.3  95956 46616 ?        Ss   10:06   0:03 /usr/bin/tor --defaults-torrc /usr/share/tor/tor-service-defau
root     17557  0.0  0.4  98292 51092 ?        S    10:11   0:03 nmap -sV --version-all -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA
root     17606  0.0  0.0      0     0 ?        S    10:12   0:00 [kworker/2:1]
root     18365  0.0  0.0  20484  4344 ?        S    10:14   0:00 /sbin/dhclient -d -q -sf /usr/lib/NetworkManager/nm-dhcp-helpe
root     18366  0.0  0.0  20488  4492 ?        S    10:14   0:00 /sbin/dhclient -d -q -6 -N -sf /usr/lib/NetworkManager/nm-dhcp
root     18649  0.0  0.4  98528 51184 ?        S    10:16   0:02 nmap -sV --version-all -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA
root     18927  0.0  0.0      0     0 ?        S    10:21   0:00 [kworker/2:0]
root     20617  0.0  0.0 355524 10588 ?        Sl   10:58   0:00 /usr/lib/gvfs/gvfsd-http --spawner :1.17 /org/gtk/gvfs/exec_sp
root     21636  0.1  0.3 674912 45324 ?        Rsl  11:16   0:06 /usr/lib/gnome-terminal/gnome-terminal-server
root     21685  0.0  0.0  19904  3748 pts/0    Ss   11:16   0:00 bash
root     21731  0.0  0.0  11196  1852 ?        S    11:17   0:00 /bin/bash /usr/bin/atom automated_routersploit.py
root     21733  0.7  1.8 1701044 229200 ?      Sl   11:17   0:46 /usr/share/atom/atom --executed-from=/root/Desktop/projects --
root     21735  0.0  0.2 386384 31508 ?        S    11:17   0:00 /usr/share/atom/atom --type=zygote --no-sandbox
root     21752  0.7  1.2 618452 157900 ?       Sl   11:17   0:45 /usr/share/atom/atom --type=gpu-process --channel=21733.0.1796
root     21766  4.5  2.9 2677712 358404 ?      SLl  11:17   4:26 /usr/share/atom/atom --type=renderer --no-sandbox --primordial
root     21798  0.0  1.4 1037400 175488 ?      Sl   11:17   0:00 /usr/share/atom/atom --eval CompileCache = require('/usr/share
root     21860  0.0  1.5 1125292 191380 ?      Sl   11:17   0:01 /usr/share/atom/atom --type=renderer --no-sandbox --primordial
root     22657  0.0  0.4  98168 51076 ?        S    11:38   0:02 nmap -sV --version-all -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA
root     22727  0.9  1.3 1300788 170308 tty2   SLl+ 11:38   0:45 /usr/lib/x86_64-linux-gnu/opera/opera
root     22732  0.0  0.0   6372   764 tty2     S+   11:38   0:00 /usr/lib/x86_64-linux-gnu/opera/opera_sandbox /usr/lib/x86_64-
root     22733  0.0  0.2 414796 28468 tty2     S+   11:38   0:00 /usr/lib/x86_64-linux-gnu/opera/opera --type=zygote
root     22735  0.0  0.0 414796  6836 tty2     S+   11:38   0:00 /usr/lib/x86_64-linux-gnu/opera/opera --type=zygote
root     22770  0.3  1.5 631396 184436 tty2    Sl+  11:38   0:14 /usr/lib/x86_64-linux-gnu/opera/opera --type=gpu-process --fie
root     22815  0.0  0.1 449624 16872 tty2     S+   11:38   0:00 /usr/lib/x86_64-linux-gnu/opera/opera --type=gpu-broker
root     22837  0.0  0.8 903308 99284 tty2     Sl+  11:38   0:02 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     22869  0.4  1.5 1030196 188436 tty2   Sl+  11:38   0:22 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     22874  0.0  0.8 867616 108284 tty2    Sl+  11:38   0:01 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     22958  0.3  0.5 793020 70780 tty2     Sl+  11:39   0:14 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     22981  0.0  0.8 897684 106020 tty2    Sl+  11:39   0:01 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     23709  0.0  0.0      0     0 ?        S    12:04   0:00 [kworker/0:2]
root     23710  0.0  0.0      0     0 ?        S    12:04   0:01 [kworker/1:1]
root     23801  0.0  0.0      0     0 ?        S    12:04   0:00 [kworker/3:1]
root     25827  0.0  0.2 152444 30960 pts/0    Sl+  12:30   0:00 python rsf.py
root     25835  0.0  0.0  19904  3744 pts/2    Ss   12:30   0:00 bash
root     25838  0.1  0.2  78772 31192 pts/2    T    12:30   0:02 python
root     25883  0.3  0.0      0     0 ?        S    12:32   0:04 [kworker/1:3]
root     26038  0.0  0.0      0     0 ?        S    12:35   0:00 [kworker/u8:2]
root     26117  2.5  0.2  78772 31284 pts/2    T    12:38   0:24 python
root     26142  0.0  0.9 850144 121776 tty2    Sl+  12:38   0:00 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     26188  0.0  0.0  19908  3740 pts/3    Ss   12:40   0:00 bash
root     26262  0.0  0.0      0     0 ?        S    12:43   0:00 [kworker/u8:0]
root     26321  0.0  0.0   4312   772 ?        S    12:45   0:00 sh -c /usr/local/bin/pp64.bin /root/Documents/wifi_cracking_wo
root     26322  0.5  1.5 189684 186780 ?       S    12:45   0:02 /usr/local/bin/pp64.bin /root/Documents/wifi_cracking_wordlist
root     26323 39.5  2.1 14749888 266600 ?     Sl   12:45   3:36 hashcat -a 0 -w 4 -m 2500 /root/ArmsCommander/logs/HashCat/has
root     26324  0.0  0.0      0     0 ?        S    12:45   0:00 [UVM GPU1 BH]
root     26361  0.0  0.0      0     0 ?        S    12:46   0:00 [kworker/3:0]
root     26427  0.2  0.9 913408 111736 tty2    Sl+  12:48   0:00 /usr/lib/x86_64-linux-gnu/opera/opera --type=renderer --field-
root     26509  0.0  0.2  78516 30724 pts/2    S+   12:49   0:00 python
root     26631  0.0  0.0      0     0 ?        S    12:51   0:00 [kworker/3:2]
root     26773  0.0  0.0  40320  3264 pts/3    R+   12:54   0:00 ps aux
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# cd /root/Documents/routersploit/
root@CRACK_COCAINE:~/Documents/routersploit# ls
CONTRIBUTING.md  LICENSE   README.md		 requirements.txt  routersploit.log  tests
Dockerfile	 Makefile  requirements-dev.txt  routersploit	   rsf.py
root@CRACK_COCAINE:~/Documents/routersploit# cat routersploit.log
2017-12-13 10:58:29,120 ERROR routersploit.exceptions       Error during loading 'routersploit/modules/scanners/autopwn'

Error: 'module' object has no attribute 'optionsParser'

It should be valid path to the module. Use <tab> key multiple times for completion.
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/utils/__init__.py", line 66, in import_exploit
 module = importlib.import_module(path)
File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
 __import__(name)
File "/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py", line 103, in <module>
 main()
File "/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py", line 92, in main
 parser = optparse.optionsParser('usage %parser -r <manual control> -a full auto')
AttributeError: 'module' object has no attribute 'optionsParser'
2017-12-13 10:59:03,109 ERROR routersploit.exceptions       Unknown command: 'options'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_options'
2017-12-13 10:59:45,547 ERROR routersploit.exceptions       Unknown command: 'shpw'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shpw'
2017-12-13 11:07:26,917 ERROR routersploit.exceptions       Unknown command: 'jobs'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_jobs'
2017-12-13 12:43:21,542 ERROR routersploit.exceptions       Unknown command: 'hrelep'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_hrelep'
2017-12-13 12:54:46,998 ERROR routersploit.exceptions       Unknown command: 'shell'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shell'
2017-12-13 12:54:51,933 ERROR routersploit.exceptions       Unknown command: 'shell('')'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shell('')'
2017-12-13 12:55:16,471 ERROR routersploit.exceptions       Unknown command: '-v'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_-v'
2017-12-13 12:55:18,348 ERROR routersploit.exceptions       Unknown command: 'version'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_version'
root@CRACK_COCAINE:~/Documents/routersploit# cat routersploit.log
2017-12-13 10:58:29,120 ERROR routersploit.exceptions       Error during loading 'routersploit/modules/scanners/autopwn'

Error: 'module' object has no attribute 'optionsParser'

It should be valid path to the module. Use <tab> key multiple times for completion.
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/utils/__init__.py", line 66, in import_exploit
 module = importlib.import_module(path)
File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
 __import__(name)
File "/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py", line 103, in <module>
 main()
File "/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py", line 92, in main
 parser = optparse.optionsParser('usage %parser -r <manual control> -a full auto')
AttributeError: 'module' object has no attribute 'optionsParser'
2017-12-13 10:59:03,109 ERROR routersploit.exceptions       Unknown command: 'options'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_options'
2017-12-13 10:59:45,547 ERROR routersploit.exceptions       Unknown command: 'shpw'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shpw'
2017-12-13 11:07:26,917 ERROR routersploit.exceptions       Unknown command: 'jobs'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_jobs'
2017-12-13 12:43:21,542 ERROR routersploit.exceptions       Unknown command: 'hrelep'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_hrelep'
2017-12-13 12:54:46,998 ERROR routersploit.exceptions       Unknown command: 'shell'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shell'
2017-12-13 12:54:51,933 ERROR routersploit.exceptions       Unknown command: 'shell('')'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shell('')'
2017-12-13 12:55:16,471 ERROR routersploit.exceptions       Unknown command: '-v'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_-v'
2017-12-13 12:55:18,348 ERROR routersploit.exceptions       Unknown command: 'version'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_version'
root@CRACK_COCAINE:~/Documents/routersploit# cat routersploit.log
2017-12-13 10:58:29,120 ERROR routersploit.exceptions       Error during loading 'routersploit/modules/scanners/autopwn'

Error: 'module' object has no attribute 'optionsParser'

It should be valid path to the module. Use <tab> key multiple times for completion.
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/utils/__init__.py", line 66, in import_exploit
 module = importlib.import_module(path)
File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
 __import__(name)
File "/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py", line 103, in <module>
 main()
File "/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py", line 92, in main
 parser = optparse.optionsParser('usage %parser -r <manual control> -a full auto')
AttributeError: 'module' object has no attribute 'optionsParser'
2017-12-13 10:59:03,109 ERROR routersploit.exceptions       Unknown command: 'options'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_options'
2017-12-13 10:59:45,547 ERROR routersploit.exceptions       Unknown command: 'shpw'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shpw'
2017-12-13 11:07:26,917 ERROR routersploit.exceptions       Unknown command: 'jobs'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_jobs'
2017-12-13 12:43:21,542 ERROR routersploit.exceptions       Unknown command: 'hrelep'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_hrelep'
2017-12-13 12:54:46,998 ERROR routersploit.exceptions       Unknown command: 'shell'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shell'
2017-12-13 12:54:51,933 ERROR routersploit.exceptions       Unknown command: 'shell('')'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_shell('')'
2017-12-13 12:55:16,471 ERROR routersploit.exceptions       Unknown command: '-v'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_-v'
2017-12-13 12:55:18,348 ERROR routersploit.exceptions       Unknown command: 'version'
Traceback (most recent call last):
File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
 command_handler = getattr(self, "command_{}".format(command))
AttributeError: 'RoutersploitInterpreter' object has no attribute 'command_version'
root@CRACK_COCAINE:~/Documents/routersploit# cat routersploit.log grep^C
root@CRACK_COCAINE:~/Documents/routersploit# egrep -irn command_handler * --color
routersploit/interpreter.py:66:    def get_command_handler(self, command):
routersploit/interpreter.py:70:        :return: command_handler
routersploit/interpreter.py:73:            command_handler = getattr(self, "command_{}".format(command))
routersploit/interpreter.py:77:        return command_handler
routersploit/interpreter.py:89:                command_handler = self.get_command_handler(command)
routersploit/interpreter.py:90:                command_handler(args)
Binary file routersploit/interpreter.pyc matches
routersploit.log:18:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:19:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:23:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:24:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:28:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:29:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:33:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:34:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:38:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:39:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:43:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:44:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:48:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:49:    command_handler = getattr(self, "command_{}".format(command))
routersploit.log:53:  File "/root/Documents/routersploit/routersploit/interpreter.py", line 73, in get_command_handler
routersploit.log:54:    command_handler = getattr(self, "command_{}".format(command))
root@CRACK_COCAINE:~/Documents/routersploit# cd routersploit
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# atom interpreter.py
root@CRACK_COCAINE:~/Documents/routersploit/routersploit# cd -
/root/Documents/routersploit
root@CRACK_COCAINE:~/Documents/routersploit# python
Python 2.7.14 (default, Sep 17 2017, 18:50:44)
[GCC 7.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import routersploit
>>> from routersploit import *
>>> import interpreter
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ImportError: No module named interpreter
>>> from routersploit import interpreter
>>> interpreter.get_command_handler(self, 'show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'get_command_handler'
>>> interpreter.get_command_handler(self, 'show')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'get_command_handler'
>>> interpreter.BaseInterpreter.get_command_handler(self, 'show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> interpreter.BaseInterpreter(self).get_command_handler(self, 'show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> interpreter.BaseInterpreter(object).get_command_handler(self, 'show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter(__init__).get_command_handler(self, 'show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__init__' is not defined
>>> interpreter.BaseInterpreter(object).get_command_handler(self, 'show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter(object).get_command_handler('show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter(object).get_command_handler('show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter(object).__init__
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> dir(interpreter.BaseInterpreter)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'commands', 'complete', 'default_completer', 'get_command_handler', 'global_help', 'history_file', 'history_length', 'parse_line', 'prompt', 'raw_command_completer', 'setup', 'start', 'suggested_commands']
>>> dir(interpreter.BaseInterpreter.commands)
['__call__', '__class__', '__cmp__', '__delattr__', '__doc__', '__format__', '__func__', '__get__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'im_class', 'im_func', 'im_self']
>>> dir(interpreter.BaseInterpreter.get_command_handler
... show payloads
File "<stdin>", line 2
 show payloads
    ^
SyntaxError: invalid syntax
>>> dir(interpreter.BaseInterpreter.get_command_handler('show payloads'))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method get_command_handler() must be called with BaseInterpreter instance as first argument (got str instance instead)
>>> BaseInterpreter()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> help(BaseInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> BaseInterpreter(__init__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> import BaseInterpreter
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ImportError: No module named BaseInterpreter
>>> import BaseInterpreter~
KeyboardInterrupt
>>> dir(BaseInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> dir(interpreter.BaseInterpreter)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'commands', 'complete', 'default_completer', 'get_command_handler', 'global_help', 'history_file', 'history_length', 'parse_line', 'prompt', 'raw_command_completer', 'setup', 'start', 'suggested_commands']
>>> dir(interpreter.suggeseted_commands)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'suggeseted_commands'
>>> dir(interpreter.suggeseted_commands)
KeyboardInterrupt
>>> vars
<built-in function vars>
>>> vars()
{'exploits': <module 'routersploit.exploits' from 'routersploit/exploits.pyc'>, 'mute': <function mute at 0x7fb92ad31398>, 'utils': <module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>, 'print_status': <function print_status at 0x7fb92ad315f0>, 'print_error': <function print_error at 0x7fb92ad31578>, 'printer': <module 'routersploit.printer' from 'routersploit/printer.pyc'>, 'validators': <module 'routersploit.validators' from 'routersploit/validators.pyc'>, 'interpreter': <module 'routersploit.interpreter' from 'routersploit/interpreter.pyc'>, 'print_table': <function print_table at 0x7fb92ad31b18>, 'sanitize_url': <function sanitize_url at 0x7fb92ad31b90>, 'wordlists': <module 'routersploit.wordlists' from 'routersploit/wordlists/__init__.pyc'>, '__package__': None, 'payloads': <module 'routersploit.payloads' from 'routersploit/payloads.pyc'>, 'tokenize': <function tokenize at 0x7fb92ad31f50>, '__doc__': None, 'http_request': <function http_request at 0x7fb92ad31cf8>, 'shell': <function shell at 0x7fb92accf398>, 'ssh_interactive': <function ssh_interactive at 0x7fb92ad31de8>, '__builtins__': <module '__builtin__' (built-in)>, 'boolify': <function boolify at 0x7fb92ad31d70>, 'LockedIterator': <class 'routersploit.utils.LockedIterator'>, 'multi': <function multi at 0x7fb92ad31488>, '__name__': '__main__', 'modules': <module 'routersploit.modules' from 'routersploit/modules/__init__.pyc'>, 'routersploit': <module 'routersploit' from 'routersploit/__init__.pyc'>, 'index_modules': <function index_modules at 0x7fb92ad15c80>, 'print_success': <function print_success at 0x7fb92ad31668>, 'print_info': <function print_info at 0x7fb92ad316e0>, 'exceptions': <module 'routersploit.exceptions' from 'routersploit/exceptions.pyc'>, 'random_text': <function random_text at 0x7fb92ad31c80>}
>>> dir(interpreter.prompt)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'prompt'
>>> help(interpreter.prompt)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'prompt'
>>> prompt
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'prompt' is not defined
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'tokenize', 'utils', 'validators', 'wordlists']
>>> dir(multi)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> dir(_call_)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_call_' is not defined
>>> dir(_globals_)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_globals_' is not defined
>>> globals
<built-in function globals>
>>> globals()
{'exploits': <module 'routersploit.exploits' from 'routersploit/exploits.pyc'>, 'mute': <function mute at 0x7fb92ad31398>, 'utils': <module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>, 'print_status': <function print_status at 0x7fb92ad315f0>, 'print_error': <function print_error at 0x7fb92ad31578>, 'printer': <module 'routersploit.printer' from 'routersploit/printer.pyc'>, 'validators': <module 'routersploit.validators' from 'routersploit/validators.pyc'>, 'interpreter': <module 'routersploit.interpreter' from 'routersploit/interpreter.pyc'>, 'print_table': <function print_table at 0x7fb92ad31b18>, 'sanitize_url': <function sanitize_url at 0x7fb92ad31b90>, 'wordlists': <module 'routersploit.wordlists' from 'routersploit/wordlists/__init__.pyc'>, '__package__': None, 'payloads': <module 'routersploit.payloads' from 'routersploit/payloads.pyc'>, 'tokenize': <function tokenize at 0x7fb92ad31f50>, '__doc__': None, 'http_request': <function http_request at 0x7fb92ad31cf8>, 'shell': <function shell at 0x7fb92accf398>, 'ssh_interactive': <function ssh_interactive at 0x7fb92ad31de8>, '__builtins__': <module '__builtin__' (built-in)>, 'boolify': <function boolify at 0x7fb92ad31d70>, 'LockedIterator': <class 'routersploit.utils.LockedIterator'>, 'multi': <function multi at 0x7fb92ad31488>, '__name__': '__main__', 'modules': <module 'routersploit.modules' from 'routersploit/modules/__init__.pyc'>, 'routersploit': <module 'routersploit' from 'routersploit/__init__.pyc'>, 'index_modules': <function index_modules at 0x7fb92ad15c80>, 'print_success': <function print_success at 0x7fb92ad31668>, 'print_info': <function print_info at 0x7fb92ad316e0>, 'exceptions': <module 'routersploit.exceptions' from 'routersploit/exceptions.pyc'>, 'random_text': <function random_text at 0x7fb92ad31c80>}
>>> exec
File "<stdin>", line 1
 exec
    ^
SyntaxError: invalid syntax
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'tokenize', 'utils', 'validators', 'wordlists']
>>> dir(interpreter)
['BaseInterpreter', 'BasePayload', 'Counter', 'Exploit', 'GLOBAL_OPTS', 'PrinterThread', 'RoutersploitException', 'RoutersploitInterpreter', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'atexit', 'itertools', 'os', 'print_function', 'printer_queue', 'readline', 'sys', 'traceback', 'utils']
>>> dir(itertools)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'itertools' is not defined
>>> dir(readline)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'readline' is not defined
>>> dir(sys)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'sys' is not defined
>>> dir(utils)
['ABCMeta', 'CREDS_DIR', 'DummyFile', 'EXPLOITS_DIR', 'LockedIterator', 'MODULES_DIR', 'NonStringIterable', 'PrintResource', 'Resource', 'RoutersploitException', 'SCANNERS_DIR', '__builtins__', '__cprint', '__doc__', '__file__', '__name__', '__package__', '__path__', 'absolute_import', 'abstractmethod', 'boolify', 'collections', 'colors', 'create_exploit', 'create_resource', 'errno', 'http_request', 'humanize_path', 'import_exploit', 'importlib', 'index_modules', 'iter_modules', 'mkdir_p', 'module_required', 'multi', 'mute', 'os', 'posix_shell', 'pprint_dict_in_order', 'print_error', 'print_function', 'print_info', 'print_lock', 'print_status', 'print_success', 'print_table', 'printer_queue', 'pythonize_path', 'random', 'random_text', 're', 'requests', 'rsf_modules', 'sanitize_url', 'select', 'socket', 'ssh_interactive', 'stop_after', 'string', 'strtobool', 'sys', 'thread_output_stream', 'threading', 'tokenize', 'windows_shell', 'wraps']
>>> dir(import_exploit)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'import_exploit' is not defined
>>> dir(ssh_interactive)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> dir(__dict__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> help(__dict__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> help(ssh_interactive.__dict__)

>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'tokenize', 'utils', 'validators', 'wordlists']
>>> dir(utils)
['ABCMeta', 'CREDS_DIR', 'DummyFile', 'EXPLOITS_DIR', 'LockedIterator', 'MODULES_DIR', 'NonStringIterable', 'PrintResource', 'Resource', 'RoutersploitException', 'SCANNERS_DIR', '__builtins__', '__cprint', '__doc__', '__file__', '__name__', '__package__', '__path__', 'absolute_import', 'abstractmethod', 'boolify', 'collections', 'colors', 'create_exploit', 'create_resource', 'errno', 'http_request', 'humanize_path', 'import_exploit', 'importlib', 'index_modules', 'iter_modules', 'mkdir_p', 'module_required', 'multi', 'mute', 'os', 'posix_shell', 'pprint_dict_in_order', 'print_error', 'print_function', 'print_info', 'print_lock', 'print_status', 'print_success', 'print_table', 'printer_queue', 'pythonize_path', 'random', 'random_text', 're', 'requests', 'rsf_modules', 'sanitize_url', 'select', 'socket', 'ssh_interactive', 'stop_after', 'string', 'strtobool', 'sys', 'thread_output_stream', 'threading', 'tokenize', 'windows_shell', 'wraps']
>>> import absolute_import
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ImportError: No module named absolute_import
>>> from routersploit import absolute_import
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ImportError: cannot import name absolute_import
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'tokenize', 'utils', 'validators', 'wordlists']
>>> dir(interpreter)
['BaseInterpreter', 'BasePayload', 'Counter', 'Exploit', 'GLOBAL_OPTS', 'PrinterThread', 'RoutersploitException', 'RoutersploitInterpreter', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'atexit', 'itertools', 'os', 'print_function', 'printer_queue', 'readline', 'sys', 'traceback', 'utils']
>>> dir(interpreter.command_run)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'command_run'
>>> dir(interpreter.command_run())
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'command_run'
>>> dir(interpreter.command_run('show'))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'command_run'
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'tokenize', 'utils', 'validators', 'wordlists']
>>> dir(modules)
['__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__']
>>> dir(index_modules)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> dir(utils)
['ABCMeta', 'CREDS_DIR', 'DummyFile', 'EXPLOITS_DIR', 'LockedIterator', 'MODULES_DIR', 'NonStringIterable', 'PrintResource', 'Resource', 'RoutersploitException', 'SCANNERS_DIR', '__builtins__', '__cprint', '__doc__', '__file__', '__name__', '__package__', '__path__', 'absolute_import', 'abstractmethod', 'boolify', 'collections', 'colors', 'create_exploit', 'create_resource', 'errno', 'http_request', 'humanize_path', 'import_exploit', 'importlib', 'index_modules', 'iter_modules', 'mkdir_p', 'module_required', 'multi', 'mute', 'os', 'posix_shell', 'pprint_dict_in_order', 'print_error', 'print_function', 'print_info', 'print_lock', 'print_status', 'print_success', 'print_table', 'printer_queue', 'pythonize_path', 'random', 'random_text', 're', 'requests', 'rsf_modules', 'sanitize_url', 'select', 'socket', 'ssh_interactive', 'stop_after', 'string', 'strtobool', 'sys', 'thread_output_stream', 'threading', 'tokenize', 'windows_shell', 'wraps']
>>> dir(pythonize)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'pythonize' is not defined
>>> dir(pythonize_path)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'pythonize_path' is not defined
>>> help(pythonize_path)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'pythonize_path' is not defined
>>> dir(pythonize_path)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'pythonize_path' is not defined
>>> posix_shell()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'posix_shell' is not defined
>>> help(posix_shell)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'posix_shell' is not defined
>>> help(import_exploit)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'import_exploit' is not defined
>>> help(__dict__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'tokenize', 'utils', 'validators', 'wordlists']
>>> dir(modules)
['__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__']
>>> dir(random_text)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> dir(utils)
['ABCMeta', 'CREDS_DIR', 'DummyFile', 'EXPLOITS_DIR', 'LockedIterator', 'MODULES_DIR', 'NonStringIterable', 'PrintResource', 'Resource', 'RoutersploitException', 'SCANNERS_DIR', '__builtins__', '__cprint', '__doc__', '__file__', '__name__', '__package__', '__path__', 'absolute_import', 'abstractmethod', 'boolify', 'collections', 'colors', 'create_exploit', 'create_resource', 'errno', 'http_request', 'humanize_path', 'import_exploit', 'importlib', 'index_modules', 'iter_modules', 'mkdir_p', 'module_required', 'multi', 'mute', 'os', 'posix_shell', 'pprint_dict_in_order', 'print_error', 'print_function', 'print_info', 'print_lock', 'print_status', 'print_success', 'print_table', 'printer_queue', 'pythonize_path', 'random', 'random_text', 're', 'requests', 'rsf_modules', 'sanitize_url', 'select', 'socket', 'ssh_interactive', 'stop_after', 'string', 'strtobool', 'sys', 'thread_output_stream', 'threading', 'tokenize', 'windows_shell', 'wraps']
>>> dir(create_exploit)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'create_exploit' is not defined
>>> help(create_exploit)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'create_exploit' is not defined
>>> help(humanize_path)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'humanize_path' is not defined
>>> dir(humanize_path)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'humanize_path' is not defined
>>> routersploit.utils.__init__
<method-wrapper '__init__' of module object at 0x7fb92ecd26a8>
>>> dir(routersploit.utils)
['ABCMeta', 'CREDS_DIR', 'DummyFile', 'EXPLOITS_DIR', 'LockedIterator', 'MODULES_DIR', 'NonStringIterable', 'PrintResource', 'Resource', 'RoutersploitException', 'SCANNERS_DIR', '__builtins__', '__cprint', '__doc__', '__file__', '__name__', '__package__', '__path__', 'absolute_import', 'abstractmethod', 'boolify', 'collections', 'colors', 'create_exploit', 'create_resource', 'errno', 'http_request', 'humanize_path', 'import_exploit', 'importlib', 'index_modules', 'iter_modules', 'mkdir_p', 'module_required', 'multi', 'mute', 'os', 'posix_shell', 'pprint_dict_in_order', 'print_error', 'print_function', 'print_info', 'print_lock', 'print_status', 'print_success', 'print_table', 'printer_queue', 'pythonize_path', 'random', 'random_text', 're', 'requests', 'rsf_modules', 'sanitize_url', 'select', 'socket', 'ssh_interactive', 'stop_after', 'string', 'strtobool', 'sys', 'thread_output_stream', 'threading', 'tokenize', 'windows_shell', 'wraps']
>>> help(string)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'string' is not defined
>>> vars()
{'exploits': <module 'routersploit.exploits' from 'routersploit/exploits.pyc'>, 'mute': <function mute at 0x7fb92ad31398>, 'utils': <module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>, 'print_status': <function print_status at 0x7fb92ad315f0>, 'print_error': <function print_error at 0x7fb92ad31578>, 'printer': <module 'routersploit.printer' from 'routersploit/printer.pyc'>, 'validators': <module 'routersploit.validators' from 'routersploit/validators.pyc'>, 'interpreter': <module 'routersploit.interpreter' from 'routersploit/interpreter.pyc'>, 'print_table': <function print_table at 0x7fb92ad31b18>, 'sanitize_url': <function sanitize_url at 0x7fb92ad31b90>, 'wordlists': <module 'routersploit.wordlists' from 'routersploit/wordlists/__init__.pyc'>, '__package__': None, 'payloads': <module 'routersploit.payloads' from 'routersploit/payloads.pyc'>, 'tokenize': <function tokenize at 0x7fb92ad31f50>, '__doc__': None, 'http_request': <function http_request at 0x7fb92ad31cf8>, 'shell': <function shell at 0x7fb92accf398>, 'ssh_interactive': <function ssh_interactive at 0x7fb92ad31de8>, '__builtins__': <module '__builtin__' (built-in)>, 'boolify': <function boolify at 0x7fb92ad31d70>, 'LockedIterator': <class 'routersploit.utils.LockedIterator'>, 'multi': <function multi at 0x7fb92ad31488>, '__name__': '__main__', 'modules': <module 'routersploit.modules' from 'routersploit/modules/__init__.pyc'>, 'routersploit': <module 'routersploit' from 'routersploit/__init__.pyc'>, 'index_modules': <function index_modules at 0x7fb92ad15c80>, 'print_success': <function print_success at 0x7fb92ad31668>, 'print_info': <function print_info at 0x7fb92ad316e0>, 'exceptions': <module 'routersploit.exceptions' from 'routersploit/exceptions.pyc'>, 'random_text': <function random_text at 0x7fb92ad31c80>}
>>> command = "show"
>>> command = "show payloads"
>>> interpreter.get_command_handler(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'get_command_handler'
>>> interpreter.start.get_command_handler(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'start'
>>> interpreter.BaseInterpreter.start.get_command_handler(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'get_command_handler'
>>> interpreter.BaseInterpreter(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter()
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ace76d0>
>>> print 0x7fb92ace76d0
140433263851216
>>> test = interpreter.BaseInterpreter(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> test = interpreter.BaseInterpreter()
>>> print test
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ace7710>
>>> test = interpreter.BaseInterpreter(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> test = interpreter.BaseInterpreter()
>>> command = use scanners/autopwn
File "<stdin>", line 1
 command = use scanners/autopwn
                      ^
SyntaxError: invalid syntax
>>> command = "use scanners/autopwn"
>>> test = interpreter.BaseInterpreter()
>>> interpreter.BaseInterpreter()
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ac99790>
>>> print

>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'wordlists']
>>> printer
<module 'routersploit.printer' from 'routersploit/printer.pyc'>
>>> test = printer
>>> print test
<module 'routersploit.printer' from 'routersploit/printer.pyc'>
>>> command = "run"
>>> interpreter.BaseInterpreter()
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ac90690>
>>> print_error
<function print_error at 0x7fb92ad31578>
>>> print command
run
>>> print_info
<function print_info at 0x7fb92ad316e0>
>>> print_status
<function print_status at 0x7fb92ad315f0>
>>> print_success
<function print_success at 0x7fb92ad31668>
>>> help(__builtins__)

>>> __getattribute__
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__getattribute__' is not defined
>>> __getattribute__(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__getattribute__' is not defined
>>> __getattribute__(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__getattribute__' is not defined
>>> help(__builtins__)

>>> dict
<type 'dict'>
>>> dict
<type 'dict'>
>>> dict command
File "<stdin>", line 1
 dict command
            ^
SyntaxError: invalid syntax
>>> doct get_command
File "<stdin>", line 1
 doct get_command
                ^
SyntaxError: invalid syntax
>>> doct get_command()
File "<stdin>", line 1
 doct get_command()
                ^
SyntaxError: invalid syntax
>>> locals()
{'exploits': <module 'routersploit.exploits' from 'routersploit/exploits.pyc'>, 'mute': <function mute at 0x7fb92ad31398>, 'utils': <module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>, 'print_status': <function print_status at 0x7fb92ad315f0>, 'print_error': <function print_error at 0x7fb92ad31578>, 'printer': <module 'routersploit.printer' from 'routersploit/printer.pyc'>, 'validators': <module 'routersploit.validators' from 'routersploit/validators.pyc'>, 'interpreter': <module 'routersploit.interpreter' from 'routersploit/interpreter.pyc'>, 'print_table': <function print_table at 0x7fb92ad31b18>, 'sanitize_url': <function sanitize_url at 0x7fb92ad31b90>, 'wordlists': <module 'routersploit.wordlists' from 'routersploit/wordlists/__init__.pyc'>, '__package__': None, 'payloads': <module 'routersploit.payloads' from 'routersploit/payloads.pyc'>, 'tokenize': <function tokenize at 0x7fb92ad31f50>, 'test': <module 'routersploit.printer' from 'routersploit/printer.pyc'>, 'command': 'run', '__doc__': None, 'http_request': <function http_request at 0x7fb92ad31cf8>, 'shell': <function shell at 0x7fb92accf398>, 'ssh_interactive': <function ssh_interactive at 0x7fb92ad31de8>, '__builtins__': <module '__builtin__' (built-in)>, 'boolify': <function boolify at 0x7fb92ad31d70>, 'LockedIterator': <class 'routersploit.utils.LockedIterator'>, 'multi': <function multi at 0x7fb92ad31488>, '__name__': '__main__', 'modules': <module 'routersploit.modules' from 'routersploit/modules/__init__.pyc'>, 'routersploit': <module 'routersploit' from 'routersploit/__init__.pyc'>, 'index_modules': <function index_modules at 0x7fb92ad15c80>, 'print_success': <function print_success at 0x7fb92ad31668>, 'print_info': <function print_info at 0x7fb92ad316e0>, 'exceptions': <module 'routersploit.exceptions' from 'routersploit/exceptions.pyc'>, 'random_text': <function random_text at 0x7fb92ad31c80>}
>>> BaseInterpreter(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> interpreter.BaseInterpreter(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter()
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ac99790>
>>> command = "exit"
>>> interpreter.BaseInterpreter()
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ac90690>
>>> help(__doc__)

>>> list
<type 'list'>
>>> list __builtins__
File "<stdin>", line 1
 list __builtins__
                 ^
SyntaxError: invalid syntax
>>> list main
File "<stdin>", line 1
 list main
         ^
SyntaxError: invalid syntax
>>> list command
File "<stdin>", line 1
 list command
            ^
SyntaxError: invalid syntax
>>> list(print_status)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'function' object is not iterable
>>> list(wordlists)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not iterable
>>> list(modules)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not iterable
>>> help(list)

>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'wordlists']
>>> help(command)

>>> command(__dict__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> dict(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> __dict__(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> help(command)

>>> help(command)
KeyboardInterrupt
>>> command(__weakref__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__weakref__' is not defined
>>> help(command)

>>> call(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'call' is not defined
>>> command(call)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'call' is not defined
>>> command(__call__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__call__' is not defined
>>> command.call('show payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'call'
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'wordlists']
>>> interpreter.dir()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'dir'
>>> get.command.call
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'get' is not defined
>>> get_command.call
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'get_command' is not defined
>>> interpreter.get_command.call
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'get_command'
>>> interpreter.BaseInterpreter()
<routersploit.interpreter.BaseInterpreter object at 0x7fb92ac76510>
>>> interpreter.BaseInterpreter(dir)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter.setup()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method setup() must be called with BaseInterpreter instance as first argument (got nothing instead)
>>> interpreter.BaseInterpreter.parse_line.call("show payloads")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'call'
>>> interpreter.BaseInterpreter.parse_line("show payloads")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method parse_line() must be called with BaseInterpreter instance as first argument (got str instance instead)
>>> interpreter.BaseInterpreter("show payloads")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.BaseInterpreter(__init__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__init__' is not defined
>>> interpreter.BaseInterpreter.__init__
<unbound method BaseInterpreter.__init__>
>>> interpreter.BaseInterpreter.__init__."show payloads"
File "<stdin>", line 1
 interpreter.BaseInterpreter.__init__."show payloads"
                                                    ^
SyntaxError: invalid syntax
>>> interpreter.BaseInterpreter.__init__.show
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'show'
>>> interpreter.BaseInterpreter.__init__.parse_line
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'parse_line'
>>> interpreter.BaseInterpreter.parse_line
<unbound method BaseInterpreter.parse_line>
>>> interpreter.BaseInterpreter.parse_line(self,"showpayloads")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> interpreter.BaseInterpreter.get_command_handler('show')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method get_command_handler() must be called with BaseInterpreter instance as first argument (got str instance instead)
>>> interpreter.BaseInterpreter(get_command_handler('show'))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'get_command_handler' is not defined
>>> interpreter.BaseInterpreter().parse_line(self,"showpayloads")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> interpreter.BaseInterpreter().parse_line(self,"showpayloads")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> interpreter.BaseInterpreter().parse_line("showpayloads")
('showpayloads', '')
>>> interpreter.BaseInterpreter().parse_line("show payloads")
('show', 'payloads')
>>> interpreter.BaseInterpreter().parse_line("use scanners/autopwn")
('use', 'scanners/autopwn')
>>> interpreter.BaseInterpreter().parse_line("set target 192.168.1.1")
('set', 'target 192.168.1.1')
>>> interpreter.BaseInterpreter().parse_line("set target 192.168.1.1")
('set', 'target 192.168.1.1')
>>> interpreter.BaseInterpreter().parse_line("run")
('run', '')
>>> interpreter.BaseInterpreter().parse_line("show target")
('show', 'target')
>>> interpreter.BaseInterpreter().parse_line("0v")
('0v', '')
>>> interpreter.BaseInterpreter().parse_line("-v")
('-v', '')
>>> interpreter.BaseInterpreter().parse_line("exec uname")
('exec', 'uname')
>>> interpreter.BaseInterpreter().parse_line("ssh -p 666 root@70.170.54.53")
('ssh', '-p 666 root@70.170.54.53')
>>> complete_command.call
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'complete_command' is not defined
>>> complete(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'complete' is not defined
>>> complete(command,0)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'complete' is not defined
>>> complete('show',0)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'complete' is not defined
>>> interpreter.BaseInterpreter().parse_line("ssh -p 666 root@70.170.54.53")
('ssh', '-p 666 root@70.170.54.53')
>>> print command
exit
>>> print history_file
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'history_file' is not defined
>>> print RoutersploitInterpreter.history_file
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> print RoutersploitInterpreter().history_file
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> print RoutersploitInterpreter(BaseInterpreter).history_file
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> print interpreter.RoutersploitInterpreter(BaseInterpreter).history_file
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> print interpreter.RoutersploitInterpreter().history_file
/root/.rsf_history
>>> run
KeyboardInterrupt
>>> RoutersploitInterpreter()._parse_prompt('show all')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> RoutersploitInterpreter().command_use('scanners/autopwn')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> RoutersploitInterpreter().BaseInterpreter().command_use('scanners/autopwn')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> interpreter.BaseInterpreter().command_use('scanners/autopwn')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'BaseInterpreter' object has no attribute 'command_use'
>>> utils.command_use('scanners/autopwn')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'command_use'
>>> utils.stop.after.command_use('scanners/autopwn')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'stop'
>>> utils.stop_after.command_use('scanners/autopwn')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'command_use'
>>> interpreter.BaseInterpreter()._show_all()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'BaseInterpreter' object has no attribute '_show_all'
>>> interpreter.BaseInterpreter()._show_modules()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'BaseInterpreter' object has no attribute '_show_modules'
>>> interpreter.utils._show_modules()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '_show_modules'
>>> interpreter.utils.module_required._show_modules()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_modules'
>>> interpreter.utils.module_required()._show_modules()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: module_required() takes exactly 1 argument (0 given)
>>> interpreter.utils.module_required()._show_modules('root')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: module_required() takes exactly 1 argument (0 given)
>>> interpreter.utils.module_required()._show_modules('')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: module_required() takes exactly 1 argument (0 given)
>>> interpreter.utils.module_required()._show_modules(' ')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: module_required() takes exactly 1 argument (0 given)
>>> interpreter.utils.__show_modules('scanners')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '__show_modules'
>>> interpreter.utils().__show_modules('scanners')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> interpreter.__show_modules('scanners')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '__show_modules'
>>> interpreter.@utils.module_required.__show_modules('scanners')
File "<stdin>", line 1
 interpreter.@utils.module_required.__show_modules('scanners')
             ^
SyntaxError: invalid syntax
>>> interpreter.utils.module_required.__show_modules('scanners')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '__show_modules'
>>> interpreter.utils.module_required.__show_modules('scanners'
...
...
...
KeyboardInterrupt
>>> var = interpreter.utils.module_required.__show_modules('scanners'
...
KeyboardInterrupt
>>> var = interpreter.utils.module_required.__show_modules('scanners')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '__show_modules'
>>> self.__show_modules('scanners')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> _show_scanners()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_show_scanners' is not defined
>>> interpreter._show_scanners()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '_show_scanners'
>>> interpreter.utils._show_scanners()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '_show_scanners'
>>> interpreter.utils.print_info_show_scanners()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'print_info_show_scanners'
>>> interpreter.utils.print_info._show_scanners()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_scanners'
>>> _show_scanners(self, *args, **kwargs):
File "<stdin>", line 1
 _show_scanners(self, *args, **kwargs):
                                      ^
SyntaxError: invalid syntax
>>>         self.__show_modules('scanners')
File "<stdin>", line 1
 self.__show_modules('scanners')
 ^
IndentationError: unexpected indent
>>> _show_scanners(self)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_show_scanners' is not defined
>>> _show_scanners(self,,)
File "<stdin>", line 1
 _show_scanners(self,,)
                     ^
SyntaxError: invalid syntax
>>> _show_scanners(self,'','')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_show_scanners' is not defined
>>> utils.module_required._show_devices
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_devices'
>>> utils.module_required._show_devices()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_devices'
>>> utils.module_required._show_devices(services)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_devices'
>>> utils.module_required._show_devices('devices')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_devices'
>>> interpreter.utils.module_required._show_devices('devices')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute '_show_devices'
>>> /root/Documents/routersploit/routersploit/interpreter.pyinterpreter.utils.module_required._show_devices('devices')
KeyboardInterrupt
>>> RoutersploitInterpreter.available_modules_completion('payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> BaseInterpreter.available_modules_completion('payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> interpreter.available_modules_completion('payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'available_modules_completion'
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'wordlists']
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help>

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help(__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__' is not defined
>>> help(_init__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '_init__' is not defined
>>> BaseInterpreter.available_modules_completion('payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> RoutersploitInterpreter(BaseInterpreter).available_modules_completion('payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> RoutersploitInterpreter('payloads')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> help(RoutersploitInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> dir(RoutersploitInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> /root/Documents/routersploit/routersploit/interpreter.py
KeyboardInterrupt
>>> help(BaseInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> dir(BaseInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'BaseInterpreter' is not defined
>>> dir(interpreter)
['BaseInterpreter', 'BasePayload', 'Counter', 'Exploit', 'GLOBAL_OPTS', 'PrinterThread', 'RoutersploitException', 'RoutersploitInterpreter', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'atexit', 'itertools', 'os', 'print_function', 'printer_queue', 'readline', 'sys', 'traceback', 'utils']
>>> help(interpreter.RoutersploitInterpreter)

>>> interpreter.RoutersploitInterpreter.start()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method start() must be called with RoutersploitInterpreter instance as first argument (got nothing instead)
>>> interpreter.RoutersploitInterpreter.start('show')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method start() must be called with RoutersploitInterpreter instance as first argument (got str instance instead)
>>> interpreter.RoutersploitInterpreter(start)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'start' is not defined
>>> RoutersploitInterpreter(start)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> help(RoutersploitInterpreter)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> RoutersploitInterpreter.start
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> RoutersploitInterpreter().start
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> RoutersploitInterpreter().start.()
File "<stdin>", line 1
 RoutersploitInterpreter().start.()
                                 ^
SyntaxError: invalid syntax
>>> RoutersploitInterpreter.start.()
File "<stdin>", line 1
 RoutersploitInterpreter.start.()
                               ^
SyntaxError: invalid syntax
>>> RoutersploitInterpreter(BaseInterpreter).start.()
File "<stdin>", line 1
 RoutersploitInterpreter(BaseInterpreter).start.()
                                                ^
SyntaxError: invalid syntax
>>> global_help
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'global_help' is not defined
>>> RoutersploitInterpreterglobal_help
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreterglobal_help' is not defined
>>> RoutersploitInterpreter.global_help
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'RoutersploitInterpreter' is not defined
>>> interpreter.RoutersploitInterpreter.global_help
'Global commands:\n    help                        Print this help menu\n    use <module>                Select a module for usage\n    exec <shell command> <args> Execute a command in a shell\n    search <search term>        Search for appropriate module\n    exit                        Exit RouterSploit'
>>> interpreter.RoutersploitInterpreter.search payloads
File "<stdin>", line 1
 interpreter.RoutersploitInterpreter.search payloads
                                                   ^
SyntaxError: invalid syntax
>>> interpreter.RoutersploitInterpreter.search
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: type object 'RoutersploitInterpreter' has no attribute 'search'
>>> interpreter.RoutersploitInterpreter.show
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: type object 'RoutersploitInterpreter' has no attribute 'show'
>>> interpreter.RoutersploitInterpreter.use scanners/autopwn
File "<stdin>", line 1
 interpreter.RoutersploitInterpreter.use scanners/autopwn
                                                ^
SyntaxError: invalid syntax
>>> interpreter.RoutersploitInterpreter.use
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: type object 'RoutersploitInterpreter' has no attribute 'use'
>>> interpreter.RoutersploitInterpreter.global_help use
File "<stdin>", line 1
 interpreter.RoutersploitInterpreter.global_help use
                                                   ^
SyntaxError: invalid syntax
>>> interpreter.RoutersploitInterpreter.commands()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method commands() must be called with RoutersploitInterpreter instance as first argument (got nothing instead)
>>> interpreter.RoutersploitInterpreter.commands(self)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> interpreter.RoutersploitInterpreter(commands)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'commands' is not defined
>>> interpreter.RoutersploitInterpreter('commands')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>> interpreter.RoutersploitInterpreter()
<routersploit.interpreter.RoutersploitInterpreter object at 0x7fb92ac80250>
>>> interpreter.BaseInterpreter.commands()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method commands() must be called with BaseInterpreter instance as first argument (got nothing instead)
>>> interpreter.BaseInterpreter(commands)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'commands' is not defined
>>> interpreter.BaseInterpreter(commands.())
File "<stdin>", line 1
 interpreter.BaseInterpreter(commands.())
                                      ^
SyntaxError: invalid syntax
>>> interpreter.BaseInterpreter('commands')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 1 argument (2 given)
>>>
>>> interpreter.BaseInterpreter.init('commands')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: type object 'BaseInterpreter' has no attribute 'init'
>>> interpreter.BaseInterpreter.__init__('commands')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method __init__() must be called with BaseInterpreter instance as first argument (got str instance instead)
>>>
>>> interpreter.BaseInterpreter.commands()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method commands() must be called with BaseInterpreter instance as first argument (got nothing instead)
>>> interpreter.BaseInterpreter.commands
<unbound method BaseInterpreter.commands>
>>> interpreter.BaseInterpreter.commands
<unbound method BaseInterpreter.commands>
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> var = interpreter.BaseInterpreter.commands
>>> print var
<unbound method BaseInterpreter.commands>
>>> var = interpreter.BaseInterpreter(self).commands
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> var = interpreter.BaseInterpreter(self).commands(self)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> var = interpreter.BaseInterpreter(self).commands()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> var = interpreter.BaseInterpreter().commands()
>>> var = interpreter.BaseInterpreter().commands()
>>> print var
[]
>>> uname
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'uname' is not defined
>>> interpreter.BaseInterpreter.commands
<unbound method BaseInterpreter.commands>
>>> interpreter.BaseInterpreter.commands()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unbound method commands() must be called with BaseInterpreter instance as first argument (got nothing instead)
>>> interpreter.BaseInterpreter().commands()
[]
>>> interpreter.RoutersploitInterpreter().commands()
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> interpreter.RoutersploitInterpreter().commands('sudo su')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> interpreter.RoutersploitInterpreter().commands('show payloads')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> interpreter.RoutersploitInterpreter().commands('use scanners/autopwn')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> interpreter.RoutersploitInterpreter().commands('set target 192.168.1.1')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> interpreter.RoutersploitInterpreter().commands('set port 80')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> run
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'run' is not defined
>>> interpreter.RoutersploitInterpreter().commands('run')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> interpreter.RoutersploitInterpreter().commands('help')
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']
>>> license
Type license() to see the full license text
>>> license()
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit:
releases have also been GPL-compatible; the table below summarizes
the various releases.

 Release         Derived     Year        Owner       GPL-
                 from                                compatible? (1)

 0.9.0 thru 1.2              1991-1995   CWI         yes
 1.3 thru 1.5.2  1.2         1995-1999   CNRI        yes
 1.6             1.5.2       2000        CNRI        no
 2.0             1.6         2000        BeOpen.com  no
 1.6.1           1.6         2001        CNRI        yes (2)
 2.1             2.0+1.6.1   2001        PSF         no
 2.0.1           2.0+1.6.1   2001        PSF         yes
 2.1.1           2.1+2.0.1   2001        PSF         yes
 2.1.2           2.1.1       2002        PSF         yes
 2.1.3           2.1.2       2002        PSF         yes
 2.2 and above   2.1.1       2001-now    PSF         yes

Footnotes:

(1) GPL-compatible doesn't mean that we're distributing Python under
 the GPL.  All Python licenses, unlike the GPL, let you distribute
 a modified version without making your changes open source.  The
Hit Return for more, or q (and Return) to quit:
 GPL-compatible licenses make it possible to combine Python with
 other software that is released under the GPL; the others don't.

(2) According to Richard Stallman, 1.6.1 is not GPL-compatible,
 because its license has a choice of law clause.  According to
 CNRI, however, Stallman's lawyer has told CNRI's lawyer that 1.6.1
 is "not incompatible" with the GPL.

Thanks to the many outside volunteers who have worked under Guido's
direction to make these releases possible.


B. TERMS AND CONDITIONS FOR ACCESSING OR OTHERWISE USING PYTHON
===============================================================

PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
--------------------------------------------

1. This LICENSE AGREEMENT is between the Python Software Foundation
("PSF"), and the Individual or Organization ("Licensee") accessing and
otherwise using this software ("Python") in source or binary form and
its associated documentation.

Hit Return for more, or q (and Return) to quit:
2. Subject to the terms and conditions of this License Agreement, PSF hereby
grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
analyze, test, perform and/or display publicly, prepare derivative works,
distribute, and otherwise use Python alone or in any derivative version,
provided, however, that PSF's License Agreement and PSF's notice of copyright,
i.e., "Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
2011, 2012, 2013, 2014, 2015, 2016, 2017 Python Software Foundation; All Rights
Reserved" are retained in Python alone or in any derivative version prepared by
Licensee.

3. In the event Licensee prepares a derivative work that is based on
or incorporates Python or any part thereof, and wants to make
the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to Python.

4. PSF is making Python available to Licensee on an "AS IS"
basis.  PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

Hit Return for more, or q (and Return) to quit:
5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON
FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS
A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON,
OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between PSF and
Licensee.  This License Agreement does not grant permission to use PSF
trademarks or trade name in a trademark sense to endorse or promote
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using Python, Licensee
agrees to be bound by the terms and conditions of this License
Agreement.


BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0
-------------------------------------------

BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1
Hit Return for more, or q (and Return) to quit:

1. This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an
office at 160 Saratoga Avenue, Santa Clara, CA 95051, and the
Individual or Organization ("Licensee") accessing and otherwise using
this software in source or binary form and its associated
documentation ("the Software").

2. Subject to the terms and conditions of this BeOpen Python License
Agreement, BeOpen hereby grants Licensee a non-exclusive,
royalty-free, world-wide license to reproduce, analyze, test, perform
and/or display publicly, prepare derivative works, distribute, and
otherwise use the Software alone or in any derivative version,
provided, however, that the BeOpen Python License is retained in the
Software, alone or in any derivative version prepared by Licensee.

3. BeOpen is making the Software available to Licensee on an "AS IS"
basis.  BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

4. BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE
Hit Return for more, or q (and Return) to quit: q
>>> dir(class)
File "<stdin>", line 1
 dir(class)
         ^
SyntaxError: invalid syntax
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'var', 'wordlists']
>>> help(command)

>>> help(command)

>>> help(command(__dict__))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> __dict__(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__dict__' is not defined
>>> dict(command)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> interpreter
<module 'routersploit.interpreter' from 'routersploit/interpreter.pyc'>
>>> printer interpreter
File "<stdin>", line 1
 printer interpreter
                   ^
SyntaxError: invalid syntax
>>> modules
<module 'routersploit.modules' from 'routersploit/modules/__init__.pyc'>
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'var', 'wordlists']
>>> utils
<module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>
>>> ()
()
>>> routersploit.utils
<module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>
>>> routersploit.utils()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> multi()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: multi() takes exactly 1 argument (0 given)
>>> multi.()
File "<stdin>", line 1
 multi.()
       ^
SyntaxError: invalid syntax
>>> multi(self)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> dir(multi)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> globals(multi)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: globals() takes no arguments (1 given)
>>> vars(multi))
File "<stdin>", line 1
 vars(multi))
            ^
SyntaxError: invalid syntax
>>> vars(multi)
{}
>>> __class__(multi))
File "<stdin>", line 1
 __class__(multi))
                 ^
SyntaxError: invalid syntax
>>> __list__(multi)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__list__' is not defined
>>> help(multi)

>>> __getattribute__(__hash__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__getattribute__' is not defined
>>> help(__hash__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__hash__' is not defined
>>> print(hash)
<built-in function hash>
>>> hash.()
File "<stdin>", line 1
 hash.()
      ^
SyntaxError: invalid syntax
>>> hash()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: hash() takes exactly one argument (0 given)
>>> hash(self)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> dir()
['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'var', 'wordlists']
>>> validators()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> validators(dir)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> dir(validators)
['OptionValidationError', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'address', 'boolify', 'choice', 'convert_ip', 'convert_port', 'integer', 'ipv4', 'socket', 'strtobool', 'url', 'urlparse']
>>> exceptions()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> modules()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> modules.()
File "<stdin>", line 1
 modules.()
         ^
SyntaxError: invalid syntax
>>> module()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'module' is not defined
>>> index_modules()
['exploits.routers.cisco.ucs_manager_rce', 'exploits.routers.cisco.video_surv_path_traversal', 'exploits.routers.cisco.ios_http_authorization_bypass', 'exploits.routers.cisco.catalyst_2960_rocem', 'exploits.routers.cisco.unified_multi_path_traversal', 'exploits.routers.cisco.firepower_management60_path_traversal', 'exploits.routers.cisco.dpc2420_info_disclosure', 'exploits.routers.cisco.secure_acs_bypass', 'exploits.routers.cisco.firepower_management60_rce', 'exploits.routers.cisco.ucm_info_disclosure', 'exploits.routers.huawei.e5331_mifi_info_disclosure', 'exploits.routers.huawei.hg530_hg520b_password_disclosure', 'exploits.routers.huawei.hg630a_default_creds', 'exploits.routers.huawei.hg866_password_change', 'exploits.routers.huawei.hg520_info_dislosure', 'exploits.routers.multi.heartbleed', 'exploits.routers.multi.misfortune_cookie', 'exploits.routers.multi.shellshock', 'exploits.routers.multi.tcp_32764_rce', 'exploits.routers.multi.tcp_32764_info_disclosure', 'exploits.routers.multi.rom0', 'exploits.routers.multi.ssh_auth_keys', 'exploits.routers.2wire.4011g_5012nv_path_traversal', 'exploits.routers.2wire.gateway_auth_bypass', 'exploits.routers.juniper.screenos_backdoor', 'exploits.routers.tplink.archer_c2_c20i_rce', 'exploits.routers.tplink.wdr740nd_wdr740n_path_traversal', 'exploits.routers.tplink.wdr740nd_wdr740n_backdoor', 'exploits.routers.tplink.wdr842nd_wdr842n_configure_disclosure', 'exploits.routers.netgear.multi_rce', 'exploits.routers.netgear.r7000_r6400_rce', 'exploits.routers.netgear.wnr500_612v3_jnr1010_2010_path_traversal', 'exploits.routers.netgear.n300_auth_bypass', 'exploits.routers.netgear.multi_password_disclosure-2017-5521', 'exploits.routers.netgear.prosafe_rce', 'exploits.routers.netgear.jnr1010_path_traversal', 'exploits.routers.netgear.dgn2200_dnslookup_cgi_rce', 'exploits.routers.netgear.dgn2200_ping_cgi_rce', 'exploits.routers.linksys.1500_2500_rce', 'exploits.routers.linksys.smartwifi_password_disclosure', 'exploits.routers.linksys.wap54gv3_rce', 'exploits.routers.linksys.wrt100_110_rce', 'exploits.routers.fortinet.fortigate_os_backdoor', 'exploits.routers.asus.infosvr_backdoor_rce', 'exploits.routers.asus.rt_n16_password_disclosure', 'exploits.routers.ipfire.ipfire_proxy_rce', 'exploits.routers.ipfire.ipfire_shellshock', 'exploits.routers.belkin.g_plus_info_disclosure', 'exploits.routers.belkin.g_n150_password_disclosure', 'exploits.routers.belkin.play_max_prce', 'exploits.routers.belkin.n150_path_traversal', 'exploits.routers.belkin.n750_rce', 'exploits.routers.belkin.auth_bypass', 'exploits.routers.bhu.bhu_urouter_rce', 'exploits.routers.dlink.dir_825_path_traversal', 'exploits.routers.dlink.dir_645_password_disclosure', 'exploits.routers.dlink.dir_300_320_600_615_info_disclosure', 'exploits.routers.dlink.dir_645_815_rce', 'exploits.routers.dlink.dsl_2640b_dns_change', 'exploits.routers.dlink.dsl_2730b_2780b_526b_dns_change', 'exploits.routers.dlink.dwr_932_info_disclosure', 'exploits.routers.dlink.dvg_n5402sp_path_traversal', 'exploits.routers.dlink.dsp_w110_rce', 'exploits.routers.dlink.dsl_2730_2750_path_traversal', 'exploits.routers.dlink.dir_300_320_615_auth_bypass', 'exploits.routers.dlink.dcs_930l_auth_rce', 'exploits.routers.dlink.dwl_3200ap_password_disclosure', 'exploits.routers.dlink.dsl_2740r_dns_change', 'exploits.routers.dlink.dwr_932b_backdoor', 'exploits.routers.dlink.dir_300_645_815_upnp_rce', 'exploits.routers.dlink.multi_hedwig_cgi_exec', 'exploits.routers.dlink.dir_815_850l_rce', 'exploits.routers.dlink.dgs_1510_add_user', 'exploits.routers.dlink.multi_hnap_rce', 'exploits.routers.dlink.dir_300_600_rce', 'exploits.routers.dlink.dns_320l_327l_rce', 'exploits.routers.dlink.dsl_2750b_info_disclosure', 'exploits.routers.3com.officeconnect_rce', 'exploits.routers.3com.imc_info_disclosure', 'exploits.routers.3com.3cradsl72_info_disclosure', 'exploits.routers.3com.officeconnect_info_disclosure', 'exploits.routers.3com.ap8760_password_disclosure', 'exploits.routers.3com.imc_path_traversal', 'exploits.routers.netsys.multi_rce', 'exploits.routers.netcore.udp_53413_rce', 'exploits.routers.thomson.twg849_info_disclosure', 'exploits.routers.thomson.twg850_password_disclosure', 'exploits.routers.billion.5200w_rce', 'exploits.routers.billion.7700nr4_password_disclosure', 'exploits.routers.movistar.adsl_router_bhs_rta_path_traversal', 'exploits.routers.zyxel.p660hn-t_v1_rce', 'exploits.routers.zyxel.p660hn-t_v2_rce', 'exploits.routers.zyxel.d1000_rce', 'exploits.routers.zyxel.d1000_wifi_password_disclosure', 'exploits.routers.zyxel.zywall_usg_extract_hashes', 'exploits.routers.ubiquiti.airos_6_x', 'exploits.routers.comtrend.ct_5361t_password_disclosure', 'exploits.routers.asmax.ar_1004g_password_disclosure', 'exploits.routers.asmax.ar_804_gu_rce', 'exploits.routers.technicolor.tg784_authbypass', 'exploits.routers.technicolor.tc7200_password_disclosure', 'exploits.routers.technicolor.dwg855_authbypass', 'exploits.routers.technicolor.tc7200_password_disclosure_v2', 'exploits.routers.zte.f660_config_disclosure', 'exploits.routers.zte.zxv10_rce', 'exploits.routers.zte.f609_config_disclosure', 'exploits.routers.zte.f460_f660_backdoor', 'exploits.routers.zte.f6xx_default_root', 'exploits.routers.shuttle.915wm_dns_change', 'exploits.cameras.videoiq.videoiq_camera_path_traversal', 'exploits.cameras.multi.netwave_IP_camera', 'exploits.cameras.multi.jvc_vanderbilt_honeywell_path_traversal', 'exploits.cameras.multi.P2P_wificam_rce', 'exploits.cameras.multi.P2P_wificam_credential_disclosure', 'exploits.cameras.honeywell.hicc_1100pt_password_disclosure', 'exploits.cameras.dlink.dcs_930l_932l_auth_bypass', 'exploits.cameras.brickcom.corp_network_cameras_conf_disclosure', 'exploits.cameras.brickcom.users_cgi_cred_disclosure', 'exploits.cameras.grandstream.gxv3611hd_ip_camera_rce', 'exploits.cameras.siemens.CVMS2025_credentials_disclosure', 'exploits.misc.asus.b1m_projector_rce', 'exploits.misc.miele.pg8528_path_traversal', 'exploits.misc.wepresent.wipg1000_rce', 'payloads.mipsbe.reverse_tcp', 'payloads.mipsbe.bind_tcp', 'payloads.generic.netcat_reverse_tcp', 'payloads.generic.awk_bind_tcp', 'payloads.generic.awk_reverse_tcp', 'payloads.generic.netcat_bind_tcp', 'payloads.mipsle.reverse_tcp', 'payloads.mipsle.bind_tcp', 'payloads.armle.reverse_tcp', 'payloads.armle.bind_tcp', 'scanners.netgear_scan', 'scanners.cisco_scan', 'scanners.cameras_scan', 'scanners.asus_scan', 'scanners.technicolor_scan', 'scanners.linksys_scan', 'scanners.3com_scan', 'scanners.zte_scan', 'scanners.zyxel_scan', 'scanners.misc_scan', 'scanners.autopwn', 'scanners.movistar_scan', 'scanners.multi_scan', 'scanners.2wire_scan', 'scanners.grandstream_scan', 'scanners.shuttle_scan', 'scanners.netsys_scan', 'scanners.tplink_scan', 'scanners.comtrend_scan', 'scanners.routers_scan', 'scanners.thomson_scan', 'scanners.asmax_scan', 'scanners.ubiquiti_scan', 'scanners.belkin_scan', 'scanners.juniper_scan', 'scanners.netcore_scan', 'scanners.billion_scan', 'scanners.fortinet_scan', 'scanners.bhu_scan', 'scanners.ipfire_scan', 'scanners.dlink_scan', 'scanners.huawei_scan', 'creds.ftp_default', 'creds.http_basic_bruteforce', 'creds.ssh_default', 'creds.telnet_bruteforce', 'creds.ftp_bruteforce', 'creds.http_digest_default', 'creds.telnet_default', 'creds.snmp_bruteforce', 'creds.http_form_default', 'creds.http_form_bruteforce', 'creds.ssh_bruteforce', 'creds.http_digest_bruteforce', 'creds.http_basic_default']
>>>

>>>

 """
