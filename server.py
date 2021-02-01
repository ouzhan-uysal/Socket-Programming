# Multi Threading TCP File Transfer

import socket, threading, logging, time, json

TCP_HOST = socket.gethostbyname(socket.gethostname())
TCP_PORT = 9001
BUFFER_SIZE = 1024

TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
TCP_SOCKET.bind((TCP_HOST, TCP_PORT))
TCP_SOCKET.listen(5)

# Read access_keys
access_keys = []
with open('serverFile/access_keys.json') as ak_file:
    data = json.load(ak_file)
    for i in range(len(data["accessToken"])):
        access_keys.append(data[f"accessToken"][i]["private_key"])
    # for key, value in data["accessToken"][1].items():
    #     print(f"{key}: {value}")
    # print(data["accessToken"]["private_key"])
    # access_keys.append(data)
# print(access_keys)


class TCP_SERVER(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print(f"[NEW CONNECTION]: Got connection from {addr}")

    def checkFile(self):
        logging.debug(f"[{self.addr}]: make a checkFile request.")
        filename='serverFile/GoodBye.json'
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
        
        print(f"[DISCONNECT]: {addr} disconnected.")
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 2}\n")
        

    def doNothing(self):
        # logging.debug(f"[{self.addr}]: make a doNothing request.")
        filename='serverFile/GoodBye.json'
        f = open(filename, 'rb')
        len_data = f.read(BUFFER_SIZE)
        while len_data:
            try:
                len_data = f.read(BUFFER_SIZE)
                # data = self.conn.recv(BUFFER_SIZE)
                # if data:
                #     data = int(data)
                #     msg = self.conn.recv(data).decode('utf-8')

                #     print(f"[{addr}]:{msg}")
                #     self.conn.send(data.encode('utf-8'))
                # else:
                #     break

            except ConnectionResetError as err:
                print(f"[DISCONNECT]: {addr} disconnected.")
                print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 2}")
                break
        f.close()
        self.conn.send('\nThank you for connecting'.encode('utf-8'))
        self.conn.close()
        
        print(f"[DISCONNECT]: {addr} disconnected.")
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 2}\n")

    def redirectToExit(self):
        pass
        # logging.debug(f"[{self.addr}] is redirecting to exit.")
        # self.conn.send('Thanks for the connection. Goodbye now.'.encode('utf-8'))
        # self.conn.close()
        # while True:
        #     try:
        #         data = self.conn.recv(BUFFER_SIZE).decode('utf-8')
        #         print(data)
        #         if data:
        #             len_data = int(data)
        #             self.conn.send('Thanks for the connection.'.encode('utf-8'))
        #         else:
        #             break

        #     except (ConnectionResetError, ConnectionAbortedError) as err:
        #         print(f"[DISCONNECT]: {addr} disconnected.")
        #         print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 2}")
        #         break
        # self.conn.close()


if __name__ == "__main__":
    # Registry of logs
    error_handler = logging.FileHandler("logs/ERROR.log")
    debug_handler = logging.FileHandler("logs/DEBUG.log")
    logging.basicConfig(level=logging.DEBUG, handlers=[error_handler, debug_handler], format='[%(levelname)s] Thread:%(threadName)-10s Message:%(message)s')

    
    print("[STARTING]: Server is starting...")
    while True:
        print(f"\n[LISTENING]: Server is listening on {TCP_HOST}\n")
        conn, addr = TCP_SOCKET.accept()
        try:
            data = conn.recv(BUFFER_SIZE)
            data = json.loads(data)
            print(data)
            access_permission = data["private_key"] in access_keys
            if access_permission:
                # Bu kısımdan sonra server client'e hangi işlemi yapması gerektiğini soracak ardından kullanıcının key'İnin yetsini var ise erişimi onaylayacak yoksa erişimi reddedecek.
                if data == 'Check File':
                    threading.Thread(target=TCP_SERVER(conn=conn, addr=addr).checkFile, name="Dosya indirme").start()
                elif data == 'boş yap':
                    threading.Thread(target=TCP_SERVER(conn=conn, addr=addr).doNothing, name="Hiçbir şey yapma").start()
                else:
                    conn.send('Thanks for the connection. Goodbye now.'.encode('utf-8'))
                    conn.close()
                print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")
            else:
                conn.send('Access Denied.'.encode('utf-8'))
                conn.close()
        
        except Exception as err:
            # logging.error(err)
            conn.close()