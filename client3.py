import socket, sys, json
# from cPickle as pickle

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((TCP_IP, TCP_PORT))
except ConnectionRefusedError as err:
    print(f"[SERVER NOT ACTIVE]: Error: {err}")
    sys.exit(0)

def createFile():
    json_file = open('ServerAccessKey.json', 'rb')
    json_data = json_file.read()
    s.send(json_data)
    with open('received_file.json', 'wb') as f:
        try:
            while True:
                data = s.recv(BUFFER_SIZE)
                if not data:
                    f.close()
                    break
                f.write(data)

        except ConnectionResetError as err:
            print(f"Server is inactive. Program is closing..")
            sys.exit(0)

    s.close()
    print('connection closed')

def doNothing():
    s.send("boş yap".encode('utf-8'))
    
    with open('received_file.json', 'wb') as f:
        try:
            while True:
                data = s.recv(BUFFER_SIZE)
                if not data:
                    f.close()
                    break
                f.write(data)

        except ConnectionResetError as err:
            print(f"Server is inactive. Program is closing..")
            sys.exit(0)

    s.close()
    print('connection closed')

def sendMsg():
    s.send('Hello World'.encode('utf-8'))
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        data = s.recv(BUFFER_SIZE)
    s.close
    print('connection closed')
            

if __name__ == "__main__":
    while True:
        chooise = input(
            " Enter the action you want to take:"+
            "\n 1. Check File"+
            "\n 2. Do Nothing"+
            "\n 3. Send Message"+
            "\n 4. Exit"+
            "\n Chooise: ")
        if chooise == '1':
            createFile()
            break
        elif chooise == '2':
            doNothing()
            break
        elif chooise == '3':
            sendMsg()
            break
        elif chooise == '4':
            sys.exit(0)
        else:
            print("Choose one of the actions shown.")