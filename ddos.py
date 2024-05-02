import socket
import time
from tabulate import tabulate

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the host and port
    host = "0.0.0.0"
    port = 9999

    # Bind to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print("Server listening on {}:{}".format(host, port))
    
    requests_data = []
    start_time = time.time()

    while True:
        # Accept a connection
        client_socket, addr = server_socket.accept()
        print("Connection from", addr)

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("Received data:", data)
        
        # Measure response time
        start_request_time = time.time()

        # Send a response back to the client
        response = "HTTP/1.1 200 OK\n\nServer received your request\n"
        client_socket.sendall(response.encode('utf-8'))

        # Measure response time
        end_request_time = time.time()
        response_time = end_request_time - start_request_time

        # Update requests data
        requests_data.append((addr[0], response_time))

        # Print the table
        print_metrics(requests_data, start_time)

        # Close the connection
        client_socket.close()

    # Close the server socket
    server_socket.close()

def print_metrics(data, start_time):
    current_time = time.time()
    total_requests = len(data)
    total_response_time = sum(response_time for _, response_time in data)
    average_response_time = total_response_time / total_requests if total_requests > 0 else 0
    request_rate = total_requests / (current_time - start_time) if current_time - start_time > 0 else 0

    headers = ["Metric", "Value"]
    table = [
        ["Total Requests", total_requests],
        ["Average Response Time", average_response_time],
        ["Request Rate (req/sec)", request_rate]
    ]

    print("Server Metrics:")
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()

if __name__ == "__main__":
    main()
