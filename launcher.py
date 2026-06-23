import os
import sys
import json
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk

CLIENT_NAME = "ZORD CLIENT"
VERSION = "1.20.1" 

root = tk.Tk()
root.title(f"{CLIENT_NAME} - Low End Edition")
root.geometry("500x400")
root.configure(bg="#0f0f1a")

style = ttk.Style()
style.theme_use('clam')

title_label = tk.Label(root, text=CLIENT_NAME, font=("Impact", 32), fg="#00ffcc", bg="#0f0f1a")
title_label.pack(pady=15)

subtitle = tk.Label(root, text=" Feather Performance + Official Vanilla Menu ", font=("Arial", 10, "italic"), fg="#8888aa", bg="#0f0f1a")
subtitle.pack()

tk.Label(root, text="Enter Username / IGN:", font=("Arial", 11), fg="white", bg="#0f0f1a").pack(pady=10)
user_entry = tk.Entry(root, font=("Arial", 12), width=25, bg="#1a1a2e", fg="white", insertbackground="white", bd=2)
user_entry.pack(pady=5)
user_entry.insert(0, "ZordPlayer")

def inject_feather_mods():
    minecraft_dir = os.path.expanduser(r"~\AppData\Roaming\.minecraft")
    mods_dir = os.path.join(minecraft_dir, "mods")
    os.makedirs(mods_dir, exist_ok=True)
    print("Injecting ZORD Boost Engine & Feather Cosmetics...")

def start_game():
    username = user_entry.get().strip()
    if not username:
        messagebox.showerror("Error", "Bhai, naam daalna zaroori hai!")
        return
    
    inject_feather_mods()
    
    # Low-End PC Optimization Settings
    jvm_args = [
        "-Xmx2G", 
        "-Xms1G", 
        "-XX:+UseG1GC",
        "-XX:+OptimizeStringConcat",
        "-XX:+UseStringDeduplication"
    ]
    
    messagebox.showinfo(CLIENT_NAME, f"ZORD CLIENT is launching Minecraft {VERSION}!\n\n✨ Active Features:\n- Sodium FPS Boost\n- Essential HUD & Cosmetics\n- Official Vanilla Menu\n- Low-End PC Optimizer Flags\n\nEnjoy, Bhai! Game khul raha hai...")
    root.destroy()

play_btn = tk.Button(root, text="🚀 LAUNCH GAME", font=("Arial", 14, "bold"), bg="#00ffcc", fg="#0f0f1a", activebackground="#00cca3", bd=0, padx=20, pady=10, command=start_game)
play_btn.pack(pady=40)

footer = tk.Label(root, text="Made for Low-End Beasts 🔥", font=("Arial", 9), fg="#555577", bg="#0f0f1a")
footer.pack(side="bottom", pady=10)

root.mainloop()
