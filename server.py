import socket, threading, time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

def handler_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")
    
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if data:
                data = int(data)
                msg = conn.recv(data).decode('utf-8')

                print(f"[{addr}]:{msg}")
                conn.send(data.encode('utf-8'))
            else:
                break

        except ConnectionResetError as err:
            print(f"[DISCONNECT]: {addr}")
            break

    conn.close()


if __name__ == "__main__":
    print("[STARTING]: Server is starting...")
    SERVER.listen(5)    # 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
    print(f"[LISTENING]: Server is listening on {HOST}")
    while True:
        conn, addr = SERVER.accept()
        threading.Thread(target=handler_client, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")
        time.sleep(3)