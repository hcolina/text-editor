import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
        txt_edit.delete(1.0,tk.END)
        with open(filepath,"r") as input_file:
            text = input.file.read()
            text_edit.insert(tk.END, text)