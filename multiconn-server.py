import socket
import selectors

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

sel = selectors.DefaultSelector()
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Listening on {HOST, PORT}")
lsock.setblocking(False)    # 
sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key, fileobj)
        else:
            service_connection(key, mask)