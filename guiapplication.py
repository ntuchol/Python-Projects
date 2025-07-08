import tkinter as tk

def button_clicked():
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("Button and Label GUI")

label = tk.Label(window, text="Click the button below:")
label.pack(pady=20)

button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack(pady=10)

window.mainloop()