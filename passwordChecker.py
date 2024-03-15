import tkinter as tk
from tkinter import messagebox
import re

def calculate_strength(password):
    score = 0
    length = len(password)
    if length >= 8:
        score += 1
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*()-+=_{}[\]:;<>,.?~]', password):
        score += 1
    
    return score

def check_password():
    password = password_entry.get()
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return
    
    strength_score = calculate_strength(password)
    
    if strength_score >= 3:
        messagebox.showinfo("Password Strength", "Your password is strong!")
    elif strength_score == 2:
        messagebox.showwarning("Password Strength", "Your password is moderate.")
    else:
        messagebox.showerror("Password Strength", "Your password is weak.")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create password entry field
password_label = tk.Label(root, text="Enter your password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create button to check password
check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()

# Run the Tkinter event loop
root.mainloop()
