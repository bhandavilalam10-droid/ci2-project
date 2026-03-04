import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        # Length validation
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return
        
        if length > 50:
            messagebox.showerror("Error", "Length too large (Max 50)")
            return

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    characters = string.ascii_letters

    if include_numbers.get():
        characters += string.digits

    if include_symbols.get():
        characters += string.punctuation

    # Edge case: no options selected except letters
    if not include_numbers.get() and not include_symbols.get():
        pass  # letters already included

    password = ''.join(random.choice(characters) for _ in range(length))

    # Character inclusion check
    if include_numbers.get() and not any(char.isdigit() for char in password):
        password = password[:-1] + random.choice(string.digits)

    if include_symbols.get() and not any(char in string.punctuation for char in password):
        password = password[:-1] + random.choice(string.punctuation)

    result_var.set(password)


# GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

include_numbers = tk.BooleanVar()
include_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=include_numbers).pack()
tk.Checkbutton(root, text="Include Symbols", variable=include_symbols).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack(pady=10)

root.mainloop() 