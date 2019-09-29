from server.connection.connection import Connection
from server.domain.board import Board


def main_loop():
    print("Welcome to minefield")
    print("Starting server interface")
    connection = Connection()
    connection.create_socket()
    board = Board()
    board.populate_map(5, 8)
    while True:
        events = connection.selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                connection.accept_wrapper(key.fileobj)
            else:
                connection.service_connection(key, mask, board)


main_loop()
