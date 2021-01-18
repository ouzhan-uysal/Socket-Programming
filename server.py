import socket 

HEADERSIZE = 10

s = socket.socket()
port = 1234
s.bind((socket.gethostname(), port))      # bind() method: Specific ip and port so that it can listen to incoming requests on that ip and port.
print(f"Socket binded to {port}")

s.listen(5)     # 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
print("Socket is listening.")

while True:
    clientSocket, addr = s.accept()    # Establish connection with client
    print(f"Got connection from {addr}")

    msg = "Welcome to the server!"
    print(f"{len(msg):<{HEADERSIZE}}"+msg)

    clientSocket.send(bytes(msg, "utf-8"))
    clientSocket.close()