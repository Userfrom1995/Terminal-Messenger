import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(message)

def print_welcome_header():
    header = """
  ____                 _                       _             
 |  _ \  ___  ___ _ __| |_ _ __ ___   ___ _ __| | ___   __ _ 
 | | | |/ _ \/ _ \ '__| __| '_ ` _ \ / _ \ '__| |/ _ \ / _` |
 | |_| |  __/  __/ |  | |_| | | | | |  __/ |  | | (_) | (_| |
 |____/ \___|\___|_|   \__|_| |_| |_|\___|_|  |_|\___/ \__, |
                                                        |___/ 
"""
    print(header)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print_welcome_header()  # Print the Welcome header
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
