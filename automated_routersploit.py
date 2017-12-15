import os
import sys
import argv
import socket
import threading
import subprocess
import time
import subprocess
import time
import operator
import os
import socket
import sys
from termcolor import colored
sys.path.append('/root/ArmsCommander')
import toolkits
import optparse
from sys import argv

#These are just my notes. my code is way fdown there at the bottom.

#Its a bit complex but its doable to directly control routersploit via a hands-free fast-flowing terminal session. All the console does is parse your optoions into the right arguments and commands.

# there is quite a bit of importing going on, but with this list of functions, its even more straightforward since we just have to pass our arguments into their arguments.



def bash_command(cmd):
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    return

cmd_to_pull_gateway_ip = "route -n egrep -i "{}" awk '{print $2}' grep -v 0.0.0.0"""
routersploit_installation = "/root/Documents/routersploit"
RSF_shell_call_location = "interpreter.RoutersploitInterpreter()
subdirectory = ""
os.chdir(routersploit_installation)
cmd_GET_RSF_command = "interpreter.RoutersploitInterpreter().commands()"
str(module_path) = "scanners/autopwn"
RSF_shell_architecture = "interpreter.RoutersploitInterpreter().commands()"
interpreter()
#

def RSF_interpreter_shell(routersploit_installation,RSF_shell_call_location,str(module_path),str(argsv_1),str(opt_argsv_2)):
import routersploit
from routersploit import *
from routersploit.modules import *
import __builtin__
import __builtins__
from routersploit import shell
from routersploit import interpreter
from __builtin__ import *
import __future__
from __future__import import *

    CMD_init_all = """
routersploit.__init__
shell.__init__
ssh_interactive.__init__
routersploit.utils.__init__
routersploit.modules.__init__
multi.__init__
index_modules.__init__
help(shell)
__call__
, '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'http_request': <function http_request at 0x7fb791b2ecf8>, 'EOFError': <type 'exceptions.EOFError'>, 'str': <type 'str'>, 'sorted': <built-in function sorted>, '__builtins__': <module '__builtin__' (built-in)>, 'basestring': <type 'basestring'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__main__', 'ord': <built-in function ord>, 'super': <type 'super'>, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'routersploit': <module 'routersploit' from 'routersploit/__init__.pyc'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'print_success': <function print_success at 0x7fb791b2e668>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, '__builtin__': <module '__builtin__' (built-in)>, 'StopIteration': <type 'exceptions.StopIteration'>, 'print_error': <function print_error at 0x7fb791b2e578>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'Ellipsis': Ellipsis, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'wordlists': <module 'routersploit.wordlists' from 'routersploit/wordlists/__init__.pyc'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'int': <type 'int'>, 'chr': <built-in function chr>, 'tokenize': <function tokenize at 0x7fb791b2ef50>, 'type': <type 'type'>, '__doc__': None, 'print_status': <function print_status at 0x7fb791b2e5f0>, 'shell': <function shell at 0x7fb791acd398>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'KeyError': <type 'exceptions.KeyError'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'multi': <function multi at 0x7fb791b2e488>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'print_info': <function print_info at 0x7fb791b2e6e0>, 'exceptions': <module 'routersploit.exceptions' from 'routersploit/exceptions.pyc'>, 'property': <type 'property'>, 'random_text': <function random_text at 0x7fb791b2ec80>, 'MemoryError': <type 'exceptions.MemoryError'>, 'ImportError': <type 'exceptions.ImportError'>, 'xrange': <type 'xrange'>, 'utils': <module 'routersploit.utils' from 'routersploit/utils/__init__.pyc'>, 'Exception': <type 'exceptions.Exception'>, 'coerce': <built-in function coerce>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, '__package__': None, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'payloads': <module 'routersploit.payloads' from 'routersploit/payloads.pyc'>, 'BufferError': <type 'exceptions.BufferError'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'printer': <module 'routersploit.printer' from 'routersploit/printer.pyc'>, 'ssh_interactive': <function ssh_interactive at 0x7fb791b2ede8>, 'any': <built-in function any>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, 'boolify': <function boolify at 0x7fb791b2ed70>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'modules': <module 'routersploit.modules' from 'routersploit/modules/__init__.pyc'>, 'print_table': <function print_table at 0x7fb791b2eb18>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}
>>> ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
>>> dir()
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LockedIterator', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__builtin__', '__builtins__', '__doc__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'boolify', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exceptions', 'execfile', 'exit', 'exploits', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'http_request', 'id', 'index_modules', 'input', 'int', 'intern', 'interpreter', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'modules', 'multi', 'mute', 'next', 'object', 'oct', 'open', 'ord', 'payloads', 'pow', 'print', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'property', 'quit', 'random_text', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'routersploit', 'sanitize_url', 'set', 'setattr', 'shell', 'slice', 'sorted', 'ssh_interactive', 'staticmethod', 'str', 'sum', 'super', 'tokenize', 'tuple', 'type', 'unichr', 'unicode', 'utils', 'validators', 'vars', 'wordlists', 'xrange', 'zip']
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']

 "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> dir(validators)
['OptionValidationError', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'address', 'boolify', 'choice', 'convert_ip', 'convert_port', 'integer', 'ipv4', 'socket', 'strtobool', 'url', 'urlparse']
"""

Initialization of third-party libraries

        Setting interpreter history.
        Setting appropriate completer function.

        :return:

    def parse_line(self, line):
        """ Split line into command and argument.

        :param line: line to parse
        :return: (command, argument)
        """
        command, _, arg = line.strip().partition(" ")
        return command, arg.strip()

    @property
    def prompt(self):
        """ Returns prompt string """
        return ">>>"

    def get_command_handler(self, command):
        """ Parsing command and returning appropriate handler.

        :param command: command
        :return: command_handler
        """
        try:
            command_handler = getattr(self, "command_{}".format(command))
        except AttributeError:
            raise RoutersploitException("Unknown command: '{}'".format(command))

        return command_handler

    def start(self):
        """ Routersploit main entry point. Starting interpreter loop. """

        utils.print_info(self.banner)
        printer_queue.join()
        while True:
            try:
                command, args = self.parse_line(raw_input(self.prompt))
                if not command:
                    continue
                command_handler = self.get_command_handler(command)
                command_handler(args)
            except RoutersploitException as err:
                utils.print_error(err)
            except EOFError:
                utils.print_info()
                utils.print_status("routersploit stopped")
                break
            except KeyboardInterrupt:
                utils.print_info()
            finally:
                printer_queue.join()

    def complete(self, text, state):
        """Return the next possible completion for 'text'.

        If a command has not been entered, then complete against command list.
        Otherwise try to call complete_<command> to get list of completions.
        """
        if state == 0:
            original_line = readline.get_line_buffer()
            line = original_line.lstrip()
            stripped = len(original_line) - len(line)
            start_index = readline.get_begidx() - stripped
            end_index = readline.get_endidx() - stripped

            if start_index > 0:
                cmd, args = self.parse_line(line)
                if cmd == '':
                    complete_function = self.default_completer
                else:
                    try:
                        complete_function = getattr(self, 'complete_' + cmd)
                    except AttributeError:
                        complete_function = self.default_completer
            else:
                complete_function = self.raw_command_completer

            self.completion_matches = complete_function(text, line, start_index, end_index)

        try:
            return self.completion_matches[state]
        except IndexError:
            return None

    def commands(self, *ignored):
        """ Returns full list of interpreter commands.

        :param ignored:
        :return: full list of interpreter commands
        """
        return [command.rsplit("_").pop() for command in dir(self) if command.startswith("command_")]

    def raw_command_completer(self, text, line, start_index, end_index):
        """ Complete command w/o any argument """
        return filter(lambda entry: entry.startswith(text), self.suggested_commands())

    def default_completer(self, *ignored):
        return []

    def suggested_commands(self):
        """ Entry point for intelligent tab completion.

        Overwrite this method to suggest suitable commands.

        :return: list of suitable commands
        """
        return self.commands()


class RoutersploitInterpreter(BaseInterpreter):
    history_file = os.path.expanduser("~/.rsf_history")
    global_help = """Global commands:
    help                        Print this help menu
    use <module>                Select a module for usage
    exec <shell command> <args> Execute a command in a shell
    search <search term>        Search for appropriate module
    exit                        Exit RouterSploit"""

odule commands:
    run                                 Run the selected module with the given options
    back                                De-select the current module
    set <option name> <option value>    Set an option for the selected module
    setg <option name> <option value>   Set an option for all of the modules
    unsetg <option name>                Unset option that was set globally
    show [info|options|devices]         Print information, options, or target devices for a module
    check                               Check if a given target is vulnerable to a selected module's exploit"""

    def __init__(self):
        super(RoutersploitInterpreter, self).__init__()
        PrinterThread().start()

        self.current_module = None
        self.raw_prompt_template = None
        self.module_prompt_template = None
        self.prompt_hostname = 'rsf'
        self.show_sub_commands = (
            'info', 'options', 'devices', 'all',
            'creds', 'exploits', 'scanners'
        )

        self.global_commands = sorted(
            ['use ', 'exec ', 'help', 'exit', 'show ', 'search ']
        )
        self.module_commands = self._extend_with_global_commands(
            ['run', 'back', 'set ', 'setg ', 'check']
        )
        self.payload_commands = self._extend_with_global_commands(
            ['run', 'back', 'set ', 'setg ']
        )

        self.modules = utils.index_modules()
        self.modules_count = Counter()
        [self.modules_count.update(module.split('.')) for module in self.modules]
        self.main_modules_dirs = [module for module in os.listdir(utils.MODULES_DIR) if not module.startswith("__")]

        self.__parse_prompt()

        self.banner = """ ______            _            _____       _       _ _
 | ___ \          | |          /  ___|     | |     (_) |
 | |_/ /___  _   _| |_ ___ _ __\ `--. _ __ | | ___  _| |_
 |    // _ \| | | | __/ _ \ '__|`--. \ '_ \| |/ _ \| | __|
 | |\ \ (_) | |_| | ||  __/ |  /\__/ / |_) | | (_) | | |_
 \_| \_\___/ \__,_|\__\___|_|  \____/| .__/|_|\___/|_|\__|
                                     | |
        IoT Exploitation Framework   |_|

 Dev Team : Marcin Bury (lucyoa) & Mariusz Kupidura (fwkz)
 Codename : Bad Blood
 Version  : 2.2.1

 Exploits: {exploits_count} Scanners: {scanners_count} Creds: {creds_count} Payloads: {payloads_count}
""".format(exploits_count=self.modules_count['exploits'],
           scanners_count=self.modules_count['scanners'],
           creds_count=self.modules_count['creds'],
           payloads_count=self.modules_count['payloads'])

    def __parse_prompt(self):
        raw_prompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 > "
        raw_prompt_template = os.getenv("RSF_RAW_PROMPT", raw_prompt_default_template).replace('\\033', '\033')
        self.raw_prompt_template = raw_prompt_template if '{host}' in raw_prompt_template else raw_prompt_default_template

        module_prompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 (\001\033[91m\002{module}\001\033[0m\002) > "
        module_prompt_template = os.getenv("RSF_MODULE_PROMPT", module_prompt_default_template).replace('\\033', '\033')
        self.module_prompt_template = module_prompt_template if all(map(lambda x: x in module_prompt_template, ['{host}', "{module}"])) else module_prompt_default_template

    def _extend_with_global_commands(self, sequence):
        """ Extend specific command suggestion with global commands """
        sequence.extend(self.global_commands)
        sequence.sort()
        return sequence

    @property
    def module_metadata(self):
        return getattr(self.current_module, "_{}__info__".format(self.current_module.__class__.__name__))

    @property
    def prompt(self):
        """ Returns prompt string based on current_module attribute.

        Adding module prefix (module.name) if current_module attribute is set.

        :return: prompt string with appropriate module prefix.
        """
        if self.current_module:
            try:
                return self.module_prompt_template.format(host=self.prompt_hostname, module=self.module_metadata['name'])
            except (AttributeError, KeyError):
                return self.module_prompt_template.format(host=self.prompt_hostname, module="UnnamedModule")
        else:
            return self.raw_prompt_template.format(host=self.prompt_hostname)

    def available_modules_completion(self, text):
        """ Looking for tab completion hints using setup.py entry_points.

        May need optimization in the future!

        :param text: argument of 'use' command
        :return: list of tab completion hints
        """
        text = utils.pythonize_path(text)
        all_possible_matches = filter(lambda x: x.startswith(text), self.modules)
        matches = set()
        for match in all_possible_matches:
            head, sep, tail = match[len(text):].partition('.')
            if not tail:
                sep = ""
            matches.add("".join((text, head, sep)))
        return list(map(utils.humanize_path, matches))  # humanize output, replace dots to forward slashes

    def suggested_commands(self):
        """ Entry point for intelligent tab completion.

        Based on state of interpreter this method will return intelligent suggestions.

        :return: list of most accurate command suggestions
        """
        if self.current_module and GLOBAL_OPTS:
            return sorted(itertools.chain(self.module_commands, ('unsetg ',)))
        elif self.current_module and isinstance(self.current_module, Exploit):
            return self.module_commands
        elif self.current_module and isinstance(self.current_module,
                                                BasePayload):
            return self.payload_commands
        elif self.current_module:
            return self.module_commands
        else:
            return self.global_commands

    def command_back(self, *args, **kwargs):
        self.current_module = None

    def command_use(self, module_path, *args, **kwargs):
        module_path = utils.pythonize_path(module_path)
        module_path = '.'.join(('routersploit', 'modules', module_path))
        # module_path, _, exploit_name = module_path.rpartition('.')
        try:
            self.current_module = utils.import_exploit(module_path)()
        except RoutersploitException as err:
            utils.print_error(err.message)

    @utils.stop_after(2)
    def complete_use(self, text, *args, **kwargs):
        if text:
            return self.available_modules_completion(text)
        else:
            return self.main_modules_dirs

    @utils.module_required
    def command_run(self, *args, **kwargs):
        utils.print_status("Running module...")
        try:
            self.current_module.run()
        except KeyboardInterrupt:
            utils.print_info()
            utils.print_error("Operation cancelled by user")
        except Exception:
            utils.print_error(traceback.format_exc(sys.exc_info()))

    def command_exploit(self, *args, **kwargs):
        self.command_run()

    @utils.module_required
    def command_set(self, *args, **kwargs):
        key, _, value = args[0].partition(' ')
        if key in self.current_module.options:
            setattr(self.current_module, key, value)
            if kwargs.get("glob", False):
                GLOBAL_OPTS[key] = value
            utils.print_success({key: value})
        else:
            utils.print_error("You can't set option '{}'.\n"
                              "Available options: {}".format(key, self.current_module.options))

    @utils.stop_after(2)
    def complete_set(self, text, *args, **kwargs):
        if text:
            return [' '.join((attr, "")) for attr in self.current_module.options if attr.startswith(text)]
        else:
            return self.current_module.options

    @utils.module_required
    def command_setg(self, *args, **kwargs):
        kwargs['glob'] = True
        self.command_set(*args, **kwargs)

    @utils.stop_after(2)
    def complete_setg(self, text, *args, **kwargs):
        return self.complete_set(text, *args, **kwargs)

    @utils.module_required
    def command_unsetg(self, *args, **kwargs):
        key, _, value = args[0].partition(' ')
        try:
            del GLOBAL_OPTS[key]
        except KeyError:
            utils.print_error("You can't unset global option '{}'.\n"
                              "Available global options: {}".format(key, GLOBAL_OPTS.keys()))
        else:
            utils.print_success({key: value})

    @utils.stop_after(2)
    def complete_unsetg(self, text, *args, **kwargs):
        if text:
            return [' '.join((attr, "")) for attr in GLOBAL_OPTS.keys() if attr.startswith(text)]
        else:
            return GLOBAL_OPTS.keys()

    @utils.module_required
    def get_opts(self, *args):
        """ Generator returning module's Option attributes (option_name, option_value, option_description)

        :param args: Option names
        :return:
        """
        for opt_key in args:
            try:
                opt_description = self.current_module.exploit_attributes[opt_key]
                opt_value = getattr(self.current_module, opt_key)
            except (KeyError, AttributeError):
                pass
            else:
                yield opt_key, opt_value, opt_description

    @utils.module_required
    def _show_info(self, *args, **kwargs):
        utils.pprint_dict_in_order(
            self.module_metadata,
            ("name", "description", "devices", "authors", "references"),
        )
        utils.print_info()

    @utils.module_required
    def _show_options(self, *args, **kwargs):
        target_opts = ['target', 'port', 'rhost', 'rport', 'lhost', 'lport']
        module_opts = [opt for opt in self.current_module.options if opt not in target_opts]
        headers = ("Name", "Current settings", "Description")

        utils.print_info('\nTarget options:')
        utils.print_table(headers, *self.get_opts(*target_opts))

        if module_opts:
            utils.print_info('\nModule options:')
            utils.print_table(headers, *self.get_opts(*module_opts))

        utils.print_info()

    @utils.module_required
    def _show_devices(self, *args, **kwargs):  # TODO: cover with tests
        try:
            devices = self.current_module._Exploit__info__['devices']

            utils.print_info("\nTarget devices:")
            i = 0
            for device in devices:
                if isinstance(device, dict):
                    utils.print_info("   {} - {}".format(i, device['name']))
                else:
                    utils.print_info("   {} - {}".format(i, device))
                i += 1
            utils.print_info()
        except KeyError:
            utils.print_info("\nTarget devices are not defined")

    def __show_modules(self, root=''):
        for module in [module for module in self.modules if module.startswith(root)]:
            utils.print_info(module.replace('.', os.sep))

    def _show_all(self, *args, **kwargs):
        self.__show_modules()

    def _show_scanners(self, *args, **kwargs):
        self.__show_modules('scanners')

    def _show_exploits(self, *args, **kwargs):
        self.__show_modules('exploits')

    def _show_creds(self, *args, **kwargs):
        self.__show_modules('creds')

    def command_show(self, *args, **kwargs):
        sub_command = args[0]
        try:
            getattr(self, "_show_{}".format(sub_command))(*args, **kwargs)
        except AttributeError:
            utils.print_error("Unknown 'show' sub-command '{}'. "
                              "What do you want to show?\n"
                              "Possible choices are: {}".format(sub_command, self.show_sub_commands))

    @utils.stop_after(2)
    def complete_show(self, text, *args, **kwargs):
        if text:
            return [command for command in self.show_sub_commands if command.startswith(text)]
        else:
            return self.show_sub_commands

    @utils.module_required
    def command_check(self, *args, **kwargs):
        try:
            result = self.current_module.check()
        except Exception as error:
            utils.print_error(error)
        else:
            if result is True:
                utils.print_success("Target is vulnerable")
            elif result is False:
                utils.print_error("Target is not vulnerable")
            else:
                utils.print_status("Target could not be verified")

    def command_help(self, *args, **kwargs):
        utils.print_info(self.global_help)
        if self.current_module:
            utils.print_info("\n", self.module_help)

    def command_exec(self, *args, **kwargs):
        os.system(args[0])

    def command_search(self, *args, **kwargs):
        keyword = args[0]

        if not keyword:
            utils.print_error("Please specify search keyword. e.g. 'search cisco'")
            return

        for module in self.modules:
            if keyword in module:
                module = utils.humanize_path(module)
                utils.print_info(
                    "{}\033[31m{}\033[0m{}".format(*module.partition(keyword))
                )

    def command_exit(self, *args, **kwargs):
        raise EOFError

    bash_command(CMD_init_all)

    # this function is not meant to be directly touched. It's meant to pass arugment variables to the itnerpreter easy-mode.
    BasicInterpreter_Commands = "interpreter.BaseInterpreter().commands()"
    RSF_interpreter_LIST_CMDS = "interpreter.RoutersploitInterpreter().commands()"

    RSF_machine_commands_list = ['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']


# >>> interpreter.BaseInterpreter.commands()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unbound method commands() must be called with BaseInterpreter instance as first argument (got nothing instead)
# >>> interpreter.BaseInterpreter().commands()
# []
# >>> interpreter.RoutersploitInterpreter().commands()
# ['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']


    bash_command(RSF_interpreter_LIST_CMDS)
    RSF_interpreter_SHOW_HIST = "interpreter.RoutersploitInterpreter().commands(){}.history_file()."
        str(RSF_shell_call_location)))
    RSF_interpreter_MODULE_HELP = "interpreter.RoutersploitInterpreter().commands(){}.module_help({1}str(RSF_shell_call_location))
    if str(opt_argsv_2) == 0 or None or '':
        str(opt_argsv_2) = None
    else:
        pass

    if str(argsv_1) == 0 or None or '':
        str(argsv_1) = None
    else:
        pass


def routersploit_interpreter():

    return

def routersploit_ssh_interactive():
    return
def screen_make_detach_session(processname):

    bash_command("screen -dmS %s" % str(processname))
    return bash_command

def screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session(process_name, process_number, subproc_name, cmd_exec):



    cmd = "Interpreter.RoutersploitInterpreter().commands({},{},{})".format((str(module_path),str(argsv_1),str(opt_argsv_2)))
    bash_command(cmd)
    return bash_command

def subproc_popen(cmd):
    sub_p = subprocess.Popen(cmd,shell=True,stdin=stdout,executable='/bin/bash')
    value = sub_p.communicate()
    value = str(value).strip()

    return value
def autorouter(target_router_ip):

    # remember that we already enumerated target IPs far during the beginning of the script.
    screen_make_detach_session('netdiscover')
    subnet_list = []

    subnet = target_router_ip.split('.')
        first_octet = subnet[0]
        second_octet = subnet[1]
        third_octet = subnet[2]
        fourth_octet = 0

    subnet = "interpreter.RoutersploitInterpreter().commands()%d.%d.%d.%d" % (int(first_octet), int(second_octet), int(third_octet), int(fourth_octet))
    subnet = str(subnet)

    subnet_list.append(subnet)

    gateway = str(target_router_ip)
    netmask = "interpreter.RoutersploitInterpreter().commands()255.255.255.0"
    route_to_net = str(subnet)
    BASH_netdiscover = "interpreter.RoutersploitInterpreter().commands()netdiscover grep *.*.*.* > ./new_ips.log"
    BASH_auto_route = "interpreter.RoutersploitInterpreter().commands()route -add net str(RSF_shell_call_location) netmask {1} gw {2} {3}({1}, {2})(
        str(route_to_net),
        str(netmask),
        str(gateway)
    )
    BASH_arp_a = "interpreter.RoutersploitInterpreter().commands()arp -a"
    GREP_parse_new_Ips = "interpreter.RoutersploitInterpreter().commands()"
    screen_make_detach_session('netdiscover')
    screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('netdiscover',0,'bash_cmd',BASH_netdiscover)

    BASH_read_discovered_nets = "interpreter.RoutersploitInterpreter().commands()cat ./net_ips.log grep *.*.*.* sort uniq strings"
    discovered_nets = subproc_popen(BASH_read_discovered_nets)

    discovered_nets = discovered_nets.split('\n')
    for item in discovered_nets:
        network = str(item)
        subnet = discovered_nets.split('.')
        for subnet in discovered_nets:
            first_octet = subnet[0]
            second_octet = subnet[1]
            third_octet = subnet[2]
            fourth_octet = 0
            subnet_list.append(str(subnet))

    for item in subnet_list:
        subnet = item
        route_to_net = str(subnet).strip()
        gateway = str(target_router_ip).strip()
        netmask = str("255.255.255.0")

        screen_make_detach_session('autorouter')
        screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('autorouter',0,'bash_cmd',BASH_auto_route)
        screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('autorouter',0,'bash_cmd','route -n > new_routes.txt;ifconfig -a > new_routes.txt,nbtscan 0.0.0.0 > new_routes.txt')

    for item in subnet_list:
        target_net = str(item)
        start_routersploit(target_net)
        metasploit(target_net)
        nmap_directory_traversal(target_net)

    return subnet_list

def packet_sniffers():
    net_interface = "interpreter.RoutersploitInterpreter().commands()wlan1"

    MSF_psnuffle = "interpreter.RoutersploitInterpreter().commands()"
    MSF_resource_script = "interpreter.RoutersploitInterpreter().commands()./MSF_resource_script.rc"
    MSF_resource_script_content = "interpreter.RoutersploitInterpreter().commands()""
    # socks4a server

    # pnuffle

    # nbt spoofer

    # common exploits
    ""({1}, {2})(

    )

    w = open(MSF_resource_script,'w+')
    w.write(MSF_resource_script_content)
    w.close()

    MSF_resource_script = bash_command("ls $PWD/str(RSF_shell_call_location)").format(
        str(MSF_resource_script)
    )

    MSF_resource_script = str(MSF_resource_script)
    MSF_workspace = "interpreter.RoutersploitInterpreter().commands()"
    MSF_exec_RSF_command = "interpreter.RoutersploitInterpreter().commands()_set_global WORKSPACE str(RSF_shell_call_location);workspace str(RSF_shell_call_location);resource {1}({1}, {2})(
        str(workspace),
        str(MSF_resource_script)
    )
    GIT_netcreds = "interpreter.RoutersploitInterpreter().commands()"
    BASH_tcpdump = "interpreter.RoutersploitInterpreter().commands()"
    return
def metasploit():

    # init and launch
    # make a workspace

    # arpsweep

    # ping sweep

    # self infection

    # netbios
    # # connect scan
    # class Option(__builtin__.object)
    #   Exploit attribute that is set by the end user.
    #
    #   Methods defined here:
    #
    #   __get__"(self, instance, owner)
    #
    #   __init__"(self, default, description='', validators=())
    #
    #   __set__"(self, instance, value)
    #


    # syn scan

    # db_export into xml
    return
def nmap_directory_traversal():

    script_list = "interpreter.RoutersploitInterpreter().commands()""http-enum.nse"""

    cmd_nmap_FIN = "interpreter.RoutersploitInterpreter().commands()"
    cmd_nmap_XMAS = "interpreter.RoutersploitInterpreter().commands()"
    cmd_nmap_COMPREHENSIVE = "interpreter.RoutersploitInterpreter().commands()"

    # nmap must be optimized for speed and efficiency and not power, otherwise it'll quickly run doqwn the laptop's battery.

    start_metasploit()
    return



def start routersploit():
    routersploit_installation = "/root/Documents/routersploit"
    # subdirectory = "interpreter.RoutersploitInterpreter().commands()/root/Documents/routersploit/routersploit/modules/scanners/autopwn.py"
    import optparse
    from sys import argv
    import os
    import operator
    import sys
    import routersploit
    from routersploit import *
    import __builtin__

    from os import path
    from routersploit import (
        exploits,
        print_error,
        print_success,
        print_status,
        print_info,
        utils,
        threads,
    )


    # we need to make sure that the proper python libraries are loaded. the autopwn scanner looks relatively simple, it's actually it's back-end that does the work, not the pretty front end that were c0ontributed by the open source community.

    # we are gonna start up our services in the background far before anyone noticed


    screen_make_detach_session('rsf')
    screen_RSF_command = "interpreter.RoutersploitInterpreter({},{},{})".rundetached_session(str('module_path'),str(argsv_1),str(opt_argsv_2),RSF_set_target)
    bash_command(screen_RSF_command)


    # 1. Main thread, the direct engagement
    # 2. Recon thread, would be all of the stuff running in  the autorouter function and automatically find IPs and route networks
    # 3. Routersploit thread attemepts to autonomously run exploits and dump the creds
    # 4. nmap ThreadPoolExecutor
    # 5. ncrack thread
    # 6. metasploit crack
    ### official routersploit autopwn source code
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
        # directly attack router with routersploit
        target_router_ip = str(target_router_ip)
        target_port = str(target_port)

### this is my tool's side. Which will secretly start up routersploit services to make sure they are ready to go ###
        RSF_set_target = "interpreter.RoutersploitInterpreter().commands()set target %s" % str(target_router_ip)
        screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn',str(RSF_set_target))

        If the targeting parameters fail to change from nothing because of a technical issue then it will redset itself to standard parametersself.

        if target_router_ip or target_port == 0 or '' or None:
            target_threads = str(8)
            target_ip = str(192.168.1.1)
            target_port = str(80)
        else:
            pass

        for item in target_port_list_http:
            target_port = item
            RSF_set_port = "interpreter.RoutersploitInterpreter().commands()set port %s" % str(target_port)
            screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn',str(RSF_set_port))
            screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn','run')
            time.sleep(60)

        target_ip = str("")
        target_port = str("")
        target threads = 8


        screen_make_detach_session('rsf')
        screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn',RSF_set_target)
        target_port_list_http = [
            '80',
            '443',
            '81',
            '8080',
            '22',
            '23',
            '445',
            '139',
            '25'

        ]

        target_port_front_page_list = [
            'index.asp', 'index.html', 'login.html','admin.html','home.html'.'styles.css','script.js','script.php'
        ]

        # directly attack router with routersploit

        RSF_set_target = "interpreter.RoutersploitInterpreter().commands()set target %s" % str(target_router_ip)
        screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn',str(RSF_set_target))
        for item in target_port_list_http:
            target_port = item
            RSF_set_port = "interpreter.RoutersploitInterpreter().commands()set port %s" % str(target_port)
            screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn',str(RSF_set_port))
            screen_RSF_command = "interpreter.RoutersploitInterpreter().rundetached_session('rsf',0,'autopwn','run')
            time.sleep(60)



        target_ip = str(192.168.1.1)
        target_port = str(80)
        target_threads = str(8)

        target = exploits.Option(target_ip, 'Target IP address e.g. 192.168.1.1')  # target address
        port = exploits.Option(target_port, 'Target port')  # default port
        threads = exploits.Option(target_threads, "Number of threads")
        def __init__"(self):
            self.vulnerabilities = []
            self.not_verified = []
            self._exploits_directories = [path.join(utils.EXPLOITS_DIR, module) for module in self.modules]

        def run"(self):
            self.vulnerabilities = []
            self.not_verified = []

            with threads.ThreadPoolExecutor"(self.threads) as executor:
                for directory in self._exploits_directories:
                    for exploit in utils.iter_modules(directory):
                        executor.submit"(self.target_function, exploit)

            print_info()
            if self.not_verified:
                print_status("Could not verify exploitability:")
                for v in self.not_verified:
                    print_info(" - {}({1}, {2})(v))

            print_info()
            if self.vulnerabilities:
                print_success("Device is vulnerable:")
                for v in self.vulnerabilities:
                    print_info(" - {}({1}, {2})(v))
                print_info()
            else:
                print_error("Could not confirm any vulnerablity\n")

        def check"(self):
            raise NotImplementedError("Check method is not available")

        def target_function(self, exploit):
            exploit = exploit()
            exploit.target = self.target
            exploit.port = self.port

            response = exploit.check()

            if response is True:
                print_success((("{} is vulnerable({1}, {2})(exploit))
                self.vulnerabilities.append(exploit)
            elif response is False:
                print_error("{} is not vulnerable({1}, {2})(exploit))
            else:
                print_status("{} could not be verified({1}, {2})(exploit))
                self.not_verified.append(exploit)

                ### END OF OFFICIAL ROUTERSPLOIT CODE ###


    screen_make_detach_session('rsf')
    screen_RSF_command = "interpreter.RoutersploitInterpreter()".rundetached_session('rsf',0,'autopwn',RSF_set_target)
    target_port_list_http = [
        '80',
        '443',
        '81',
        '8080',
        '22',
        '23',
        '445',
        '139',
        '25'
        ]

    target_port_front_page_list = [
        'index.asp', 'index.html', 'login.html','admin.html'
    ]

    # directly attack router with routersploit

    RSF_set_target = "interpreter.RoutersploitInterpreter().commands()set target %s" % str(target_router_ip)
    screen_RSF_command = "interpreter.RoutersploitInterpreter()".rundetached_session('rsf',0,'autopwn',str(RSF_set_target))
    for item in target_port_list_http:
        target_port = item
        RSF_set_port = "interpreter.RoutersploitInterpreter().commands()set port %s" % str(target_port)
        screen_RSF_command = "interpreter.RoutersploitInterpreter()".rundetached_session('rsf',0,'autopwn',str(RSF_set_port))
        screen_RSF_command = "interpreter.RoutersploitInterpreter()".rundetached_session('rsf',0,'autopwn','run')
        time.sleep(60)


    RSF_set_module = "interpreter.RoutersploitInterpreter().commands()".format(
        str(

        )
    )
    cmd_curl_pull_page = "interpreter.RoutersploitInterpreter()".commands().curl -O % str(possible_url)
    cmd_GET_RSF_command = "interpreter.RoutersploitInterpreter()".commands()GET %s % str(possible_url)

    for item in target_port_list_http:
        target_port = item
        for url in target_port_front_page_list:
            possible_url = "interpreter.RoutersploitInterpreter().commands()"
            cmd = "interpreter.RoutersploitInterpreter().commands()" % str(possible_url)
            bash_RSF_command = (cmd)
            cmd = "interpreter.RoutersploitInterpreter().commands()%s %s" % (str(cmd_curl_pull_page), str(possible_url))


    # in case nothing gets done, attempt direectory traversal.

    nmap_directory_traversal()


    return
def power_on(cmd_to_pull_gateway_ip, routersploit_installation):
    time.sleep(30)

    bootup_cmds = "interpreter.RoutersploitInterpreter().commands()
    macchanger -b -r wlan1
    sleep 10; ifconfig -a >> /root/Desktop/network_config.log
    netdiscover > /root/Desktop/netdiscover.log
    "
    target_router_ip = bash_command(cmd_to_pull_gateway_ip)
    target_router_ip = str(target_router_ip)

    return
power_on()
target_router_ip = bash_command(cmd_to_pull_gateway_ip)
