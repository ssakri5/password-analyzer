import re
import tkinter as tk
from tkinter import messagebox

def is_strong_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password contains at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False
    
    # Check if password contains at least one lowercase letter
    if not re.search("[a-z]", password):
        return False
    
    # Check if password contains at least one digit
    if not re.search("[0-9]", password):
        return False
    
    # Check if password contains at least one special character
    if not re.search("[!@#$%^&*()_+=\[{\]};:<>|./?,-]", password):
        return False
    
    # If all conditions pass, return True (password is strong)
    return True

def check_password():
    password = password_entry.get()
    if is_strong_password(password):
        messagebox.showinfo("Password Strength", "Strong password!")
    else:
        messagebox.showwarning("Password Strength", "Weak password! Please make sure your password contains at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.")

# GUI Setup
root = tk.Tk()
root.title("Password Analyzer")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter your password:")
label.pack()

password_entry = tk.Entry(frame, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(frame, text="Check Password", command=check_password)
check_button.pack(pady=10)

root.mainloop()
