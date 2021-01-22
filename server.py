import socket

HOST = socket.gethostbyname(socket.gethostname())   # Standard loopback interface address (localhost)
PORT = 1234 # Port to listen on (non-privileged ports are > 1023)
ADDR = (HOST, PORT)

FORMAT = "utf-8"
MSG_BYTE = 1024
DISCONNECT_MESSAGE = "!DISCONNECT"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # We don't need to call the s.close () function with the "with" statement.
    s.bind((HOST, PORT))
    s.listen()  # if parameter is 5. 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.

    conn, addr = s.accept()
    with conn:
        print(f"Connection by {addr}")
        while True:
            data = conn.recv(MSG_BYTE)
            if not data:
                break
            conn.sendall(data)
    