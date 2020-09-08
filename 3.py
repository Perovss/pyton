#!/usr/bin/env python3
import subprocess as sp
import os

code = sp.call(["ping","-c1", "www.yahoo.com"])
hostname = ["drive.google.com", "mail.google.com", "google.com"]

for n in hostname:
    response = os.system("ping -c1 " + n)
    if response == 0:
        print (n,response,'is up!')
    else:
        print (n, 'is down!')

def ipcheck():
    status, result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
    if status == 0:
        print("System " + str(pop) + " is UP !")
    else:
        print("System " + str(pop) + " is DOWN !")
pop = input("Введите IP адрес: ")
ipcheck()