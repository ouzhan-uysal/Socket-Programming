import socket 

s = socket.socket()

port = 12345

s.bind(("", port))      # bind() method: Specific ip and port so that it can listen to incoming requests on that ip and port.
print(f"Socket binded to {port}")

s.listen(5)     # 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
print("Socket is listening.")

while True:
    c, addr = s.accept()    # Establish connection with client
    print(f"Got connection from {addr}")

    c.send("Thank you for connection")
    c.close