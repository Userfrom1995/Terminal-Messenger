import socket
import threading

SERVER_HOST = "3d0ca80b-6c3c-4513-8931-ce6156d28272-00-i27rtb4ksw1l.spock.replit.dev"
SERVER_PORT = 0000

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(message)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_HOST)
    print("[+] Connected to the server.")

    username = input("Enter your username: ")
    client_socket.send(username.encode())  # Send username to server

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    main()
