# wSScan - a simple web server info scanner
# Version: 0.1
# Date: 05/08/2019
# Country: Argentina
#
# c0ded by spider0ne

import socket
import sys  

# Check if host/ip is valid
def ip_valida(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  
        return False
    return True

# Branding banner
def banner():
    print color.BOLD
    print "            _____ _____                 "
    print "           / ____/ ____|                "
    print " __      _| (___| (___   ___ __ _ _ __  "
    print " \ \ /\ / /\___ \ \__ \ / __/ _` | '_ \ "
    print "  \ V  V / ____) |___) | (_| (_| | | | |"
    print "   \_/\_/ |_____/_____/ \___\__,_|_| |_|"
    print color.END
    print color.BOLD + "wSScan" + color.END + " -simple web server info scanner"
    print "Version: " + color.BOLD + version + color.END
    print "                                        "

# Terminal colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   YELLOW_BLINK = '\033[93;5m' 
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Number of version
version = "0.1"


# Check for arguments
if len (sys.argv) != 2 :
    banner()
    print color.BOLD + "Usage: " + color.END + sys.argv[0] + color.BOLD + " <" + color.END + "HOST/IP" + color.BOLD + ">" + color.END
    print "\nC0ded by " + color.BOLD + color.UNDERLINE + "spider0ne" + color.END + "\n"
    sys.exit (1)

# Web server port and address 
port = 80
host = sys.argv[1]

# Banner 
banner()

# create socket
print color.GREEN + "# Attempting to connect..." + color.END
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print color.GREEN + "# " + color.RED + "Failed to connect!" + color.END
    sys.exit()

print color.GREEN + "# Getting remote IP address" + color.END

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print color.GREEN + "# " + color.RED + "Hostname could not be resolved!" + color.END
    print "\nC0ded by " + color.BOLD + color.UNDERLINE + "spider0ne" + color.END + "\n"
    sys.exit()

# Connect to remote server
print color.GREEN + "# " + color.YELLOW_BLINK + "Connecting to server" + color.END
print color.BOLD + "  -Hostname: " + color.END + host
print color.BOLD + "  -IP Address: " + color.END + remote_ip + "\n"
s.connect((remote_ip , port))

# Send data to remote server
request = "HEAD / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print color.GREEN + "# " + color.RED + "Failed to connect!" + color.END
    sys.exit()

# Receive data
print color.GREEN + "# Receiving data from server\n" + color.END
reply = s.recv(4096)

# Show data except the header
print color.BOLD + "[DATA from WEBSERVER on " + color.UNDERLINE + host + color.BOLD + "]" + color.END
i = reply.index('\n')
data = reply[i+1:].replace("Connection: close", '', -1).rstrip()
print "".join([s for s in data.splitlines(True) if s.strip()])
print color.BOLD + "[END OF DATA]\n" + color.END
print "C0ded by " + color.BOLD + color.UNDERLINE + "spider0ne" + color.END + "\n"

