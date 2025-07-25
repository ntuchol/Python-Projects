import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Happy Birthday")
window.geometry("300x200") # Set window size

label = ttk.Label(window, text="Happy Birthday!", font=("Arial", 20))
label.pack(pady=50)

window.mainloop()
