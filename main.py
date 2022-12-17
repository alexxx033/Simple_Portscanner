import socket
import os
import sys

from datetime import datetime

os.system('cls')
sadcaf
remoteServer = input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

print("_") * 60
print("Please wait, scanning remote host"), remoteServerIP
print("_") * 60

time1 = datetime.now()

try:
    for port in range(1, 5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
        print("Port {}:          Open").format(port)
        sock.close()

except KayboardInterrupt:
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
