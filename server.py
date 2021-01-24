import socket, threading, time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
BUFFER_SIZE = 1024

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

def handler_client(conn, addr):
    print(f"[NEW CONNECTION]: {addr} connected.")
    
    while True:
        try:
            data = conn.recv(BUFFER_SIZE)
            if data:
                data = int(data)
                msg = conn.recv(data).decode('utf-8')

                print(f"[{addr}]:{msg}")
                conn.send(data.encode('utf-8'))
            else:
                break

        except ConnectionResetError as err:
            print(f"[DISCONNECT]: {addr} disconnected.")
            print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 2}")
            break

    conn.close()


if __name__ == "__main__":
    print("[STARTING]: Server is starting...")
    SERVER.listen(5)
    print(f"[LISTENING]: Server is listening on {HOST}")
    while True:
        conn, addr = SERVER.accept()
        threading.Thread(target=handler_client, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")