#Client.py
import socket 
import threading 
import sys 
from substitution_cipher import encrypt_mssg,decrypt_mssg 
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
    host ='localhost' 
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
 
if name == "__main__": 
    main()
