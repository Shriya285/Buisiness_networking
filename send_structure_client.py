import socket

class MyStruct:
    def __init__(self, name, userId, password):
        self.name = name
        self.userId = userId
        self.password = password

def main():
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if sockfd < 0:
        print("Socket not created")
        exit(0)
    else:
        print("Socket Created")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('localhost', 3050))
    print("Connection Successful")

    myst = MyStruct("", 0, "")

    print("Enter userId: ")
    myst.userId = int(input())
    print("Enter password: ")
    myst.password = input()

    server.sendall(str(myst.__dict__).encode())

    message = server.recv(1024).decode()

    print(message)

    server.close()

if __name__ == "__main__":
    main()
