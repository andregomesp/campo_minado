import socket
import selectors
import types


class Connection:
    host: str = "127.0.0.1"
    port: int = 2045
    selector: selectors
    messages = [b'Message 1 from client.', b'Message 2 from client.']

    def start_connections(self, num_conns):
        self.selector = selectors.DefaultSelector()
        server_addr = (self.host, self.port)
        for i in range(0, num_conns):
            connid = i + 1
            print('starting connection', connid, 'to', server_addr)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)
            sock.connect_ex(server_addr)
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            data = types.SimpleNamespace(connid=connid,
                                         msg_total=sum(len(m) for m in self.messages),
                                         recv_total=0,
                                         messages=list(self.messages),
                                         outb=b'')
            self.selector.register(sock, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                print('received', repr(recv_data), 'from connection', data.connid)
                data.recv_total += len(recv_data)
            if not recv_data or data.recv_total == data.msg_total:
                print('closing connection', data.connid)
                self.selector.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)
            if data.outb:
                print('sending', repr(data.outb), 'to connection', data.connid)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]
