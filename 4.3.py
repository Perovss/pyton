#!/usr/bin/env python3
import json
import subprocess as sp
import os
hostnames = ["ya.ru", "mail.google.com", "google.com"]
exit_file = dict()
if os.path.exists("iptables.json"):
    with open("iptables.json", "r") as read_file:
        file_data = json.load(read_file)
else:
    open("iptables.json", "w")
    file_data=0
count=0
for hostname in hostnames:
    response,status= sp.getstatusoutput("ping -c1 " +str(hostname))
    ip_host=status.split(' ')[2].replace("(","").replace(")","")
    try:
        ip = file_data[hostname]
    except TypeError:
        ip = 0
    if ip==0:
        old_ip_host=ip_host
    else:
        old_ip_host =file_data[hostname]
    if response == 0:
        if ip_host==old_ip_host:
            print(hostname+" - "+ip_host)
        else:
            print('[ERROR] ' + hostname + ' IP mismatch: <' + ip_host + '> <' + old_ip_host + '>')
    else:
        print ('[ERROR] '+hostname+' down!')
    exit_file.update({hostnames[count]: ip_host})
    count+=1
with open("iptables.json", "w") as read_file:
    json.dump(exit_file, read_file)