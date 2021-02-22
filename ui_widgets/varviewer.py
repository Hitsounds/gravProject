import tkinter as tk
from functools import partial
import numpy as np

class VariableViewer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="green")
        #variables for state
        self.currentState = None
        self.simulation = None
        self.forces = None
        self.accelerations = None
        self.displacements = None
        self.velocities = None
        
        test = tk.Label(self, text="VariableViewer")
        test.pack()

        #Dropdown menu
        self.choice = tk.StringVar(self)
        self.configMenu = tk.OptionMenu(self, self.choice, {"placeholder"})
        self.configMenu.pack(side="top")

        #Details frame
        self.details = tk.Frame(self, bg="green")
        self.details.pack(side="top", fill="both")

    def construct_detaillist(self):
        '''Constructs the dropdown menu of options
        '''
        menu = self.configMenu["menu"]
        menu.delete(0, "end")
        for i in range(0, len(self.currentState)):
            name = self.currentState[i]["nick"] or f"Body {i}"
            menu.add_command(label=name, command=partial(self.render_body, f"{i}"))
        self.configMenu.update()

    def easy_update(self, state):
        '''
        Calculate all details when invoked so they can be displayed to the user
        quickly
        '''
        self.simulation = state
        self.currentState = self.simulation.getCurrentState()
        self.forces = [np.linalg.norm(x) for x in self.simulation._calculateForceOnBodies()]
        self.accelerations = [np.linalg.norm(x) for x in self.simulation._calculateAccelerationOnBodies()]
        self.displacements = [np.linalg.norm(x["pos"]) for x in self.currentState]
        self.velocities = [np.linalg.norm(x["vel"]) for x in self.currentState]
        self.construct_detaillist()

    def clear_detailsFrame(self):
        for widget in self.details.winfo_children():
            widget.destroy()

    def render_body(self, i):
        '''
        Renders the details of a body given index i
        '''
        self.construct_detaillist()
        i=int(i)
        name = self.currentState[i]["nick"] or f"Body {str(i)}"
        self.choice.set(name)
        self.clear_detailsFrame()

        #Labels with details
        self.simForceLabel = tk.Label(self.details,text=f"Force Experienced: {self.forces[i]} N")
        self.simAccelerationLabel = tk.Label(self.details,text=f"Acceleration: {self.accelerations[i]} ms^-2")
        self.simDisplacementLabel = tk.Label(self.details,text=f"Displacement from centre: {self.displacements[i]} m") 
        self.simVelocityLabel = tk.Label(self.details,text=f"Speed: {self.velocities[i]} ms^-1")

        #Pack Labels
        self.simForceLabel.pack(side="top")
        self.simAccelerationLabel.pack(side="top")
        self.simDisplacementLabel.pack(side="top")
        self.simVelocityLabel.pack(side="top")

    
