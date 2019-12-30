"""
server-side for simple chat on python
"""

import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 5000))
server.listen(100)

list_of_clients = []


def clientthread(conn, addr):
    conn.send(("Welcome to this chatroom!").encode())

    while True:
        try:
            message = conn.recv(2048)
            print(f"<{addr}>", message.decode())

            if message:
                message_to_send = f"{addr}".encode() + b">> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except socket.error as err:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except socket.error as err:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)
    print(addr, " connected")

    thr = threading.Thread(target=clientthread, args=(conn, addr))
    thr.start()

conn.close()
server.close()
