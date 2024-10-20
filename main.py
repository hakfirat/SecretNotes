import os
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter import Frame, Label

import pybase64
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from tkinter import messagebox



def encrypt_save():
    title = title_entry.get()
    secret_notes = secret_text.get(1.0, "end")
    key = masterkey_entry.get()

    secret_notes = secret_notes.encode("ascii")
    secret_notes = pybase64.b64encode(secret_notes)
    secret_notes = secret_notes.decode("ascii")

    if title == "":
        messagebox.showwarning(title="Warning", message="Please enter your title")
        return
    elif len(secret_notes) == 0:
        messagebox.showwarning(title="Warning", message="Please enter your secret")
        return
    elif key == "":
        messagebox.showwarning(title="Warning", message="Please enter a key")
        return

    try:
        with open(title + ".txt", "w") as file:
            file.writelines(f"{title}\n\n")
            file.writelines(f"{secret_notes}")
            title_entry.delete()
    except:
        pass
    title_entry.delete(0, END)
    secret_text.delete(1.0, END)
    masterkey_entry.delete(0, END)

def decrypt():
    pass


window = tk.Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)
window.config(width=800, height=500)

img = Image.open("top_secret.png")
img = img.resize(size=(75, 75))
img = ImageTk.PhotoImage(img)
panel = Label(window, image= img)
panel.pack()

title_label = Label(text="Enter your title")
title_label.config(padx=10)
title_label.pack()

title_entry = Entry(width=30)
title_entry.pack()

secret_label = Label(text="Enter your secret")
secret_label.config(padx=10)
secret_label.pack()

secret_text = Text(width=30, height=10)
secret_text.pack()

masterkey_label = Label(text="Enter master key")
masterkey_label.config(padx=10)
masterkey_label.pack()

masterkey_entry = Entry(width=30)
masterkey_entry.pack()

save_button = Button(text="Save & Encrypt", highlightbackground='#3E4149', command=encrypt_save)
save_button.pack(pady=10)

decrypt_button = Button(text="Decrypt", command=decrypt)
decrypt_button.pack()

window.mainloop()



