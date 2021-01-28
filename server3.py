# multi threading tcp file transfer

import socket, threading, logging, time

TCP_HOST = socket.gethostbyname(socket.gethostname())
TCP_PORT = 9001
BUFFER_SIZE = 1024

TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
TCP_SOCKET.bind((TCP_HOST, TCP_PORT))
threads = []    # 1. Nesil kullanıyor

# --- 1. Nesil ---
# class ClientThread(threading.Thread):
#     def __init__(self, ADDR, SOCK):
#         threading.Thread.__init__(self)
#         self.IP = IP
#         self.PORT = PORT
#         self.SOCK = SOCK
#         print(f"[NEW CONNECTION]: Got connection from {ADDR}")

#     def run(self):
#         filename='ServerAccessKey.json'
#         f = open(filename, 'rb')
#         while True:
#             data = f.read(BUFFER_SIZE)
#             while data:
#                 self.SOCK.send(data)
#                 #print('Sent ',repr(data))
#                 data = f.read(BUFFER_SIZE)
#             if not data:
#                 f.close()
#                 self.SOCK.close()
#                 break

# if __name__=="__main__":
#     print("[STARTING]: Server is starting...")
#     while True:
#         TCP_SOCKET.listen(5)
#         print("Waiting for incoming connections...")
#         (CONN, ADDR) = TCP_SOCKET.accept() # ADDR == (IP,PORT)
#         print('Got connection from ', ADDR)
#         newthread = ClientThread(ADDR, CONN)
#         newthread.start()
#         threads.append(newthread)

#     for t in threads:
#         t.join()



# --- 2. Nesil ---
# def handler_client(conn, addr):
#     print(f"[NEW CONNECTION]: Got connection from {addr}")
#     filename='ServerAccessKey.json'
#     f = open(filename, 'rb')
#     while True:
#         try:
#             data = f.read(BUFFER_SIZE)
#             while data:
#                 conn.send(data)
#                 # print(f"Sent {repr(data)}")
#                 data = f.read(BUFFER_SIZE)
#             if not data:
#                 f.close()
#                 conn.close()
#                 break

#         except Exception as err:
#             print(err)

# if __name__ == "__main__":
#     print("[STARTING]: Server is starting...")
#     TCP_SOCKET.listen(5)
#     while True:
#         print(f"\n[LISTENING]: Server is listening on {TCP_HOST}")
#         conn, addr = TCP_SOCKET.accept()     # addr == (IP, PORT)
#         threading.Thread(target=handler_client, args=(conn, addr)).start()
#         print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")



# --- 3. Nesil
class TCP_SERVER(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print(f"[NEW CONNECTION]: Got connection from {addr}")

    def checkFile(self):
        filename='ServerAccessKey.json'
        f = open(filename, 'rb')
        while True:
            data = f.read(BUFFER_SIZE)
            while data:
                self.conn.send(data)
                data = f.read(BUFFER_SIZE)
            if not data:
                f.close()
                self.conn.close()
                break

    def doNothing(self):
        print("Do Nothing")
        # while True:
        #     data = self.conn.recv(BUFFER_SIZE)
        #     if data:
        #         data = int(data)
        #         msg = conn.recv(data).decode('utf-8')
        #         print(f"[{self.addr}]: {msg}")
        #         conn.send(data.encode('utf-8'))
        #     else:
        #         break
        # conn.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] Thread:%(threadName)-10s Message:%(message)s')
    print("[STARTING]: Server is starting...")
    TCP_SOCKET.listen(5)
    while True:
        print(f"\n[LISTENING]: Server is listening on {TCP_HOST}\n")
        conn, addr = TCP_SOCKET.accept()
        data = conn.recv(BUFFER_SIZE).decode('utf-8')
        if data == 'Check File':
            threading.Thread(target=TCP_SERVER(conn=conn, addr=addr).checkFile, name="Dosya indirme", daemon=True).start()
        elif data == 'boş yap':
            threading.Thread(target=TCP_SERVER(conn=conn, addr=addr).doNothing, name="Hiçbir şey yapma", daemon=True).start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")