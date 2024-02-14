import socket

PORT = 4444
SERVER_ADDR = "127.0.0.1"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((SERVER_ADDR, PORT))
print("[+]Connected to Server.")

while True:
    message = input("Client: \t")
    clientSocket.send(message.encode())

    if message == ":exit":
        clientSocket.close()
        print("[-]Disconnected from server.")
        break

    data = clientSocket.recv(1024).decode()
    if not data:
        print("[-]Error in receiving data.")
    else:
        print("Server: \t", data)
