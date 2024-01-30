import socket
import queue
import threading

HOST = "127.0.0.1"
PORT = 65432

# Priority queue to store messages
message_queue = queue.PriorityQueue()

# Function to handle client connections
def handle_client(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        message = data.decode("utf-8")
        # Assuming message format: priority_level:message_content
        priority, content = message.split(":", 1)
        priority = int(priority)
        message_queue.put((priority, content))

# Setting up the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Server is listening...")

    while True:
        connection, address = server_socket.accept()
        print(f"Connected to {address}")

        # Handle client connection in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(connection,))
        client_handler.start()
