import socket

tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8090))
    server_socket.listen()

    while True:
        #yield ('read', server_socket)
        client_socket, addr = server_socket.accept() # блокирующая операция на read
        print(f"connection from {addr}")
        client(client_socket)

def client(client_socket):
    while True:
        #yield ('read', client_socket)
        data_from_client = client_socket.recv(2048) # блокирующая операция на read

        if not data_from_client:
            break
        else:
            response = 'Hello, i recieve data from you!'.encode()
            #yield ('write', client_socket)
            client_socket.send(response) # блокирующая операция на write
    client_socket.close()


# def event_loop():
#     while any[(tasks, to_read, to_write)]:
#         while not tasks:
#             ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
#
# tasks.append(server())

server()
