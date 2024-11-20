import socket
import threading

censored_word = "secret"

def broadcast_message(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode())

def handle_client(client_socket, clients, lock):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            censored_message = message.replace(censored_word, "*" * len(censored_word))
            print(f"Server received (censored): {censored_message}")  # Server-side output after censoring
            lock.acquire()
            broadcast_message(censored_message, client_socket, clients)
            lock.release()
        except ConnectionResetError:
            break

    lock.acquire()
    clients.remove(client_socket)
    lock.release()
    client_socket.close()

def start_server(host="127.0.0.1", port=9090):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    clients = []
    lock = threading.Lock()

    while True:
        client_socket, _ = server_socket.accept()
        lock.acquire()
        clients.append(client_socket)
        lock.release()
        threading.Thread(target=handle_client, args=(client_socket, clients, lock)).start()

start_server()
