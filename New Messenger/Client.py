import socket
import threading

SERVER_HOST ='127.0.0.1'
SERVER_PORT = 8000
headers = {
    'User-Agent': 'Mozilla',  # Example header
       # Add any custom headers you need
}


def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(message)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
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
