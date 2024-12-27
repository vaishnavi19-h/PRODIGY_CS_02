import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption and Decryption Tool")

        self.image = None
        self.encrypted = False

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image, state=tk.DISABLED)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image, state=tk.DISABLED)
        self.decrypt_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=500, height=500, bg="lightgray")
        self.canvas.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            self.image.thumbnail((500, 500)) 
            self.display_image(self.image)
            self.encrypted = False
            self.encrypt_button.config(state=tk.NORMAL)
            self.decrypt_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.DISABLED)

    def display_image(self, img):
        self.tk_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(250, 250, image=self.tk_image)

    def encrypt_image(self):
        if self.image:
            self.image = self.pixel_operation(self.image, mode="encrypt")
            self.display_image(self.image)
            self.encrypted = True
            self.encrypt_button.config(state=tk.DISABLED)
            self.decrypt_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)

    def decrypt_image(self):
        if self.image and self.encrypted:
            self.image = self.pixel_operation(self.image, mode="decrypt")
            self.display_image(self.image)
            self.encrypted = False
            self.encrypt_button.config(state=tk.NORMAL)
            self.decrypt_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL)

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
            )
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")

    def pixel_operation(self, img, mode):
        img_array = np.array(img)
        
        if mode == "encrypt":
            img_array = img_array[:, :, [2, 1, 0]]
        elif mode == "decrypt":
            img_array = img_array[:, :, [2, 1, 0]] 

        return Image.fromarray(img_array.astype('uint8'))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
