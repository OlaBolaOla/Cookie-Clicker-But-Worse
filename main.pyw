#Hi :D
import tkinter as tk
import json
import os

DATA_PATH = "data.json"

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return {"cookies": 0, "test_mode": False}

def save_data():
    with open(DATA_PATH, "w") as f:
        json.dump(data, f)

def add_cookie():
    data["cookies"] += 1
    label.config(text=f"Cookies: {data['cookies']}")
    save_data()

data = load_data()

root = tk.Tk()
root.title("Cookie Clicker But Worse")

label = tk.Label(root, text=f"Cookies: {data['cookies']}", font=("Arial", 24))
label.pack(pady=20)

button = tk.Button(root, text="Click me!", command=add_cookie, font=("Arial", 18))
button.pack(pady=10)

root.mainloop()
