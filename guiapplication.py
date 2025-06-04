import tkinter as tk
root = tk.Tk()

label = tk.Label(root, text="Hello, GUI!")
button = tk.Button(root, text="Click Me")
label.pack()
button.pack()
root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

label = tk.Label(root, text="Hello, GUI!")
button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked!"))

label.pack()
button.pack()

root.mainloop()