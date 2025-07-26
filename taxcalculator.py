import tkinter as tk
from tkinter import messagebox

def calculate_tax():
    try:
        income = float(income_entry.get())
        tax_rate = float(tax_rate_entry.get())
        tax = income * (tax_rate / 100)
        result_label.config(text=f"Tax Amount: ${tax:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for income and tax rate.")

root = tk.Tk()
root.title("Tax Calculator")
root.geometry("300x200")

income_label = tk.Label(root, text="Income:")
income_label.pack(pady=5)
income_entry = tk.Entry(root)
income_entry.pack(pady=5)

tax_rate_label = tk.Label(root, text="Tax Rate (%):")
tax_rate_label.pack(pady=5)
tax_rate_entry = tk.Entry(root)
tax_rate_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Tax", command=calculate_tax)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Tax Amount: $0.00", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
