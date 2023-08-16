import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
from datetime import datetime

class SelfieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selfie App")

        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.label = tk.Label(root)
        self.label.pack()

        self.capture_button = tk.Button(root, text="Capture Selfie", command=self.capture)
        self.capture_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.pack()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        self.logged_in = False
        self.logged_user = ""

    def login(self):
        # Replace this with your actual authentication logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "password":
            self.logged_in = True
            self.logged_user = username
            self.username_entry.config(state="disabled")
            self.password_entry.config(state="disabled")
            self.login_button.config(state="disabled")
            messagebox.showinfo("Success", "Logged in as {}".format(username))
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def capture(self):
        if not self.logged_in:
            messagebox.showerror("Error", "You must be logged in to capture a selfie.")
            return

        ret, frame = self.camera.read()
        if ret:
            selfie_filename = f"{self.logged_user}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
            cv2.imwrite(selfie_filename, frame)
            self.save_to_excel(self.logged_user, selfie_filename)
            messagebox.showinfo("Success", "Selfie saved as '{}'".format(selfie_filename))
        else:
            messagebox.showerror("Error", "Failed to capture selfie.")

    def save_to_excel(self, username, selfie_filename):
        data = {
            "Username": [username],
            "Selfie Filename": [selfie_filename],
            "Timestamp": [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        }
        df = pd.DataFrame(data)
        try:
            existing_data = pd.read_excel("selfies.xlsx")
            updated_data = pd.concat([existing_data, df], ignore_index=True)
            updated_data.to_excel("selfies.xlsx", index=False)
        except FileNotFoundError:
            df.to_excel("selfies.xlsx", index=False)

    def quit_app(self):
        self.camera.release()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = SelfieApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()