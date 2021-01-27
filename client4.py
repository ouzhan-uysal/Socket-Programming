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
    with open('received_file.json', 'wb') as f:
        print('file opened')
        while True:
            #print('receiving data...')
            data = s.recv(BUFFER_SIZE)
            print('data=%s', (data))
            if not data:
                f.close()
                print('file close()')
                break
            # write data to a file
            f.write(data)

    print('Successfully get the file')
    s.close()
    print('connection closed')

def doNothing():
    sys.exit(0)

if __name__ == "__main__":
    while True:
        i = input("Enter the action you want to take: \n 1. Check File \n 2. Do Nothing \n Chooise: ")
        if i == 1:
            createFile()
            break
        elif i == 2:
            doNothing()
            break
        elif i == 'q':
            sys.exit(0)
        else:
            print("Choose one of the actions shown. Or press 'q' to exit.")