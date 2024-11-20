import socket
import threading

def start_client(host="127.0.0.1", port=9090):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Message from server: {message}")
            except ConnectionResetError:
                break

    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        try:
            message = input("Enter message to send: ")
            client_socket.send(message.encode())
        except KeyboardInterrupt:
            client_socket.close()
            break

start_client()
