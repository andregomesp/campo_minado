import socket
import selectors


class Connection:
    host: str
    port: str = "2045"

    def create_socket(self):
        selector = selectors.DefaultSelector()
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.bind((self.host, self.port))
        new_socket.listen()
        print("---Listening on---", (self.host, self.port))
        new_socket.setblocking(False)
        selector.register(new_socket, selectors.EVENT_READ, data=None)


