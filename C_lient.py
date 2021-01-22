import socket

MSG_BYTE = 1024
HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Sa Hacılar!')
    data = s.recv(MSG_BYTE)

print(f"Received {repr(data)}")