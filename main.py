import tkinter as tk
from ui_widgets.simconfig import SimConfig
from ui_widgets.simviewer import SimulationViewer
from ui_widgets.timeline import Timeline
from ui_widgets.varviewer import VariableViewer


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
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

        #Padding between the widgets in pixels
        padding = 5 
        
        #Use grid GUI layout to organise the frames according to design
        self.viewer.grid(row=0,
                        column=0,
                        pady=padding,
                        padx=padding,
                        sticky="NWSE")
        self.timeline.grid(row=1,
                        column=0,
                        pady=padding,
                        padx=padding,
                        sticky="NWSE")
        self.SimConfig.grid(row=0,
                        column=1,
                        pady=padding,
                        padx=padding,
                        sticky="NWSE")
        self.VariableViewer.grid(row=1,
                        column=1,
                        pady=padding,
                        padx=padding,
                        sticky="NWSE")

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
