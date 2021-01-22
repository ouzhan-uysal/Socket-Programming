import socket, threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def handler_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")

    connected = True
    while connected:
        data = conn.recv(1024).decode('utf-8')
        if data:
            data = int(data)
            msg = conn.recv(data).decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}]: {msg}")
            conn.send("Msg received".encode('utf-8'))

    conn.close()


if __name__ == "__main__":
    print("[STARTING]: Server is starting...")
    server.listen() # if parameter is 5. 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
    print(f"[LISTENING]: Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handler_client, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")