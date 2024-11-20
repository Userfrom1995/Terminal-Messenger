import socket
import threading
import sys


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print(f"\n{data.decode('utf-8')}")
        except:
            print("Disconnected from server")
            break


def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py [YourName]")
        sys.exit(1)

    name = sys.argv[1]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.205.126'
    port = 9999
    client_socket.connect((host, port))
    client_socket.sendall(name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            print("Exiting chat...")
            client_socket.close()
            sys.exit(0)
        client_socket.sendall(message.encode('utf-8'))


if __name__ == "__main__":
    main()