import socket
import tkinter as tk
from tkinter import messagebox

# Function to handle the received message and show message boxes
def handle_button_click(message):
    if message == "Button1":
        messagebox.showinfo("Message", "Hi")
    elif message == "Button2":
        messagebox.showinfo("Message", "Hello")
    elif message == "Button3":
        messagebox.showinfo("Message", "Goodbye")
    # Add more button conditions as needed

# Create the socket server to listen for client connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# You can set the server host to '0.0.0.0' for listening on all available interfaces
# Use '127.0.0.1' if you want to test on the same machine
SERVER_HOST = '0.0.0.0'  # Listens on all network interfaces, allowing connections from other devices
SERVER_PORT = 12345       # The server's listening port

server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Create a Tkinter root window to display message boxes
root = tk.Tk()
root.withdraw()  # Hide the root window, we just want message boxes

# Main server loop to handle button clicks
while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break

    # Decode the data to get the button message
    message = data.decode()

    # Handle the button click by showing the appropriate message box
    handle_button_click(message)

# Close the client socket and server socket when done
client_socket.close()
server_socket.close()
