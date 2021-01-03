import tkinter as tk

class SimulationViewer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="red")
        test = tk.Label(self, text="SimulationViewer" )
        test.pack()
