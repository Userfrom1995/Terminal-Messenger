import socket

def start_server(host='127.0.0.1', port=8080, n=10):
    """
    Start the server to check if the received text has exactly N characters.
    :param host: Host address to bind the server
    :param port: Port to bind the server
    :param n: Number of characters to check
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}, expecting text of length {n}.")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the text from the client
        text = client_socket.recv(1024).decode()
        print(f"Received text: {text}")

        # Check the length of the text
        if len(text) == n:
            response = f"Text length is exactly {n}."
        else:
            response = f"Text length is {len(text)}, expected {n}."

        # Send the result back to the client
        client_socket.send(response.encode())

        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    n = int(input("Enter the expected number of characters (N): "))
    start_server(n=n)
