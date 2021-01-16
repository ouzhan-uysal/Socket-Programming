import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

print(s.recv(1024)) # receive data from the server
s.close()   # close the connection