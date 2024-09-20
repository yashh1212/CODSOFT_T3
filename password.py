import tkinter as tk
from tkinter import messagebox
import random
import string

generated_password = ""

def generate_password():
    global generated_password
    try:
        length = int(entry_length.get())  
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return
        elif length >16:
            messagebox.showerror("Error", "Password length should be at most 16 characters.")
            return
        characters = string.ascii_letters + string.digits
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {generated_password}")
        copy_button.pack(pady=10)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

def copy_password():
    if generated_password:
        window.clipboard_clear()
        window.clipboard_append(generated_password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")

title_label = tk.Label(window, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

length_label = tk.Label(window, text="Enter password length:")
length_label.pack()

entry_length = tk.Entry(window, width=10)
entry_length.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack_forget()

window.mainloop()
