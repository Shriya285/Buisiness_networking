import socket
import os

PORT = 4444
SERVER_ADDR = "127.0.0.1"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDR, PORT))
print("[+]Server Socket is created.")

server_socket.listen(10)
print("[+]Listening....")

while True:
    new_socket, addr = server_socket.accept()
    print(f"Connection accepted from {addr[0]}:{addr[1]}")

    child_pid = os.fork()

    if child_pid == 0:
        server_socket.close()

        while True:
            data = new_socket.recv(1024).decode()
            if data == ":exit":
                print(f"Disconnected from {addr[0]}:{addr[1]}")
                break
            else:
                print(f"Client: {data}")
                new_socket.send(data.encode())
                data = ""

        new_socket.close()
        exit()

server_socket.close()
