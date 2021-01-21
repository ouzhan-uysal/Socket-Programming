import socket
import threading

MSG_BYTE = 64

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (SERVER, PORT)

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# socket.socket().listen(5)   # 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.

def handler_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(MSG_BYTE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}]: {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING]: Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handler_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")

print("[STARTING]: Server is starting...")
start()