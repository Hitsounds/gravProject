import tkinter as tk

class Timeline(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="blue")
        test = tk.Label(self, text="Timeline" )
        test.pack()
