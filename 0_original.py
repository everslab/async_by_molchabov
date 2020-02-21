# В данном коде отображена проблема блокирующих функций
# при запуске данного скрипта , подключаемся через телнет на 127.0.0.1 8090
# мы замыкаемся на цикле ---2
# и если подключиться другим телнетом, то он не подключится т.к. нельзя отработать цикл ---1 без выходи из цикла ---2
# Борьбе с этой задачей будут посвящены следующие файлы
# можно реализовать с помощью
# 1) простыми функциями, событийный цикл
# 2) callback
# 3) генераторы и корутины
# 4) asyncio

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8090))
server_socket.listen()

while True:
    print("---1")
    client_socket, addr = server_socket.accept()
    print(f"connection from {addr}")

    while True:
        print("---2")
        data_from_client = client_socket.recv(2048)

        if not data_from_client:
            break
        else:
            response = 'Hello, i recieve data from you!'.encode()
            client_socket.send(response)
    client_socket.close()
