import tkinter as tk
from tkinter import messagebox

def greet_user():
    name = name_entry.get()
    if name.strip():
        messagebox.showinfo("Greeting", f"Hello, {name}! Welcome!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create the main window
root = tk.Tk()
root.title("Dialog Style GUI")

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry widget
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

# Create a button to trigger the greeting
greet_button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 12))
greet_button.pack(pady=10)

# Run the application
root.mainloop()