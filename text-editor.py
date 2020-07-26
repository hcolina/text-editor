import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """This opens a file for editing"""
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
        txt_edit.delete(1.0,tk.END)
        with open(filepath,"r") as input_file:
            text = input.file.read()
            text_edit.insert(tk.END, text)
        window.title()(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return