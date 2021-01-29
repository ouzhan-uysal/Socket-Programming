import socket

HOST = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 9001        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send('Hello World'.encode('utf-8'))
    # s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', data.decode('utf-8'))

# import socket, sys

# HEADERSIZE = 10

# s = socket.socket()

# try:
#     s.connect((socket.gethostname(), 9001))
# except socket.error as err:
#     print(f"Server aktif değil. Error: {err}")
#     sys.exit(0)

# while True:
#     full_data = ""
#     new_data = True
#     while True:
#         data = s.recv(1024)
#         if new_data:
#             print(f"New message length: {data[:HEADERSIZE]}")
#             datalen = int(data[:HEADERSIZE])
#             new_data = False

#         full_data += data.decode("utf-8")

#         if len(full_data)-HEADERSIZE == datalen:
#             print("full_msg recvd.")
#             print(full_data[HEADERSIZE:])
#             new_data = True

# print(full_data)
