import tkinter as tk
import numpy as np
from datetime import datetime
from datetime import timedelta
import copy

from ui_widgets.simconfig import SimConfig
from ui_widgets.simviewer import SimulationViewer
from ui_widgets.controller import Controller
from ui_widgets.varviewer import VariableViewer
from simulation_engines.cycles import cycles

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Gravity Simulator")
        self.parent.geometry("1024x768")

        #Simulator related objects
        self.simulation = None
        self.simulationActive = False
        self.simulationRealToSimRatio = 10000
        self.simulationMostRecentTimer = 0
        self.current_config = None

        #Setting relative sizes using weights
        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)

        #Create Frame objects for the GUI
        self.viewer = SimulationViewer(self)
        self.controller = Controller(self)
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
        self.controller.grid(row=1,
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


        #Create buttons to control simulation
        self.applyButton = tk.Button(self.controller, text="Apply Config", command=self.applyNewConfig)
        self.applyButton.pack(side="left",fill="y")

        button = tk.Button(self.controller, text="Pause/Resume", command=self.toggleSimState)
        button.pack(side="left",fill="y")

        button = tk.Button(self.controller, text="Reset", command=self.reset)
        button.pack(side="left",fill="y")

        self.simActiveLabel = tk.Label(self.controller,text="Simulation Active")     
        
    def applyNewConfig(self, new=True):
        '''
        Reads settings and creates a new simulation object from them
        '''
        if new:
            self.current_config = self.SimConfig.get_settings()
        #Set new number of lines for visualiser 
        self.viewer.set_number_of_lines(len(self.current_config["bodies"]))
        if self.current_config["general"]["simulation_mode"] == "cycles":
            #Create a new simulation object and run for 0 sec to get normalised coordinates
            self.simulation = cycles(copy.deepcopy(self.current_config["bodies"]))
            self.simulation.update(0)
            self.simulationRealToSimRatio = self.current_config["general"]["timestep"]
        #Plot first point: allows user to see that the settings applied successfully
        self.viewer.easy_update(self.simulation.getCurrentState())

    def toggleSimState(self):
        '''
        Called when the user wants to toggle the simulation state
        Disables the apply config button and kickstarts the simulator
        '''
        self.simulationActive = not self.simulationActive
        if self.simulationActive:
            self.applyButton["state"] = tk.DISABLED
            self.simActiveLabel.pack(side="left")
            self.simulationMostRecentTimer = 0
            self.simulate()
        else:
            self.simActiveLabel.pack_forget()
            self.VariableViewer.easy_update(self.simulation)
            self.applyButton["state"] = tk.NORMAL

    def reset(self):
        '''
        Resets to original state
        '''
        self.applyNewConfig(new=False)

    def simulate(self):
        if self.simulationMostRecentTimer == 0:
            #First run of simulate
            self.simulationMostRecentTimer = datetime.now()
        else:
            #Successive calls
            currentTime = datetime.now()
            delta = (currentTime - self.simulationMostRecentTimer).total_seconds() * float(self.SimConfig.settings["general"]["timestep"][2].get())
            res = self.simulation.update(delta)
            self.simulationMostRecentTimer = currentTime
            self.viewer.easy_update(res)
        if self.simulationActive:
            self.parent.after(1, self.simulate)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
