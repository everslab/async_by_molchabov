# Решение простыми функциями

# 1) рефакторим код в виде функций
# import socket
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(("127.0.0.1", 8090))
# server_socket.listen()
#
#
# def accept_connection(server_socket):
#     while True:
#         client_socket, addr = server_socket.accept()
#         print(f"connection from {addr}")
#         send_message(client_socket)
#
#
# def send_message(client_socket):
#     while True:
#         data_from_client = client_socket.recv(2048)
#
#         if not data_from_client:
#             break
#         else:
#             response = 'Hello, i recieve data from you!'.encode()
#             client_socket.send(response)
#
#     client_socket.close()
#
#
# accept_connection(server_socket)


# 2) отвяжем фунции друг от друга
import socket
from select import select# работает с файловыми обьектами, понимает что они изменены

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8090))
server_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f"connection from {addr}")
    to_monitor.append(client_socket)

def send_message(client_socket):
    data_from_client = client_socket.recv(2048)
    if data_from_client:
        response = 'Hello, i recieve data from you!'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        #функция select возворащаеть обьекты готовые к чтению, готовые к записи и буферная переменная для хранения последнего вывода
        #передаем туда то что мониторить для чтения , для записи и ошибки
        ready_ro_read, _, _ = select(to_monitor, [], [])

        for sock in ready_ro_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


to_monitor.append(server_socket)
event_loop()
