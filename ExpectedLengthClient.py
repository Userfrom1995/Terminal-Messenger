import socket

def start_client(host='127.0.0.1', port=8080):
    """
    Start the client to send text to the server and receive a response.
    :param host: Server host to connect to
    :param port: Server port to connect to
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))

        # Input the text to send
        text = input("Enter the text to send: ")
        client_socket.send(text.encode())

        # Receive and print the server's response
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
    except ConnectionRefusedError:
        print("Failed to connect to the server. Ensure the server is running.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
