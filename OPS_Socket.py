import socket

class OPS_Socket:
    def __init__(self, sk=None):
        if sk = is None:
            self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sk = sk

    def connect(self, host, port):
        self.sk.connect((host, port))
    
    def sendMsg(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sk.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken.")
            totalsent = totalsent + sent
    
    def receiveMsg(self):
        chunks = []
        byts_recd = 0
        while byts_recd < MSGLEN:
            chunk = self.sk.recv(min(MSGLEN - byts_recd, 2048))
            if chunk == b'':
                raise RuntimeError("Socket connection broken.")
            chunks.append(chunk)
            byts_recd = byts_recd + len(chunk)
        return b''.join(chunks)