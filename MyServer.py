import socket
import threading

# Dictionary to keep track of connected clients
Client_sockets_dict = {}
HOST = '138.68.140.83'  # Use '0.0.0.0' to listen on all interfaces
PORT = 5847  # The port that the server will listen on

# Create a TCP socket
Server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server_socket.bind((HOST, PORT))
Server_socket.listen(5)
print("Server is listening on", HOST, ":", PORT)

# Function to handle each client connection
def Handle_client(Client_socket, Client_address):
    try:
        # Receive and store the client's name
        Name = Client_socket.recv(1024).decode()
        Client_sockets_dict[Client_socket] = Name
        print(f"New connection from {Client_address} with name {Name}")

        while True:
            # Receive message from the client
            Data = Client_socket.recv(1024)
            if not Data:
                break

            Message = Data.decode()

            if Message.lower().strip() == 'exit':
                # If client sends 'exit', remove them from the dictionary and close connection
                Client_socket.send(Message.encode())
                Client_sockets_dict.pop(Client_socket)
                break
            else:
                print(f"Received message from {Name}: {Message}")

                # Broadcast the message to all other clients
                for Key in Client_sockets_dict.keys():
                    if Key != Client_socket:
                        Key.send(f"{Name}: {Message}".encode())

    except ConnectionResetError:
        print(f"Connection with {Client_address} closed abruptly.")
    finally:
        # Ensure the client socket is removed and closed
        if Client_socket in Client_sockets_dict:
            Client_sockets_dict.pop(Client_socket)
        Client_socket.close()

# Main loop to accept incoming connections
while True:
    Client_socket, Client_address = Server_socket.accept()
    # Start a new thread to handle each client
    Client_handler = threading.Thread(target=Handle_client, args=(Client_socket, Client_address))
    Client_handler.start()
