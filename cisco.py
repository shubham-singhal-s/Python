import subprocess
import os
import _thread
import threading
import sys

os.system("curl -s www.cisco.com | grep cisco.com | grep -o 'http[^\"]*' | awk -F  \"/\" '{print $3}' | grep cisco | uniq -u > domain > domain")

def pingit( ipadd):
    #print(os.system("host "+str(ipadd)+" | grep 'has address' "))i
    hostString = ipadd.strip('\n')
    bashCommand = "host %s | grep 'has address' " %hostString
    os.system(bashCommand)

threads = []

with open("domain", "r") as ins:
    for line in ins:
        t = threading.Thread(target=pingit, args=(line,))
        threads.append(t)
        t.start()


for x in threads:
    x.join()

