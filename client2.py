import socket                

s = socket.socket()          

host = socket.gethostbyname(socket.gethostname())
port = 9001

try:
    s.connect((host, port))
except ConnectionRefusedError as err:
    print(f"Server aktif değil. Error: {err}")

try:
    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))

    s.close()
    
except socket.error as msg:
    print("[Server aktif değil.] Mesaj:", msg)