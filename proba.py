import tkinter as tk
from tkinter import Toplevel, Label, Button

def custom_messagebox(title, message):
    # Create a new top-level window
    window = Toplevel()
    window.title(title)
    window.geometry("300x150")  # Set the window size

    # Customize the label with font, size, and color
    label = Label(window, text=message, font=("Arial", 14), fg="blue")
    label.pack(pady=20)

    # Add an OK button to close the window
    ok_button = Button(window, text="OK", command=window.destroy)
    ok_button.pack(pady=10)

# Example usage
root = tk.Tk()
root.withdraw()  # Hide the root window

custom_messagebox("Результат", "Все верно!")

root.mainloop()