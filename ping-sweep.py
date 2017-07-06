import subprocess
import ipaddress
import os
import _thread
import threading
import sys

def pingit( ipadd):
    response = os.system("ping -c 1 " + str(ipadd) + " > /dev/null 2>&1")
    if response == 0:
        print(str(ipadd), 'is up!')

net_addr = str(sys.argv[1])
ip_net = ipaddress.ip_network(net_addr, strict=False)
threads = []

for i in ip_net.hosts():
    t = threading.Thread(target=pingit, args=(i,))
    threads.append(t)
    t.start()

for x in threads:
    x.join()
