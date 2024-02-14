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
    server.bind(('localhost', 3050))
    print("Bind Successful")

    server.listen(5)
    client, addr = server.accept()
    print(f"Connection from {addr}")

    my_struct_array = [
        MyStruct("nikhil1", 1, "nikhil1"),
        MyStruct("nikhil2", 2, "nikhil2"),
        MyStruct("nikhil3", 3, "nikhil3"),
        MyStruct("nikhil4", 4, "nikhil4"),
        MyStruct("nikhil5", 5, "nikhil5")
    ]

    myst = MyStruct("", 0, "")

    data = client.recv(1024)
    myst.__dict__ = data.decode()

    print(f"userId received: {myst.userId}")
    print(f"password received: {myst.password}")

    login_success = False
    for user in my_struct_array:
        if myst.userId == user.userId and myst.password == user.password:
            login_success = True
            break

    if login_success:
        message = "Login Successful\n"
    else:
        message = "Login Failure\n"

    client.send(message.encode())

    client.close()
    server.close()

if __name__ == "__main__":
    main()
