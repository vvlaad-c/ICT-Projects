import socket

# Setting up the host and the port
HOST = "127.0.0.1"
PORT = 65432

# Setting up the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    # Binding the socket to the host and the port
    socket.bind((HOST, PORT))
    # Listening for requests
    socket.listen()
    conection, address = socket.accept()

    # Exchanging data
    with conection:
        print("Connected")
        while True:
            data = conection.recv(1024)
            if not data:
                break
            else:
                conection.sendall(data)
