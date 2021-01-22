import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

def handler_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")
    
    connected = True
    while connected:
        data = conn.recv(1024).decode('utf-8')

        if not data:
            break

        data = int(data)
        msg = conn.recv(data).decode('utf-8')

        print(f"[{addr}]:{msg}")
        conn.send(data.encode('utf-8'))

    conn.close()



if __name__ == "__main__":
    print("[STARTING]: Server is starting...")
    SERVER.listen(5)    # 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
    print(f"[LISTENING]: Server is listening on {HOST}")
    while True:
        conn, addr = SERVER.accept()
        threading.Thread(target=handler_client, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")