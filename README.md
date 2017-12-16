<html>

# The move towards Daemonization

Dear loyal users of LULLC products such as ArmsCommander and Cylon-Raider. Be sure to anticipate a major update coming soon when our research completes. Currently the results that we have reviewed over in our various penetration testing projects point to that...

#	**We need to make better use of *nix daemons. Particularly, the service-daemon type.**

A lot of people may disagree with me on this statement. Particularly because we are not creating a ordinary UNIX daemon, **our daemon is designed for pentests and therefore is "malignant by design"**. Some people may claim this is extremely dangerous. But I will assure you, that outside of the scope of their assigned tasks, they are completely confined to performing what they were told to do and only that, very very well. They are bound to extremely confining chroot and permissions policies and cannot be told to diverge from their programming.

In order to incorporate features such as integration with a Raspberry Pi and fully automatic post-exploitation of cracked passwords....

1. We need a service-daemon managing programs such as Wardriver Express, besside-ng, Cylon-Raider, network manager, and the aircrack suite, and can continuously manage the nettools package autonomously.
2. For the password cracking rigs that we have managed to fully automate, we need a service hardware daemon to manage the constant rotation of cracked hashes, saving and exports of the Hashcat.potfile to WPA_supplicant. Most of the time, the network adapters were already gbeing managed by their own daemons.
3. We need a post-exploitation daemon to run a few repetitive tasks as soon as we connect to a network

# We do need at least two daemons.

These daemons are not true daemons. Rather they are what I like to call, subdaemons, and will be managed by native Linux daemons such as CRON and SystemD. They resemble system services like systemd and supervisord. But they wield a incredible amount of root permissions and power. Beccause of their role and the information they hold, and what they were designed to do, they are likely prioritized targets for malicious actors seeking to pry information.

They are however, going to be 100% entirely independent and will be composed of a single file, because current attempts to daemonize components for our hashcat integrations have caused major crashes and service restarts through systemd. It also broke and set us back for weeks on several projects when a python binary crashed and we were unable to retain another copy of the work, aside of a corrupted pyc file. That was our fully-automatic password cracker for hashcat.

# Design Proposals

Another proposition is to instead, split the daemon into multiple, independent, self-aware components. Our daemons often require the traversal of multiple directories, for example,

						\* \*to detect, copy and convert all of the .cap capture files on hard disk partition /dev/sda7 into another mounted partition on /dev/sdd2 and then convert the files to .hccapx format, crack the hashes, add the hashes to the potfile, extract the cracked hashes out of the potfile and generate a wpa_supplicant.conf file for each cracked BSSID, auto-load it into the /etc/wpa_supplicant directory of every compatible device (penetration testing device) that logs into our local wireless LAN*\ *\

From that, this daemon service will have several components.

			\* 1. A service daemon that manages a single drop-off folder for newly captured password hashes. Like /root/Documents/captured_WPA_hashes
			2. A hashcat manager daemon that will automatically rotate and delete cracked hashes while adding new hashes to the queue in /root/ArmsCommander/logs/HashCat
			3. A potfile manager daemon that will scan the potfile in /root/.hashcat/hashcat.potfile, find any new hashes, and write a wpa_supplicant.conf string into a master file.
			4. A wpa_supplicant editor daemon that will scan the /etc/wpa_supplicant/wpa_supplicant.conf file of every registered penetration device that connected, and then compare the cloned wpa_supplicant.conf, and make the necessary appendings and or additions to keep the visitor's wpa_supplicant.conf updated with new autologin c redentials. *\

Since these services operate independently from each other, then the UNIX service daemon will actually become a manager type of daemon that issues orders to multiple, independent subdaemon minions. The subdaemons are autonomous and it MAY BE possible to give certain orders to them to perform dangerous commands, but the likelihood of that requires the full discovery, compromise, and exploitation of both the manager daemon service and the subdaemon's source code while it's running. IT's kind of hard to mess with a background processes's code while it's running on Python. They would have to parse through thousands of lines of binary and intercept and alter the instructions that the service daemon is issuing to them but also have to reprogram the subdaemon's response to the task.

# Another Example: Wi-Fi Pentest Daemon.

The Wi-Fi Pentest Daemon will have several services

			1. A network interface daemon that will manage the wireless interfaces and run network discovery tools in the background. The NIC Daemon also reconnects the attacking device in the event that we lose connection, like hitting a firewall rule or bad signal.
			2. A Routersploit Back-End Daemon that utilizes the discovery I made about interface with the routersploit.routersploit.exploits.Exploit(args) class and directly change the target, port, threads parameters, and re-launch the autopwn module. The value of the target IP and port is constantly being updated and fed to them by the Network Interface Daemon and the Scanner Daemon
			3. A scanner daemon that runs services such as DotDotPwn directory traversal scanner, nmap scripts, Metasploit discovery tools,
			4. A Auth Daemon that tries passwords and attempts to brute-force newly discovered deviuces, networks, and ports discovered by the Scanner Daemon.

	A lot of our services are based on the standard tty console. We are considering using Pyrasite Terminals to interface with that to create a more transparent method to manipulate data in the backenmd while our attacks are starting off.

# What a attacker COULD DO to a LULLC Daemon.

It would be better for the attacker ***to spawn his own daemon services*** as soon as he acquires root access. Since the daemons would **very likely, not be aware of one another, and we as the user are not aware of their purposes because they are daemons. They do not have STDIN,STDERR, or STDOUT outputs**. They do not report to anyone. And outside of what they are designed to do and the chroot they are confined to, they have no power outside of their realms.

The only anomalies would be ifn a daemon malfunctioned because the attacker's daemons moved or relocated a directory needed for their main tasks. Or changed the permissions of a directory, causing our service daemon to crash.

# Basic Anatomy of LULLC daemons (Proposed)

We are basing this on the design of the python-daemon package available on PIP.

*The RPi Custom Routersploit Daemon is a single service manager in charge of dozens of subdaemons/bots. They are all derived from the same daemons.DaemonContext.(profile) class. Of my design.

The Daemon Class in its entirely is composed of a SINGLE Master Service Daemon. But this master Daemon manages subdaemons/bots that perform it's tasks and is defined as modules/functions/instances of a class.

So... lets say the NIC daemon if it was named NIC_subdaemon = process then it would have a method represented as a function for each task it does.*

**NIC_subdaemon module:**
\* *\def method_switch_MAC_addr(interface):
*\def run(): does the default method.
*\def stop():
-*\sys.exit('Ordered to stop')
*\def get_gw_ip(): does what its told and gets gateway IP, open port, and forwards this to my routersploit daemon to be used.
*\def daemonize(): *\
	Does all of the "cool shit"...

so python NIC_subdaemon.py and then NIC_subdaemon.stop() and NIC_subdaemon.get_gw_ip(). All the lame boring stuff.

When that's done, I am going to daemonize this process to make him run autonomously in background

[u]**NIC_subdaemon.daemonize()**[/u] Begins the satanic ritual that turns him into a daemon.

\* NIC_subdaemon.daemonize():
		os.chdir('/root/daemons_be_here')
		os.system('python -c import daemonize, from daemonize import star')
		original_file_myself = '/root/Documents/NIC_subdaemon.py'
		dir_path = os.path.dirname(os.path.realpath(original_dir))
		generate_daemon_NIC(daemon.DaemonContext, original_file_myself)
		return *\
**We need to have a function that tells us what to do**


**Then we need to add a class to generate a daemon, probably in a different file or module**

############################################################################
\* \* def generate_daemon_NIC(daemon_class_dir, process_instructions):
						sys.path.append(daemon_class_dir)
						from daemon_class_dir import daemon
						from daemon import *
						from daemon.DaemonContext import *

						MyLovelyDaemon = __daemon_module__.daemon.DaemonContext(NIC_subdaemon)
						MyLovelyDaemon.open()
						os.system('python -c import python_instructions; from instructions import star; instructions.task.method()')


						// Off he goes to do something!
						return MyLovelyDaemon *\ *\


##############################################################################

\* \*def Class DaemonContext(self): // standard template

				def __daemon_name__ = __module__.daemon.DaemonContext(__init__): // This part defines the traits of all of the daemons

				// the original daemon.DaemonContext design implies that you neeed to rewrite this class for EACH subdaemon you create and then give it DaemonContext capabilities. Like you would buiuld each daemon from scratch. Thats pretty inefficient.

				// I want it to where we can spawn as many daemons as we want. Just point this class to the program and fire it off.

							__daemon_name__.permissions = 'root'
							__daemon_name__.detach_process = 'True'
							__daemon_name__.chroot_directory = '/root/'
							__daemon_name__.working_directory = '/etc/network/'
							__daemon_name__.signalmap = '__daemon__name__signalmap.txt'
							__daemon_name__.instructions = '__daemon__name__progam.py'

							// This is your PRIMARY daemon program file. This is NOT a feature in python-daemon! You must add this yourself.

							__daemon_name__.umask = '755'
							__daemon_name__.pidfile = '/var/run/__daemon_name__.pidfile'
							__daemon_name__.uid = os.getuid() + 104-72 * 5
							__daemon_name__.gid = os.getgid() + 104+72 / 5
							__daemon_name__.preventcore = True
							__daemon_name__.initgroups = True
							__daemon_name__.stdin = '/dev/null'
							__daemon_name__.stdout = '/dev/null'
							__daemon_name__.stderr = '/dev/null'
\* *\
##################################################################################################################
# My vision of the primary Daemon class.


\* Class wireless_pentest.daemon.DaemonContext(__init__)
def wireless_pentest.daemon.DaemonContext(RSF_backend_subdaemon)
def wireless_pentest.daemon.DaemonContext(SHELL_subdaemon)
def wireless_pentest.daemon.DaemonContext(Discovery_subdaemon)
def wireless_pentest.daemon.DaemonContext(Auth_subdaemon) *\

######################################################################################################################
\* // this is the NIC_subdaemon example config

				 def wireless_pentest.daemon.DaemonContext(NIC_subdaemon): // This part defines the traits of all of the daemons

							NIC_subdaemon.permissions = 'root'
							NIC_subdaemon.detach_process = 'True'
							NIC_subdaemon.chroot_directory = '/root/'
							NIC_subdaemon.working_directory = '/etc/network/'
							NIC_subdaemon.signalmap = '__daemon__name__signalmap.txt'
							NIC_subdaemon.instructions = '__daemon__name__progam.py'
							NIC_subdaemon.umask = '755'
							NIC_subdaemon.pidfile = '/var/run/NIC_subdaemon.pidfile'
							NIC_subdaemon.uid = os.getuid()
							NIC_subdaemon.gid = os.getgid()
							NIC_subdaemon.preventcore = True
							NIC_subdaemon.initgroups = True
							NIC_subdaemon.stdin = '/dev/null'
							NIC_subdaemon.stdout = '/dev/null'
							NIC_subdaemon.stderr = '/dev/null' *\


**if I wante dto make me a network interface daemon right now.... quickn and easy....**


\* NIC_subdaemon = wireless_pentest.daemon.DaemonContext(__init__) // better yet, make one specifically for NIC subdaemon.
NIC_subdaemon.open() *\
\*
// **Powers up the daemon. Right there.**
def config_daemon(NIC_subdaemon, desired_uid, desired_gid):
		try:
			new_uid = desired_uid
			new_gid = desired_gid

			// accoridng to the daemon module .get_username_for_uid(uid)
			// 0 = root
			// 1 = daemon
			// 2 = bin
			// 3 = sys
			NIC_subdaemon.change_process_owner(new_uid, new_gid, initgroups=True)
		except DaemonOSEnvironmentError:

		// catches wrong permissions error and attempts to change its UID AGAIN to not have itself die.

			new_uid += 1
			new_gid += 1
			config_daemon(NIC_subdaemon, new_gid, new_uid) // tries a new uid and gid
		return daemon_name, new_gid, new_uid

NIC_subdaemon.change_working_directory('/etc/wpa_supplicant')

// dump passwords
daemon.pwd.getpwall()
 *\

#######################################################################################


\* def Class DaemonError(exceptions.Exception):

// why a daemon killed itself. Or contains what may have happened before the daemon crashed. *\


I need to work on this, Because It can tell me alot of why a Daemon suddenly died, I want it to at least leave me a encrypted message or status code that I can interpret. Who knows if I am getting REVERSE PEN-TESTED?!?

***


# [Improving and Honing your Hacking Abilities by Modifying the Routersploit Shell]


Update on December 14th.

I already managed to achieve it. It's quite sloppy and it is ugly though. A fully autonomous raspberry pi that exploits it's victims.

I need to look into the matter more, since now I know how to redirect the values and execution in the routersploit.exploits.Exploit Class, as shown by the alert.log file.

But the fact that Routersploit automatically gets caught up in the standard Debian logs is alarming.
<br><br>
								\* **[Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)
								/var/log/user.log:63628:Dec 23 16:25:39 I_DO_COCAINE org.gnome.Shell.desktop[9191]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)
								/var/log/user.log:63632:Dec 23 17:02:22 I_DO_COCAINE org.gnome.Shell.desktop[9191]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)
								/var/log/user.log:63633:Dec 23 17:02:22 I_DO_COCAINE org.gnome.Shell.desktop[9191]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)]** *\

<br><br>
Meanwhile I am trying to create a duplicate pipe to allow viewing of the standard routerpsloit shell. However I came across several realizations, one there wont be any output on that shell because this is completely automated and therefore no data was entered into the default shell, two, there really is no need for entry of text, three, I already resolved the issue of the module import problems for integrating with routersploit, you are required to manually append both routersploit folders from the official repo to allow your custom autopwn module to work.



After action report, Wednesday, December 13th, 2017.

I have successfully managed to take control of the RouterSploit Shell By passing commands through the their Shell API using the standard Python 2.7 console.

What this means, is that I can createa a FULLY AUTONOMOUS Raspberry Pi that is designed to attack wireless networks with cracked passwords using the scanners/autopwn module. The Pi will be the one "typing the commands" into RouterSploit using carefully timed Python scripts, cronjobs, and bash shell commands.

How the RouterSploit Shell works is that it has several sub-components that make up the terminal:

1. A primary, Routersploit Interpreter Shell that makes up several python scripts
2. A secondary, lower-in-privilege Interpreter Shell that does most of the contract between the user and the toolkit. It is represented as a class-object in the file interpreter.py and shell.py
3. Finally a SSH-Interactive Shell that works behind the scenes. The purposes of this is unknown but I noticed it performs a lot of HTTP lifting as some sort of offensive back-end. This one may be the one with the directory traversal tactics and HTTP brute-forcing modules for Routersploit.

As a user, you can actually interact with ALL THREE SHELLS at the same time right now to give it customized commands and background jobs, by downloading the official Routersploit Repo:

and then  navigate to the module tree directory (for me it's in /root/Documents)
**
cd /root/Documents**

And activate python and immediately import the modules
**
																								\* python
																								>>>import routersploit
																								>>>from routersploit import *
																								>>>import __future__
																								>>>import __builtin__
																								>>>from __builtin__ import *
																								>>>import routersploit.modules.utils
																								>>>from __future__ import absolute_import**
																								>>>interpreter.BaseInterpreter()
																								>>><routersploit.interpreter.BaseInterpreter object at 0x7fb92ac76510>
																								>>>interpreter.BaseInterpreter(__init__) *\

If you are lost, don't forget you use your help(OBJECT) and dir(OBJECT) commands.

But what I found was this one command, which after a bit of tinkering, was fully enabled to allow me to integrate my scripts and software with theirs and allow me to push commands to Routersploit to give it a job to do.
**
interpreter.RoutersploitInterpreter().commands()**
***

\* ['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']*** *\


This is the most basic of the RSF Shell commands, all it does is query the shell to tell us all of the available commands. And the unordered array was the output. All of this was discovered by typing commands into the Python shell. That means it should be as easy as importing the Routersploit modules into your own Python programs.

The syntax for this, and other subsequent important commands comes in this format...

																								\* **Interpreter.RouterSploitInterpreter.action('CMD', args, xargs)** *\

Everything that was on the top of that Python list, can be executed through this interpreter, as long as you IMPORT the right modules! As it turns out, there was a lapse in organization for the RSF development, and I spent about two yhours looking for the other modules to import to give the shell full functionality. But it seems current progress points is that they are trying hard to merge two different designs for their back-end together.

Here is a sample of some syntax.

\*
# starts up the interpreter, basically the shell started.

interpreter.RoutersploitInterpreter.start()

# This is actually the auto-tab-completion module for RouterSploit.

BaseInterpreter.available_modules_completion('payloads')

# This is the equivalent of typing "Show Targets" in Metasploit.

interpreter.utils.module_required._show_devices('devices')

# This is what happens when you type "show scanners" in the RSF shell. The opt-parsing code immediately sends it to it's own submodule/process.

interpreter.utils.module_required.__show_modules('scanners')

# When you type "use scanners/autopwn" in Routersploit

interpreter.BaseInterpreter().command_use('scanners/autopwn')

# This is how you can dump the Routersploit logs. Note the lower-case PRINT command on the left.

print interpreter.RoutersploitInterpreter(BaseInterpreter).history_file

# Even if you didn't know the module's programming syntax, you can still directly-inject commands into the parse_line(cmd) module. This was the earliest moment I could find a reliable injection point for commands.

interpreter.BaseInterpreter().parse_line("show payloads")


# The next step up is calling the command_handler() to have it review the parsed user input. If you fail to inject a command into the parse_line function, a less reliable but decent second try is injecting the command into the get_command_handler() function.

interpreter.BaseInterpreter(get_command_handler('show')) *\

# [The auto exploiting Rpi...]

Any assailant will not look suspicious at all as long as the Pi is powered on  and the attacker or "pentester" should just be walking around staying within wireless range. Now that I have found a breakthrough to createa a fully-automated initial exploitating Pi I think it's your turn to find a useful for this too ;).

It's much like handling a "pentest drop-box". But this time, the Pi is completely automated and ordered to exploit and post-exploit it's targeted victims

Furthermore I have completed approximately 90% of the rest of the work that is meant to be added to the Pi or to compliment the gear of "wireless pentesters". For example...
\*
1. A fully autonomous password-cracking rig that is automated by cronjobs, Python scripts, and shell scripts. It handles the process of converting captured WPA handshakes into a hashcat compatible format, and will automataically queue and begin brute-forcing (dictionary attack style) as soon as it reboots. It applies a improved version of my hashcat add-ons that I put into Arms-Commander.

2. A completely automatic, cracked-password sorting and credential installation service. What I mean is, at a push of a button, it will parse the default HashCat potfile at /root/.hashcat/hashcat.potfile (for Kali Linux installations) to get rid of duplicate entries and false-positives.

And then "installs" the credentials onto your nearest mobile device by copying and appending the login information to your /etc/wpa_supplicant/wpa_supplicant.conf *\

As soon as you approach the area of your target that you are returning to, your network-manager should have already connected you to the target, ready for exploitation and post-exploitation.


3. A fully autonomous, "War-driving Raspberry Pi". Do not confuse this one with #1. As this Raspberry Pi's mission is to grab NEW ENCRYPTED PASSWORDS as I move from one spot to another.

The purpose of the other Pi, is to break back into a network that we have just CRACKED credentials of.


Both of them are powered by automation scripts that are practically "dumbed-down". In other words, it really can't do much of a job outside of what I designed them to do, but it does their assigned tasks, very very well, as long as it's plugged into a microusb cord.


What else should I mention? I also built a wireless attack drone out of a AR Drone 2.0 I got from Fry's at Black Friday.

Also more than meets the eye for all of these Raspberry Pi's. They might look small, but they pack quite a punch. In both the initial deauth-attack and returning exploitation phases of the pentests, they are equipped with top-of-the-line wireless antennas that are extremely hard to find out in the wild.

I have four amplifiers mated to a network card at any time of the day.
\*
2x Hak5 Wireless Adapters with a integrated RT3070 Wi-Fi Amplifier
1x Hak5 Long-Range 400-to-800mW Wi-Fi Booster for reverse-SMA connections
1x Ubiquiti Networks M2 Bullet Wireless Signal Injector, with special features such as audio-beep assisted targeting, persistent-reconnections with my targets, and a neat spectrum analyzer to determine levels of interference and the feasibility of a attack angle if you consider radio interference.


Also 2x Antennas exceeding 13 dbi, each.
	a. One is a SimpleWiFi 2.4Ghz Parabolic Dish Antenna with a rating of 24 dbi
	b. Another is a cheap TrendNet Panel I got from Fry's rated at 14dbi. It is still useful because it allows the signal to be projected in a 30-degree wide "cone", which is more suitable for Rogue Access Points. *\


# Company dragged into a cybersecurity incident. Handled.

Earlier this month, my website has suffered a major network attack caused by a brute-forcing botnet (of approximately 1,868 bots) that nearly killed my servers. As a response, I constructed a automatic snort alert log parser and autobanner, as well as custom configurations for Intrusion Prevention and Detection Systems for VPS-hosted websites.

Not only did I turn the tables on the attacker with just a few simple fail2ban and snort rules applied company-wide (and a full switch-out of every port, especially 22, to avoid attracting new dickheads), but I also managed to enumerate the HTTP headers of the attacker, causing him to be "put on the run".

Anyways, this is my first two days back to work since the last day of class. I will have a long busy time building my company (and I don't think I passed the exam) but I will try my best to ensure that the more useful of my creations will trickle it's way into public release in ArmsCommander and Cylon-Raider. My main concern is that  in particular for this update, a lot of the things it purports to do may end up breaking your system.

It requires root-level access to everything, and it messes with critical startup processes to achieve the cyber-defense results that I wanted. For that reason, I decided to create a "Prototyping Repo" located here, https://github.com/tanc7/ArmsCommander-TestBed. You may try them out if you wish, but you must understand that I am not responsible for any unforseen incidents and/or damages caused by this. You are taking this, out of your own risk. Also be aware that the scripts located in that link are NOT complete. And that means little to no tech support if you screw something up.

But assuming that all goes well, I may personally vet for the script or program to be added to the official Arms-Commander Repository.

C.T. Lister
Lister Unlimited Cybersecurity Solutions, LLC.
9:55pm, November 13th.
</html>
