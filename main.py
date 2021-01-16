import socket
import sys

s = socket.socket()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"Socket creation failed with error: {err}")

# Default port for socket
port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror as err:
    print(f"There was an error resolving the host. Error: {err}")
    sys.exit()

# Connection
s.connect((host_ip, port))  # This must in pair parenthesis

