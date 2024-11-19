import socket
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyautogui
import os

# Set up server IP (you can change this to the actual target IP if needed)
SERVER_IP = '127.0.0.1'  # Localhost for testing

# Ask the user for the port number before connecting
def get_port_from_user():
    port = simpledialog.askinteger("Input", "Please enter the port number to connect to the server:",
                                   minvalue=1, maxvalue=65535)
    return port

# Attempt to connect to the server
def connect_to_server(port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, port))
        return client_socket
    except socket.error:
        return None

# Send command to the server
def send_command(client_socket, command):
    client_socket.send(command.encode())
    response = client_socket.recv(4096).decode('utf-8')
    print(response)

# GUI Task Functions (for demonstration purposes)
def open_notepad():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    print("Screenshot saved as screenshot.png.")

def open_calculator():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('calc')
    pyautogui.press('enter')

def open_browser():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('chrome')  # Change to your browser's name (chrome, firefox, etc.)
    pyautogui.press('enter')

# Set up the Tkinter GUI
def create_gui(port):
    root = tk.Tk()
    root.title("Remote Access Tool")
    root.geometry("400x500")

    # Create a socket connection to the server
    client_socket = connect_to_server(port)

    if client_socket is None:
        show_error_message()
    else:
        # Create 20 buttons for different tasks
        button_labels = [
            "Open Notepad", "Take Screenshot", "Open Calculator", "Open Browser",
            "Run Command 1", "Run Command 2", "Run Command 3", "Run Command 4",
            "Run Command 5", "Send File", "Download File", "System Info", "Shutdown PC",
            "Open Task Manager", "Open File Explorer", "Volume Up", "Volume Down",
            "Mute", "Open MS Word", "Open Excel", "Exit"
        ]

        # Define button actions
        for idx, label in enumerate(button_labels):
            button = tk.Button(root, text=label, width=25, height=2, command=lambda idx=idx: handle_button_click(client_socket, idx))
            button.grid(row=idx, column=0, pady=5)

        root.mainloop()

# Show error message if server is not running (using messagebox)
def show_error_message():
    messagebox.showerror("Connection Error", "ERROR: Target hasn't opened the program yet!")
    exit()  # Exit the program after showing the error

# Handle button clicks
def handle_button_click(client_socket, idx):
    if idx == 0:
        open_notepad()
    elif idx == 1:
        take_screenshot()
    elif idx == 2:
        open_calculator()
    elif idx == 3:
        open_browser()
    elif idx == 4:
        send_command(client_socket, "echo 'Run Command 1'")
    elif idx == 5:
        send_command(client_socket, "echo 'Run Command 2'")
    elif idx == 6:
        send_command(client_socket, "echo 'Run Command 3'")
    elif idx == 7:
        send_command(client_socket, "echo 'Run Command 4'")
    elif idx == 8:
        send_command(client_socket, "echo 'Run Command 5'")
    elif idx == 9:
        send_file(client_socket, "example.txt")
    elif idx == 10:
        download_file(client_socket, "example.txt")
    elif idx == 11:
        send_command(client_socket, "systeminfo")
    elif idx == 12:
        send_command(client_socket, "shutdown /s /f /t 0")
    elif idx == 13:
        open_task_manager()
    elif idx == 14:
        open_file_explorer()
    elif idx == 15:
        pyautogui.press('volumup')  # Increase volume (specific to OS)
    elif idx == 16:
        pyautogui.press('volumedown')  # Decrease volume
    elif idx == 17:
        pyautogui.press('volumemute')  # Mute volume
    elif idx == 18:
        open_word()
    elif idx == 19:
        open_excel()

def open_task_manager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def open_file_explorer():
    pyautogui.hotkey('win', 'e')

def open_word():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('winword')
    pyautogui.press('enter')

def open_excel():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('excel')
    pyautogui.press('enter')

if __name__ == "__main__":
    # Ask for the port before connecting to the server
    port = get_port_from_user()
    if port is not None:
        create_gui(port)
    else:
        messagebox.showerror("Invalid Input", "Port number is required!")
        exit()
