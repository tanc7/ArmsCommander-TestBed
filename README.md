<html>

<h4>Ambitions for the Year of 2018
</h4>
<p>Due to the dramatic changes in the Trump Tax Bill that could negatively affect Service-Focused LLCs such as Lister Unlimited (Cybersecurity Services), the founder of the company Lister Unlimited Cybersecurity Solutions, Chang Tan Lister, has immediately ordered sweeping changes to be enacted in anticipation of Tax-Year 2018, effective immediately.
</p>

<b><p>Note, this is referring to Tax-Year, 2018! Right now is the end of Tax-Year 2017. Therefore, any tax practices regarding the up and coming Tax Season for Tax Year Ending 2017, will remain the same.
</b></p>

<p>At the end of Tax-Year 2018, there will be a sudden shift in priorities for the Operations of LULLC. First and foremost.
</p>
<ul>
<li><b>Lister Unlimited will make a "sideways transition" from Service-Oriented to Manufacturing-Oriented by the end of year 2018</b>. Through refiling of the paperwork for a State-Approved LLC (Articles of Organization, Operating Agreements, etc.)
</li><li>At that point in time, LULLC will agree to pay the State Sales Tax and will change to a different NAICS code relevant to manufacturers.
</li><li><b>The manufactured-products to be marketed in question are, as of December 28th, 2017, three components of a Wireless-Attack Hardware Toolkit</b>. Each can be independently purchased/ordered, or bought as a single package entirely (recommended). In brief, these are to be... (a) a specifically modified Raspberry Pi that can harvest and exploit wireless access points automatically (b) A fully automated server that cracks passwords and queues new ones (c) a Drone that does WPA2 credential harvesting.
</li><li>For the foreseeable future, <b>Lister Unlimited will still remain as a Limited Liability Company electing to be taxed as a Sole-Proprietorship</b>.
</li><li>If additional holders of interest are expected to be included within the organization, in other words, someone else has chosen to own a percentage of ownership interest, <b>the most likely outcome is the reorganization of LULLC to be a LLC electing to be taxed as a Partnership under Federal Tax Laws</b>. Otherwise, if forced to incorporate under Federal Law, then LULLC aims to minimize tax liabilities through reorganization into a S-Corporation. LULLC has no interest in issuing shares at this time, and therefore, <b>adamantly forbids becoming a C-Corporation.</b>
</li><li><b>Github repos and Copyright and intellectual property laws regarding these "hacking-toolkits" are still under discussion. </b>Currently, Chang Tan Lister likes to keep the "software back-end" of these products as "open-source" and only retain intellectual property rights on the "hardware" and "kernel-modifications" to the components, such as the Raspberry Pi.
</li></ul>

<p><b>A good example is the Hak5 repos for Bash-Bunny, USB Rubber Ducky, Wi-Fi Pineapple and LAN Turtle.</b> The holders of Hak5, LLC of Richmond, CA has selectively marked certain items of their products as intellectual property, https://github.com/hak5. Primarily the hardware. And the remainder, such as the Open-Source GitHub repos, https://github.com/hak5/bashbunny-payloads, remain Open-Source.
</p>
<p><i><b>We suspect it was to encourage Open-Source Contributions to the product, and also to keep their hands clean from possible litigation.</b> For example, in Hak5 Product, the LAN Turtle, there is a feature called AutoSSH. The developers of AutoSSH have nothing to do with the activities of Hak5, LLC or vice versa http://www.harding.motd.ca/autossh/. But Hak5, LLC has chosen to use the feature anyways. But the works of Hak5, LLC, and the makers of AutoSSH <b>remain distinct and separately identifiable</b>.</i>
</p>
<p>Because we, in Lister Unlimited Cybersecurity Solutions, LLC, have had our hands tied up in nearly the same manner, that is, repurposing existing methods and technologies to create a product of our own, <b>we have to allow certain features, primarily from the Raspberry Pi Foundation and various GitHub Projects, to remain open source</b>.
</p>

<b><p>What will NOT be open-source, and thus, proprietary to Lister Unlimited and is intellectual property, are:
</b></p>

<ul>
<li><b>Official Branding, Logos, Recognizable Trademark Symbols, and Web Domains</b> that represents intellectual property of Lister Unlimited Cybersecurity Solutions, LLC.
</li><li><b>Various methods used to modify the existing Raspberry Pi</b> to make it viable for penetration testing
</li><li><b>The exact process for installation and construction </b>of these components to create any of the three aforementioned products
</li><li><b>The exact process of enabling root-logins and allowing on-boot autorun scripts </b>to function on Raspian
</li><li><b>kernel-modifications</b> made to Kali Linux (Desktop) to allow the repurposing of NVidia brand GPUs to crack passwords
</li><li><b>CLI and software backend-integration methods</b> between LULLC products and various Open-Source GitHub projects such as RSF.
</li><li><b>Custom network-configurations </b>that permit the LULLC product to operate in tandem with other LULLC products and communicate in real-time.
</li><li><b>Customized switches, arrays, circuitry, silicon chips and controllers</b>, that do not readily exist and was obtained through a special deal between Lister Unlimited and a Original Equipment Manufacturer, solely for the purpose of manufacturing the product.
</li><li><b>Manufacturing processes that were developed and optimized</b> by supply-chain engineers to allow efficient mass-production and distribution of the LULLC product.
</li></ul>

<p>Much like all of the Hak5 products, our LULLC products can be reverse-engineered using entirely off-the-shelf parts, https://forums.hak5.org/topic/34950-how-to-make-a-usb-rubber-ducky-using-a-normal-usb-stick/.
</p>
<p><b>But we do not recommend it. Not because it would be illegal (it's not).</b> But we at LULLC invested considerable amounts of time into making this as easy as possible for the consumer. Documentation in 2017 is hard to come by, and thankfully our Research and Development Staff have resolved all of the issues and enabled these products to function, exactly the way we wanted it to.
</p>



<h4>                                              DRAFT COPY
</h4><h4>                                              CULMINATION OF A NEW PROJECT
</h4>
"Dized" stands for Daemonized Applications.

<p>                              Chang Tan Lister
                              Lister Unlimited Cybersecurity Solutions, LLC.
                              December 19th, 2017.</p>

We use the term daemonzied because we implement a combination of open and proprietary technologies (hardware and coding libraries) to enable...
<ul>
<li>the malware we generate
</li><li>the hardware that supports and runs this malware
</li><li>the attacker who uses the toolkits and C2 (Command-and-Control Systems)
</li><li>and the target who (unwillingly) has become it's victim
</li></ul>

to adopt the characteristics of...
<ol><li>  <b>All of the basic traits of a APT (Advanced Persistent Threat characteristics)</b>, whose goal is to maintain access rather than the typical "in-and-out exfiltration plan"
</li><li>  to have the malware retain some degree of <b>"autonomy"</b>
</li><li>  <b>and some degree of "invulnerability"</b> (e.g. fork itself to evade destruction by antivirus, firewalls, IDS/IPS, heuristic scanners and can repeatedly regenerate itself from "actual deaths" by becoming a actual UNIX Daemon)
</li><li>  <b>and some degree of "self-sufficiency"</b> (e.g. capable of performing rudimentary fuzz-testing)
</li><li>  <b>and some degree of "evolution" by stress-induced response</b> (e.g. the malware is aware that there are no known documented vulnerabilities that it can exploit and it must discover a vulnerability on it's own accord. It will begin fuzz-testing and attempt to replicate "Proof-of-Concept" code into copies of itself, test that PoC, and report back to it's master)
</li><li>  <b>obviously a FULL degree of "stealth-and-obfuscation-options".</b> This means, it should be capable of producing a complete client process of ANY known tunneling protocol, standalone, wrapped, encapsulated, known and unknown. (e.g. SSH tunneling, UDP tunneling, DNS tunneling, virtual, SSL, UDP-over-TCP, VPN-over-SSH, TCP-over-SOCKS, TCP-over-HTTPS)
</li><li>  <b>In order to have a better chanc</b>e at evading the Intrusion Detection System after we already snuck past it's Ingress Filtering Rules, Intrusion Prevention System, killed the Anti-Virus, compromised the Firewall, Escalated Privileges to ROOT/SYSTEM, established Persistence, Compromised Patching Systems, Pivoted to it's neighbors in the Internal Network.
</li><li>  And to always <b>"maintain a advantage against the White Hats"*</b>
</li></ol>
*I am only saying this to refer to the Blue Team in a penetration test.

<h4>Current Projects
</h4>
<h4>STARTED DEVELOPMENT:"GROWING-PAINS":
</h4>  Automated Internal Fuzzing Service & "Zero-Day Discovery Tool" & Primative Proof-of-Concept Generator. Portable Malware Version & Client.

<h4>NOT STARTED:"EBOLAIDS":
</h4>  Command-and-Control (C2) for GROWING-PAINS. Unlike GP, Ebolaids retains a full development library, debugger, packet analyzer and should be able to compile binaries for any architecture, and any operating system (see Mirai botnet source code, they got nasty stuff for any processor or platform).

  It functions as the server in the relationship between the emergent malware and itself and provides a means of communication and job allocation for the malware.

<h4>DEVELOPMENT STAGE**:"INCANTATION":
</h4>  Automated Wireless Handshake-Capturing and Post-Exploitation Toolkit. WPA2-PSK and WPA2-MGT/ENT.

<p>  As of 12/19/17, the planned release next-year contains several portions, a Routersploit backbone(https://github.com/reverse-shell/routersploit), a modified API-to-CLI interface, credential parser, integration with other tools such as wpa_supplicant, wicd_curses/wicd_cli, rsf, dotdotpwn, metasploit scripts, and customized options catered specifically for the $30 Raspberry Pi micro-computer(https://www.raspberrypi.org/products/), which is the intended host of this toolkit.

  A subproject involves automatically running captured hashes into the project listed right after, auto-parsing the cracked credentials, and storing it back into the Raspberry Pi. Making abusing cracked passwords as easy as plugging in power and bringing the Pi home.

  And using this will be as easy as running the installer, dropping off the Pi within wireless access range of the target, and picking up the dropbox six to twelve hours later***.

  ***Assuming you use the recommended idea of a portable battery pack as a power supply. The same ones used to recharge your phone on the go.</p>

<h4>NEAR COMPLETION:"DICK-FORGE":
</h4>  Fully Automatic Password Cracker with a Hashcat Base and capable of processing rulesets and customized attack binaries (PRINCEPROCESSOR). Integrates with CRON daemons and systemd processes. Auto-traverses your specified directories to search for more untouched hashes (passwords) to crack.

  Auto-optimizes itself in response to errors discovered from the proprietary NVidia driver installation process.

<h4>NOT STARTED:"BLACK-CHANTING-GROWS":
</h4>  Tunneling Method Library and Automater.
<h4>NOT STARTED:"SUNSPEAR":
</h4>  Automated Log Parsing and Analysis. Auto-adapting Cybersecurity measures to prevent discovery by the responding Incident Response Team.


**Research was completed last week. Everything that is needed is already available. But no one had rolled anything out that is practical yet. So I am getting started on working on this.

<h4>Our Current Environment.
</h4>
<p>Developers have tried for decades in attempting to make malware and computer viruses as close if not exactly identical to the biological definition of a computer virus. All of them have failed in some respect. Particularly, the AI part was harder than expected to implement and "unpredictable mutation" of actual biological viruses. https://cs.stackexchange.com/questions/27976/would-it-ever-be-possible-for-computer-viruses-to-evolve-new-genes-to-allow-th

However, a lot of these demands have been met, SEPARATELY, and with DIFFERENCES in scope by various exploit toolkits, security firms like Rapid7, and by GitHub Developers, such as Pupy. The "evolution" portion was answered somewhat by toolkits such as Veil-Evasion (changing signature), PSScrambler (targeted towards MS Windows Portal Executable .exe formats) and Metasploit msfvenom (changes other operating characteristics, most importantly the way the traffic looks on a IDS). But it was definitely not automated. And such exploits must constantly be rediscovered, reimplemented, and republished on GitHub and the Kali Linux APT Repos when the security patches roll in.

And thats what I call a pain-in-the-ass.</p>

<h4>Asking for Help from Contributors.
</h4>
<p>I highly doubt that a single person like me could actually finish this project. I reaally do need outside help and I could appreciate some talented developers out there in the field. I accept anyone, regardless of experience level, as long as they understand at least one language or background, whether it be Python/Ruby-on-Rails, C & Assembly, Encryption/Obfuscation, Network Engineering etc., if you have time to pitch in your contribution to the project I would really appreciate it.

I never intended for this idea to ever take off. But hopefully it'll inspire a greater effort to get some future project up and going. I just want to see this goal be realized with or without me.
</p>

<h4>Difference between this and release version of Arms-Commander and Cylon-Raider:
</h4>
<p>This is a significant digression from the intents of ArmsCommander, which is a collection of penetration test tools to make the pentester's job EASIER. ArmsCommander never automated the entire processs of the actual EXPLOITATION, PAYLOAD DELIVERY, EXFILTRATION, etc. All AC did was, help you "get-in" and find out "which doors are unlocked". I never thought much of the "getting-out-part" but as I applied more time
into fine-tuning my exfiltration techniques I had a growing urge to share these tactics to the community.</p>
</html>
