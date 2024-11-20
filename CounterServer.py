import socket
import os

def count_files_in_directory(directory_path):
    try:

        return len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
    except FileNotFoundError:
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -2

def start_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")


        folder_path = client_socket.recv(1024).decode()
        print(f"Received folder path: {folder_path}")


        file_count = count_files_in_directory(folder_path)


        client_socket.send(str(file_count).encode())


        client_socket.close()

if __name__ == "__main__":
    start_server()
