import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Simple GUI Application")
root.geometry("300x200")

# Function to handle button click
def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Greeting", f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Add a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Add an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Add a button
button = tk.Button(root, text="Greet Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()