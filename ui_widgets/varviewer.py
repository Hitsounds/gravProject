import tkinter as tk

class VariableViewer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="green")
        test = tk.Label(self, text="VariableViewer")
        test.pack()
        