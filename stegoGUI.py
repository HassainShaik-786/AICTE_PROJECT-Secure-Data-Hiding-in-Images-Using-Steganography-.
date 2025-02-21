import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Dictionary for encoding and decoding characters
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def encode_message():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    msg = entry_message.get()
    password = entry_password.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and Password cannot be empty!")
        return
    
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    output_path = "encryptedImage.png"
    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", "Message encoded successfully! Saved as encryptedImage.png")
    os.system(f"start {output_path}")

def decode_message():
    file_path = filedialog.askopenfilename(title="Select an Encrypted Image", filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    pas = entry_password.get()
    
    if pas != entry_password.get():
        messagebox.showerror("Error", "Incorrect Password!")
        return
    
    message = ""
    n, m, z = 0, 0, 0
    for i in range(len(entry_message.get())):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    messagebox.showinfo("Decryption Success", f"Decrypted Message: {message}")

# GUI Setup
root = tk.Tk()
root.title("Steganography GUI")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Enter Secret Message:").pack()
entry_message = tk.Entry(frame, width=40)
entry_message.pack()

tk.Label(frame, text="Enter Password:").pack()
entry_password = tk.Entry(frame, width=40, show='*')
entry_password.pack()

tk.Button(root, text="Encode Message", command=encode_message).pack(pady=5)
tk.Button(root, text="Decode Message", command=decode_message).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()

