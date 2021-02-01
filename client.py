import socket, sys, json
# from cPickle as pickle

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 9001
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((TCP_IP, TCP_PORT))
except ConnectionRefusedError as err:
    print(f"[SERVER NOT ACTIVE]: Error: {err}")
    sys.exit(0)

def checkFile():
    with open('userFile/received_file.json', 'wb') as f:
        try:
            while True:
                data = sock.recv(BUFFER_SIZE)
                if not data:
                    f.close()
                    break
                f.write(data)

        except ConnectionResetError as err:
            print(f"Server is inactive. Program is closing..")
            sys.exit(0)

    sock.close()
    print('Connection closed.')

def doNothing():
    with open('userFile/received_file.json', 'wb') as f:
        try:
            while True:
                data = sock.recv(BUFFER_SIZE)
                if not data:
                    f.close()
                    break
                f.write(data)

        except ConnectionResetError as err:
            print(f"Server is inactive. Program is closing..")
            sys.exit(0)

    sock.close()
    print('Connection closed.')

def sendMsg():
    sock.send('Hello World'.encode('utf-8'))
    while True:
        data = sock.recv(BUFFER_SIZE)
        if not data:
            break
        data = sock.recv(BUFFER_SIZE)
    sock.close()
    print('Connection closed.')
            

if __name__ == "__main__":
    json_file = open('userFile/user_key.json', 'rb')
    json_data = json_file.read()
    sock.send(json_data)    # Send json file to server
    choice = input(sock.recv(BUFFER_SIZE).decode('utf-8'))
    sock.send(choice.encode('utf-8'))   # answer server
    while True:
        if choice == '1':
            checkFile()
            sys.exit(0)
        elif choice == '2':
            doNothing()
            sys.exit(0)
        elif choice == '3':
            sys.exit(0)
        else:
            print("Choose one of the actions shown.")