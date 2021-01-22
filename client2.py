import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

DISCONNECT_MESSAGE = "!DISCONNECT"

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((HOST, PORT))

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (1024 - len(send_length))
    CLIENT.send(send_length)
    CLIENT.send(message)
    print(CLIENT.recv(2048).decode('utf-8'))

send("Hello World!")