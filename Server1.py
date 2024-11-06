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
 
if name == "__main__": 
    main()
