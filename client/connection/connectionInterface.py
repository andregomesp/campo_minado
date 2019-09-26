from client.connection.connection import Connection


def make_connection():
    connection = Connection()
    connection.start_connections(2)
    try:
        while True:
            events = connection.selector.select(timeout=1)
            if events:
                for key, mask in events:
                    connection.service_connection(key, mask)
            if not connection.selector.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        connection.selector.close()
