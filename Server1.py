#Server.py

import socket 
import threading 
 
clients = []   
client_names = {}   
 
def handle_client(client_socket): 
    name = client_socket.recv(1024).decode('utf-8') 
    client_names[client_socket] = name 
    print(f"{name} has joined the chat!") 
    broadcast(f"{name} has joined the chat!", client_socket) 
     
    while True: 
        try: 
            data = client_socket.recv(1024) 
            if not data: 
                break 
            message = data.decode('utf-8')
            
            print(f"Received message from {name}: {message}") 
            broadcast(f"{name}: {message}", client_socket) 
        except: 
            clients.remove(client_socket) 
            broadcast(f"{name} has left the chat.", client_socket) 
            break 
    client_socket.close() 
 
def broadcast(message, sender_socket): 
    for client in clients: 
        if client != sender_socket: 
            try: 
                client.sendall(message.encode('utf-8')) 
            except: 
                clients.remove(client) 
 
def main(): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = 'localhost' 
    port = 9999 
    server_socket.bind((host, port)) 
    server_socket.listen(5) 
    print(f"Server listening on {host}:{port}") 
 
    while True: 
        client_socket, client_address = server_socket.accept() 
        clients.append(client_socket)  
        print(f"Accepted connection from {client_address}") 
        client_handler = threading.Thread(target=handle_client, args=(client_socket,)) 
        client_handler.start() 
 
if __name__ == "__main__": 
    main()
# - `server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`: Creates a new socket using IPv4 addressing and TCP protocol.
# - `host = 'localhost'`: Sets the server to listen on the local machine.
# - `port = 9999`: Defines the port number the server will listen on.
# - `server_socket.bind((host, port))`: Binds the socket to the specified host and port.
# - `server_socket.listen(5)`: Starts listening for incoming connections with a backlog of 5.
# - `print(f"Server listening on {host}:{port}")`: Outputs a message indicating the server is running and listening.
# - `while True:`: Begins an infinite loop to continuously accept new clients.
# - `client_socket, client_address = server_socket.accept()`: Waits for a new client to connect and retrieves the client's socket and address.
# - `clients.append(client_socket)`: Adds the new client's socket to the list of connected clients.
# - `print(f"Accepted connection from {client_address}")`: Logs the client's address upon successful connection.
# - `client_handler = threading.Thread(target=handle_client, args=(client_socket,))`: Creates a new thread to handle the connected client.
# - `client_handler.start()`: Starts the client handler thread to manage communication.
# - `def broadcast(message, sender_socket):`: Defines a function to send messages to all clients except the sender.
# - `for client in clients:`: Iterates through all connected clients.
# - `if client != sender_socket:`: Checks that the client is not the sender.
# - `client.sendall(message.encode('utf-8'))`: Sends the encoded message to the client.
# - `except:`: Handles any exceptions that occur during message sending.
# - `clients.remove(client)`: Removes the client from the list if sending fails.
# - `def main():`: Defines the main function to start the server.
# - `if __name__ == "__main__":`: Checks if the script is being run directly.
# - `main()`: Calls the main function to initiate the server.