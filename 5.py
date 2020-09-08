#!/usr/bin/env python3
import json
import yaml
import subprocess as sp
import os
hostnames = ["ya.ru", "mail.google.com", "google.com"]
list_ip_hosts=list()
ip_host=str()
iptables=0
if os.path.exists("iptables.json"):
    with open("iptables.json", "r") as read_file:
        file_data = json.load(read_file)
        iptables = file_data["ip"]
        print(type(iptables))
else:
    open("iptables.json", "w")
count=0
for hostname in hostnames:
    response,status= sp.getstatusoutput("ping -c1 " +str(hostname))
    ip_host=status.split(' ')[2].replace("(","").replace(")","")
    list_ip_hosts.append(ip_host)
    if iptables==0:
        old_ip_host=ip_host
    else:
        old_ip_host = iptables[count]
    if response == 0:
        if ip_host==old_ip_host:
            print(hostname+" - "+ip_host)
        else:
            print('[ERROR] ' + hostname + ' IP mismatch: <' + ip_host + '> <' + old_ip_host + '>')
    else:
        print ('[ERROR] '+hostname+' down!')
    count+=1
exit_file={"ip": list_ip_hosts}
with open("iptables.json", "w") as read_file:
    json.dump(exit_file, read_file)