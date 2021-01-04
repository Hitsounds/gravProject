import tkinter as tk

class Timeline(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="blue")
        test = tk.Label(self, text="Timeline" )
        test.pack()
