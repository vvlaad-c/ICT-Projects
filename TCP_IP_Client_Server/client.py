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


send_message("2:High")
send_message("1:Medium")
send_message("3:Low")

# Retrieve and print messages
for _ in range(3):
    print(retrieve_message())
