import socket, sys

HEADERSIZE = 10

s = socket.socket()

try:
    s.connect((socket.gethostname(), 9001))
except socket.error as err:
    print(f"Server aktif değil. Error: {err}")
    sys.exit(0)

while True:
    full_msg = "jamiryoo"
    new_msg = True
    while True:
        msg = s.recv(1024)
        if new_msg:
            print(f"New message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full_msg recvd.")
            print(full_msg[HEADERSIZE:])
            new_msg = True

print(full_msg)