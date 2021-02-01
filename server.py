# Multi Threading TCP File Transfer

import socket, threading, logging, time, json

TCP_HOST = socket.gethostbyname(socket.gethostname())
TCP_PORT = 9001
BUFFER_SIZE = 1024

TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
TCP_SOCKET.bind((TCP_HOST, TCP_PORT))
TCP_SOCKET.listen(5)

# Read access_keys and permissions
access_keys = {}
with open('serverFile/access_keys.json') as ak_file:
    data = json.load(ak_file)
    for i in range(len(data["accessToken"])):
        key = data[f"accessToken"][i]["private_key"]
        value = data[f"accessToken"][i]["permission"]
        access_keys[key] = value

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
        self.conn.close()
        

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
            data = conn.recv(BUFFER_SIZE)   # Client'ten gelen json dosyası
            data = json.loads(data)         # Json dosyasının okunması
            access_permission = data["private_key"] in access_keys
            # Kullanıcının private_key'i kontrol edilir ona göre yetki verilir.
            if access_permission:
                # Burada kullanıcıya yapmak istediği işlem sorulur. Eğer istediği işleme private_key'inin yetkisi varsa işlem yapılır yoksa tekrar sorulur veya bağlantı kesilir.
                conn.send("Make your choice.\n1. Check File\n2. doNothing\n3. Exit\n\nYour Choice: ".encode("utf-8"))   # ask client
                choice = int(conn.recv(BUFFER_SIZE).decode('utf-8'))
                # print(f"Kullanıcının Seçimi: {choice}")
                access_authority = choice in access_keys[data["private_key"]]
                
                if choice == 1 and access_authority:
                    threading.Thread(target=TCP_SERVER(conn=conn, addr=addr).checkFile, name="Dosya indirme").start()

                elif choice == 2 and access_authority:
                    threading.Thread(target=TCP_SERVER(conn=conn, addr=addr).doNothing, name="Hiçbir şey yapma").start()

                elif choice == 3 and access_authority:
                    conn.send('Thanks for the connection. Goodbye now.'.encode('utf-8'))
                    conn.close()

                else:
                    conn.send('Access Denied.'.encode('utf-8'))
                    conn.close()

                print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")

            else:
                conn.send('Access Denied.'.encode('utf-8'))
                conn.close()

        except Exception as err:
            # logging.error(err)
            conn.close()