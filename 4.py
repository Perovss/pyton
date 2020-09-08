#!/usr/bin/env python3
import subprocess as sp
import os
hostnames = ["drive.google.com", "mail.google.com", "google.com"]
list_ip_hosts=str()
ip_host=str()
iptables=0
if os.path.exists("iptables.txt"):
    with open("iptables.txt", "r") as read_file:
        iptables=read_file.read().split(' ')
else:
    open("iptables.txt", "w")
count=0
for hostname in hostnames:
    response,status= sp.getstatusoutput("ping -c1 -w2 " +str(hostname))
    ip_host=status.split(' ')[2].replace("(","").replace(")","")
    list_ip_hosts+=ip_host+' '
    if iptables==0:
        old_ip_host=ip_host
    else:
        old_ip_host = iptables[count]
    if response == 0:
        if ip_host==old_ip_host:
            print(hostname,ip_host)
        else:
            print('[ERROR] ' + hostname + ' IP mismatch: <' + ip_host + '> <' + old_ip_host + '>')
    else:
        print ('[ERROR] '+hostname+' down!')
    count+=1
file_data = open('iptables.txt', 'w')
file_data.write(list_ip_hosts)
file_data.close()