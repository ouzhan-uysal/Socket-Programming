# multi threading tcp file transfer

import socket
import threading

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 9001
BUFFER_SIZE = 1024

class ClientThread(Thread):
    def __init__(self, IP, PORT, SOCK):
        threading.Thread.__init__(self)
        self.IP = IP
        self.PORT = PORT
        self.SOCK = SOCK
        print("New thread started for " + IP + ":" + str(PORT))

    def run(self):
        filename='ServerAccessKey.json'
        f = open(filename, 'rb')
        while True:
            data = f.read(BUFFER_SIZE)
            while (data):
                self.SOCK.send(data)
                #print('Sent ',repr(data))
                data = f.read(BUFFER_SIZE)
            if not data:
                f.close()
                self.SOCK.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (CONN, (IP,PORT)) = tcpsock.accept()
    print('Got connection from ', (IP, PORT))
    newthread = ClientThread(IP, PORT, CONN)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()