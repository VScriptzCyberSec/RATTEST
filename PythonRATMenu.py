import tkinter as tk
import socket
import sys

# Define a function to handle button clicks
def button_click(button_id):
    try:
        message = f"Button{button_id}"
        # Send the message to the server
        client_socket.sendall(message.encode())
    except Exception as e:
        print(f"Error sending message: {e}")

# Determine if the client is running on the same machine or a different device
# Use 'localhost' for the same device and the server's IP address for different devices
SERVER_HOST = 'localhost'  # Default to localhost for testing on the same device
SERVER_PORT = 12345        # The server's listening port

# Optional: you can ask the user to input the server's IP address if it's running on a different machine
# SERVER_HOST = input("Enter server IP address (or press enter for localhost): ") or 'localhost'

try:
    # Create a socket connection to the server
    print(f"Connecting to server at {SERVER_HOST}:{SERVER_PORT}...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)

finally:
    # Close the socket connection when done
    client_socket.close()
