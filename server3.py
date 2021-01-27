# Sunucuya Dosya gönderme

import socket

PORT = 9001
s = socket.socket()
HOST = socket.gethostbyname(socket.gethostname())
s.bind((HOST, PORT))
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='ServerAccessKey.json'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('\nThank you for connecting'.encode('utf-8'))
    conn.close()