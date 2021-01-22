import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handler_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")
    
    connected = True
    while connected:
        data = conn.recv(1024).decode('utf-8')
        

if __name__ == "__main__":
    with SERVER as s:
        print("[STARTING]: Server is starting...")
        s.bind((HOST, PORT))
        s.listen(5)  # 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
        print(f"[LISTENING]: Server is listening on {HOST}")
        
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handler_client, args=(conn, addr)).start()
            print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")