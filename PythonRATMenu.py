import tkinter as tk
import socket

# Define a function to handle button clicks
def button_click(button_id):
    message = f"Button{button_id}"
    # Send the message to the server
    client_socket.sendall(message.encode())

# Create a socket connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server details
SERVER_HOST = '127.0.0.1'  # The server's IP address
SERVER_PORT = 12345        # The server's listening port

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Create the main window
window = tk.Tk()
window.title("Client Button Interface")

# Create 20 buttons
for i in range(1, 21):
    button = tk.Button(window, text=f"Button {i}", command=lambda i=i: button_click(i))
    button.grid(row=(i-1)//5, column=(i-1)%5, padx=10, pady=10)

# Run the tkinter event loop
window.mainloop()

# Close the socket connection when done
client_socket.close()
