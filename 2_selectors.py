import socket
import selectors

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8090))
    server_socket.listen()

    selector.register(fileobj=server_socket,events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f"connection from {addr}")

    selector.register(fileobj=client_socket,events=selectors.EVENT_READ, data=accept_connection)

def send_message(client_socket):
    data_from_client = client_socket.recv(2048)
    if data_from_client:
        response = 'Hello, i recieve data from you!'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
       pass


event_loop()
