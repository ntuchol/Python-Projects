import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple GUI Application")
root.geometry("300x200")

def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Greeting", f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Greet Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()
