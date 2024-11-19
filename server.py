import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    print("Client connected!")

    try:
        while True:
            # Receive the command from the client
            command = client_socket.recv(1024).decode('utf-8')

            if not command:
                break

            print(f"Received command: {command}")

            # Here you can implement whatever logic you need to execute commands, e.g., run system commands, etc.
            # For demonstration, we'll just echo the command back to the client.
            client_socket.send(f"Command '{command}' received and executed.".encode('utf-8'))
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()
        print("Client disconnected!")

# Function to attempt to bind and listen on every available port
def start_server():
    SERVER_IP = '0.0.0.0'  # Listen on all interfaces
    START_PORT = 1
    END_PORT = 65535

    # Try every port from START_PORT to END_PORT
    for port in range(START_PORT, END_PORT + 1):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((SERVER_IP, port))
            server_socket.listen(5)  # Set the server to listen for incoming connections
            
            print(f"Server is now listening on port {port}")
            break  # Exit the loop once a successful connection is made
            
        except socket.error as e:
            print(f"Port {port} is unavailable. Trying next port...")

    # Accept incoming client connections
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
