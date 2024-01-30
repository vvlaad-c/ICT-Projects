import socket

HOST = "127.0.0.1"
PORT = 65432

# Defining function for sendim messages
def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(message.encode("utf-8"))

# Defining function to retreive messages
def retrieve_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"RETRIEVE")
        data = client_socket.recv(1024)
        return data.decode("utf-8")
