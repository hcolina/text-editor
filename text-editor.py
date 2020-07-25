import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath: