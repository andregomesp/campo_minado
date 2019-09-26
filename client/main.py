from client.connection.connectionInterface import make_connection


def main():
    print("Welcome to minefield")
    print("Starting client interface")
    messages = [b'oi']
    make_connection(messages)


main()
