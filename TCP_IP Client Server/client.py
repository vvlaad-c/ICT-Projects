import socket

HOST = "127.0.0.1"
PORT = 65432

# Setting up the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    # Connecting to the specified host and port
    socket.connect(HOST, PORT)
    # Exchanging data
    socket.sendall(b"Test")
    data = socket.recv(1024)

print(f"Received {data}")