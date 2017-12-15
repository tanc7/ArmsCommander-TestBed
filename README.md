<html>

[Improving and Honing your Hacking Abilities by Modifying the Routersploit Shell]

Update on December 14th.

I already managed to achieve it. It's quite sloppy and it is ugly though. A fully autonomous raspberry pi that exploits it's victims.

I need to look into the matter more, since now I know how to redirect the values and execution in the routersploit.exploits.Exploit Class, as shown by the alert.log file.

But the fact that Routersploit automatically gets caught up in the standard Debian logs is alarming.
<br><br>
								**[Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)
								/var/log/user.log:63628:Dec 23 16:25:39 I_DO_COCAINE org.gnome.Shell.desktop[9191]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)
								/var/log/user.log:63632:Dec 23 17:02:22 I_DO_COCAINE org.gnome.Shell.desktop[9191]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)
								/var/log/user.log:63633:Dec 23 17:02:22 I_DO_COCAINE org.gnome.Shell.desktop[9191]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x1800001 (autopwn.py)]**

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
python
>>>import routersploit
>>>from routersploit import *
>>>import __future__
>>>import __builtin__
>>>from __builtin__ import *
>>>import routersploit.modules.utils
>>>from __future__ import absolute_import**
>>>interpreter.BaseInterpreter()
>>><routersploit.interpreter.BaseInterpreter object at 0x7fb92ac76510>
>>>interpreter.BaseInterpreter(__init__)

If you are lost, don't forget you use your help(OBJECT) and dir(OBJECT) commands.

But what I found was this one command, which after a bit of tinkering, was fully enabled to allow me to integrate my scripts and software with theirs and allow me to push commands to Routersploit to give it a job to do.
**
interpreter.RoutersploitInterpreter().commands()**
***
['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']***


This is the most basic of the RSF Shell commands, all it does is query the shell to tell us all of the available commands. And the unordered array was the output. All of this was discovered by typing commands into the Python shell. That means it should be as easy as importing the Routersploit modules into your own Python programs.

The syntax for this, and other subsequent important commands comes in this format...

**Interpreter.RouterSploitInterpreter.action('CMD', args, xargs)**

Everything that was on the top of that Python list, can be executed through this interpreter, as long as you IMPORT the right modules! As it turns out, there was a lapse in organization for the RSF development, and I spent about two yhours looking for the other modules to import to give the shell full functionality. But it seems current progress points is that they are trying hard to merge two different designs for their back-end together.

Here is a sample of some syntax.


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

interpreter.BaseInterpreter(get_command_handler('show'))

[The auto exploiting Rpi...]

Any assailant will not look suspicious at all as long as the Pi is powered on  and the attacker or "pentester" should just be walking around staying within wireless range. Now that I have found a breakthrough to createa a fully-automated initial exploitating Pi I think it's your turn to find a useful for this too ;).

It's much like handling a "pentest drop-box". But this time, the Pi is completely automated and ordered to exploit and post-exploit it's targeted victims

Furthermore I have completed approximately 90% of the rest of the work that is meant to be added to the Pi or to compliment the gear of "wireless pentesters". For example...

1. A fully autonomous password-cracking rig that is automated by cronjobs, Python scripts, and shell scripts. It handles the process of converting captured WPA handshakes into a hashcat compatible format, and will automataically queue and begin brute-forcing (dictionary attack style) as soon as it reboots. It applies a improved version of my hashcat add-ons that I put into Arms-Commander.

2. A completely automatic, cracked-password sorting and credential installation service. What I mean is, at a push of a button, it will parse the default HashCat potfile at /root/.hashcat/hashcat.potfile (for Kali Linux installations) to get rid of duplicate entries and false-positives.

And then "installs" the credentials onto your nearest mobile device by copying and appending the login information to your /etc/wpa_supplicant/wpa_supplicant.conf

As soon as you approach the area of your target that you are returning to, your network-manager should have already connected you to the target, ready for exploitation and post-exploitation.


3. A fully autonomous, "War-driving Raspberry Pi". Do not confuse this one with #1. As this Raspberry Pi's mission is to grab NEW ENCRYPTED PASSWORDS as I move from one spot to another.

The purpose of the other Pi, is to break back into a network that we have just CRACKED credentials of.


Both of them are powered by automation scripts that are practically "dumbed-down". In other words, it really can't do much of a job outside of what I designed them to do, but it does their assigned tasks, very very well, as long as it's plugged into a microusb cord.


What else should I mention? I also built a wireless attack drone out of a AR Drone 2.0 I got from Fry's at Black Friday.

Also more than meets the eye for all of these Raspberry Pi's. They might look small, but they pack quite a punch. In both the initial deauth-attack and returning exploitation phases of the pentests, they are equipped with top-of-the-line wireless antennas that are extremely hard to find out in the wild.

I have four amplifiers mated to a network card at any time of the day.

2x Hak5 Wireless Adapters with a integrated RT3070 Wi-Fi Amplifier
1x Hak5 Long-Range 400-to-800mW Wi-Fi Booster for reverse-SMA connections
1x Ubiquiti Networks M2 Bullet Wireless Signal Injector, with special features such as audio-beep assisted targeting, persistent-reconnections with my targets, and a neat spectrum analyzer to determine levels of interference and the feasibility of a attack angle if you consider radio interference.


Also 2x Antennas exceeding 13 dbi, each.
	a. One is a SimpleWiFi 2.4Ghz Parabolic Dish Antenna with a rating of 24 dbi
	b. Another is a cheap TrendNet Panel I got from Fry's rated at 14dbi. It is still useful because it allows the signal to be projected in a 30-degree wide "cone", which is more suitable for Rogue Access Points.


Earlier this month, my website has suffered a major network attack caused by a brute-forcing botnet (of approximately 1,868 bots) that nearly killed my servers. As a response, I constructed a automatic snort alert log parser and autobanner, as well as custom configurations for Intrusion Prevention and Detection Systems for VPS-hosted websites.

Not only did I turn the tables on the attacker with just a few simple fail2ban and snort rules applied company-wide (and a full switch-out of every port, especially 22, to avoid attracting new dickheads), but I also managed to enumerate the HTTP headers of the attacker, causing him to be "put on the run".

Anyways, this is my first two days back to work since the last day of class. I will have a long busy time building my company (and I don't think I passed the exam) but I will try my best to ensure that the more useful of my creations will trickle it's way into public release in ArmsCommander and Cylon-Raider. My main concern is that  in particular for this update, a lot of the things it purports to do may end up breaking your system.

It requires root-level access to everything, and it messes with critical startup processes to achieve the cyber-defense results that I wanted. For that reason, I decided to create a "Prototyping Repo" located here, https://github.com/tanc7/ArmsCommander-TestBed. You may try them out if you wish, but you must understand that I am not responsible for any unforseen incidents and/or damages caused by this. You are taking this, out of your own risk. Also be aware that the scripts located in that link are NOT complete. And that means little to no tech support if you screw something up.

But assuming that all goes well, I may personally vet for the script or program to be added to the official Arms-Commander Repository.

C.T. Lister
Lister Unlimited Cybersecurity Solutions, LLC.
9:55pm, November 13th.
</html>
