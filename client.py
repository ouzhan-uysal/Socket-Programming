import socket

HEADERSIZE = 10

s = socket.socket()
s.connect((socket.gethostname(), 1234)) # First Parameter: localhost, Second Parameter: port

while True:
    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(16)  # receive data from the server
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