import socket
import selectors
import types


class Connection:
    host: str = "0.0.0.0"
    port: int = 2045
    selector = None

    def __init__(self):
        self.selector = selectors.DefaultSelector()

    def create_socket(self):
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.bind((self.host, self.port))
        new_socket.listen()
        print("---Listening on---", (self.host, self.port))
        new_socket.setblocking(False)
        self.selector.register(new_socket, selectors.EVENT_READ, data=None)

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()
        print('Accepted connection from', addr)
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.selector.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print('closing connection to', data.addr)
                self.selector.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print('echoing', repr(data.outb), 'to', data.addr)
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]
