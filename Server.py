import socket
import threading

SERVER_HOST = '' # Listen on all available network interfaces
SERVER_PORT = 8000

clients = {}  # Dictionary to store client information (username: client_socket)

def handle_client(client_socket, client_address):
    username = client_socket.recv(1024).decode()  # Receive username from client
    clients[username] = client_socket  # Store client socket with username
    print(f"[+] {username} connected from {client_address}")

    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"{username}: {message}")
        # Broadcast message to all connected clients
        for client in clients.values():
            if client != client_socket:
                client.send(f"{username}: {message}".encode())

    print(f"[-] {username} disconnected")
    del clients[username]
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()
