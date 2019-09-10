from server.connection.connection import Connection


def main_loop():
    print("Welcome to minefield")
    print("Starting server interface")
    connection = Connection()
    connection.create_socket()
    while True:
        events = connection.selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                connection.accept_wrapper(key.fileobj)
            else:
                connection.service_connection(key, mask)


main_loop()
