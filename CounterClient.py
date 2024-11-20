import socket

def start_client(folder_path, host='127.0.0.1', port=8080):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))


        client_socket.send(folder_path.encode())


        file_count = client_socket.recv(1024).decode()
        print(f"Number of files in the folder: {file_count}")
    except ConnectionRefusedError:
        print("Failed to connect to the server. Ensure the server is running.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    start_client(folder_path)
