import tkinter as tk

class SimulationViewer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="red")
        test = tk.Label(self, text="SimulationViewer" )
        test.pack()

class Timeline(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="blue")
        test = tk.Label(self, text="Timeline" )
        test.pack()

class SimConfig(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="purple")
        test = tk.Label(self, text="SimConfig" )
        test.pack()

class VariableViewer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="green")
        test = tk.Label(self, text="VariableViewer")
        test.pack()

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Gravity Simulator")
        self.parent.geometry("1024x768")

        #Setting relative sizes using weights
        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)

        #Create Frame objects for the GUI
        self.viewer = SimulationViewer(self)
        self.timeline = Timeline(self)
        self.SimConfig = SimConfig(self)
        self.VariableViewer = VariableViewer(self)

        #Use grid GUI layout to organise the frames according to design
        self.viewer.grid(row=0,
                        column=0,
                        pady=20,
                        padx=20,
                        sticky="NWSE")
        self.timeline.grid(row=1,
                        column=0,
                        pady=20,
                        padx=20,
                        sticky="NWSE")
        self.SimConfig.grid(row=0,
                        column=1,
                        pady=20,
                        padx=20,
                        sticky="NWSE")
        self.VariableViewer.grid(row=1,
                        column=1,
                        pady=20,
                        padx=20,
                        sticky="NWSE")

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
