import socket
# import os
import sys
import nmap

from datetime import datetime

nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"
nmap.PortScanner(nmap_search_path=nmap_path)

# os.system('clear')
print('\033c')

### NMAP starts here ###
nm = nmap.PortScanner()
nm.scan = input("Enter a IP to scan:")

for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' %
                  (port, nm[host][proto][port]['state']))
### NMAP stops here ###

#remoteServer = input("Enter a remote host to scan:")
#start_port = int(input("Enter start port: "))
#end_port = int(input("Enter end port: "))
#remoteServerIP = socket.gethostbyname(remoteServer)

print("_"*60)
print("Please wait, scanning remote host", remoteServerIP)
print("_"*60)

time1 = datetime.now()

try:

    total_ports = end_port - start_port + 1
    count = 0
    for port in range(start_port, end_port + 1):
        count += 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()
        print("Checked {} of {} ports".format(count, total_ports))


except socket.error as err:
    print("Socket creation failed with error %s" % (err))

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

time2 = datetime.now()

total = time2 - time1

print("Scanning Completed in"), total
