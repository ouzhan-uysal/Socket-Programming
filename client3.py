import socket, sys

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
    s.send("Check File".encode('utf-8'))
    with open('received_file.json', 'wb') as f:
        print('file opened')
        try:
            while True:
                data = s.recv(BUFFER_SIZE)
                # print(f'data={data}')
                if not data:
                    f.close()
                    break
                # write data to a file
                f.write(data)

        except ConnectionResetError as err:
            print(f"Server is inactive. Program is closing..")
            sys.exit(0)

    print('Successfully get the file')
    s.close()
    print('connection closed')

def doNothing():
    s.send("boş yap".encode('utf-8'))
    sys.exit(0)

if __name__ == "__main__":
    while True:
        chooise = input(
            " Enter the action you want to take:"+
            "\n 1. Check File"+
            "\n 2. Do Nothing"+
            "\n 3. Exit"+
            "\n Chooise: ")
        if chooise == '1':
            createFile()
            break
        elif chooise == '2':
            doNothing()
            break
        elif chooise == '3':
            sys.exit(0)
        else:
            print("Choose one of the actions shown.")