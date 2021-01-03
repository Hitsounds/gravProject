import tkinter as tk

class SimConfig(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="purple")
        test = tk.Label(self, text="SimConfig" )
        test.pack()